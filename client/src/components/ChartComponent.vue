<template>
  <Bar
    id="my-chart-id"
    ref="barChart"
    :options="chartOptions"
    :data="formattedChartData"
  />
</template>

<script type="ts">
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  name: "ChartComponent",
  components: { Bar },
  props: {
    data: {
      type: Array,
      default: () => [],
    },
    options: {
      type: Object,
      default: () => ({}),
    },
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        ...this.options,
      },
    };
  },
  computed: {
    formattedChartData() {
      return {
        labels: this.data.map((item) => item.label),
          datasets: [
          {
            data: this.data.map((item) => {
              const [min, max] = item.value.split("-").map(Number);
              const midpoint = (min + max) / 2;
              return midpoint;
            }),
            backgroundColor: this.data.map((item) => item.backgroundColor)
          },
        ],
      };
    },
  },
  watch: {
    data: {
      handler(newValue) {
        this.$refs.barChart.update();
      },
      deep: true,
    },
    options: {
      handler(newValue) {
        this.chartOptions = {
          responsive: true,
          ...newValue,
        };
        this.$refs.barChart.update();
      },
      deep: true,
    },
  },
};
</script>
