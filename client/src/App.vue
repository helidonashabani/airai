<template>
  <div id="app">
    <AirQualityAI />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import AirQualityAI from './components/AirQualityAI.vue'

@Component({
  components: {
    AirQualityAI
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
body {
  margin: 0;
  padding: 0;
  font-family: "Roboto", sans-serif;

}

#app {
  height: 100vh;
  background: #fff;
  margin:0;
}
</style>
