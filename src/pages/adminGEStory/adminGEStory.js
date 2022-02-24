import Vue from 'vue'
import adminGEStory from './adminGEStory.vue'


Vue.config.productionTip = false

new Vue({
  render: h => h(adminGEStory),
}).$mount('#adminGEStory')
