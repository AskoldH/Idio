import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import '@fortawesome/fontawesome-free/js/all'


Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
