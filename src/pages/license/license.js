import Vue from 'vue'
import License from './license.vue' 


Vue.config.productionTip = false

new Vue({
  render: h => h(License),
}).$mount('#license')
