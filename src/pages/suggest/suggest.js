import Vue from 'vue'
import Suggest from './suggest.vue'


Vue.config.productionTip = false

new Vue({
  render: h => h(Suggest),
}).$mount('#suggest')
