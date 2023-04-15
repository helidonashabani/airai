<template>
    <div class="chatbot-wrapper">
        <div class="chatbot">
        <div class="chatbot__conversation">
            <div class="chatbot__messages">
            <div v-for="(message, index) in messages" :key="index" :class="['chatbot__message', { incoming: message.incoming }]">
                <div class="chatbot__message-content">
                   <p>{{ message.answer }}</p> 
                   <p v-if="message.source">Source: {{ message.source }}</p>
                </div>
                <div class="chart-bar" v-if="message.chart">
                  <chart-component  :data="message.chartData"
                    :options="{ responsive: true}">
                  </chart-component>
                </div>
            </div>
            </div>
            <form class="chatbot__input" @submit.prevent="sendMessage">
                <input type="text" class="chatbot__input-field"  v-model="newMessage"  placeholder="Type your message here...">
                <button class="chatbot__send-button">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M2.04 21L23 12 2.04 3 2 10l15 2-15 2z"/></svg>
                </button>
            </form>
        </div>
        </div>
    </div>

  </template>
  
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ChartComponent from '@/components/ChartComponent.vue';

import apiClient from '@/api';

interface Message {
  answer: string;
  source?: string;
  incoming: boolean;
  chart?: boolean;
  chartData?: FormattedDataItem[];
}

interface ColorMapItem {
  range: [number, number];
  color: string;
  label: string;
}

interface ApiResponse {
  data: { [key: string]: string };
}

interface FormattedDataItem {
  label: string;
  value: string;
  backgroundColor: string;
}

@Component({
  components: {
    ChartComponent,
  },
})
export default class AirQualityAI extends Vue {
  public messages: Message[] = [];
  public newMessage = '';
  public apiResponse: any = null;

  public created(): void {
    this.messages.push({
      answer: 'Hello! How can I assist you today?',
      incoming: false,
    });
    document.title = 'Air Quality AI';
  }

  public async sendMessage(): Promise<void> {
    if (!this.newMessage) {
      return;
    }

    this.messages.push({ answer: this.newMessage, incoming: false });

    const message = this.newMessage;
    this.newMessage = '';

    try {
      const response = await apiClient.post('/air_quality', {
        question: message,
      });
      if (response?.data?.answer) {
          const formattedChartData = this.drawChart(response?.data?.data);

          this.messages.push({
            answer: response?.data?.answer,
            source: response?.data?.source,
            incoming: true,
            chart: true,
            chartData: formattedChartData,
          });
        } else {
          this.messages.push({
            answer:
              'Sorry, I could not understand your query. Please try again!',
            incoming: true,
          });
        }
      } catch (error) {
        console.error(error);
        this.messages.push({
          answer:
            'Sorry, there was an error processing your request. Please try again later!',
          incoming: true,
        });
      }
    }

    public drawChart(apiDataResponse: ApiResponse): FormattedDataItem[] {
      if (!apiDataResponse) {
        return [];
      }

      const formatted_data: FormattedDataItem[] = Object.entries(apiDataResponse).map(([city, value]) => {
        const { range, color, label } = this.getColorAndLabel(value);
        return {
          label: `${city}-${label}`,
          value: value,
          backgroundColor: color,
        };
      });
      return formatted_data;
    }


    public getColorAndLabel(value: string): ColorMapItem {
      const colorMap: ColorMapItem[] = [
        { range: [0, 50], color: "green", label: "Good" },
        { range: [51, 100], color: "yellow", label: "Moderate" },
        { range: [101, 150], color: "orange", label: "Unhealthy for sensitive groups" },
        { range: [151, 200], color: "red", label: "Unhealthy" },
        { range: [201, 300], color: "orchid", label: "Very Unhealthy" },
        { range: [301, 500], color: "maroon", label: "Hazardous" },
      ];

        const [min, max] = value.split("-").map(Number);

        for (const item of colorMap) {
          if (min >= item.range[0] && max <= item.range[1]) {
            return item;
          }
        }
        return { range: [-1, -1], color: "", label: "Unknown" };
      }
    
  }
  </script>
  
  <style lang="scss" scoped>

.chatbot-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}



  .chatbot {
    height: 100%;
    display: flex;
    flex-direction: column;
    width: 50%;
  
    &__conversation {
      flex-grow: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 20px;
    }
  
    &__messages {
      display: flex;
      flex-direction: column;
      color: black;

      .chart-bar {
        margin: 10px;
      }
    }
  
    &__message {
      background-color: #f7f7f8;
      margin-bottom: 20px;
      border-radius: 30px;
      padding: 5px 5px 5px 20px;

      &.incoming {
        background-color: #f7f7f8;
      }
    }
  
    &__message-content {
      font-size: 14px;
    }
  
    &__input {
        display: flex;
        display: flex;
        align-items: center;
        background-color: #fff;
        padding: 10px;
        border-radius: 10px;
        border: 0.3px;
        border: 0.5px solid #dd2c00;
        caret-color: #dd2c00;

  
      &-field {

        flex-grow: 1;
        padding: 5px;
        border: none;
        border-radius: 5px;
        margin-right: 10px;
        &:focus {
            outline: none;
        }
      }
    }

    &__send-button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        outline: none;
        padding: 0;
        width: 24px;
        height: 24px;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;

        & svg {
            fill: #dd2c00;
            width: 100%;
            height: 100%;
        }
      }
  }

  </style>
  