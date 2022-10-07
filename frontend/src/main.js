import { createApp } from 'vue'
import App from './App.vue'
import Notifications from '@kyvg/vue3-notification'
import axios from 'axios'

import './assets/main.css'

const app = createApp(App)
app.config.globalProperties.$axios = axios;
app.use(Notifications)
app.mount('#app')
