import Vue from 'vue'
import adminGEStory from './adminGEStory.vue'
import '@/filters'


Vue.config.productionTip = false

new Vue({
  render: h => h(adminGEStory),
}).$mount('#adminGEStory')
