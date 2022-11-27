import { createApp } from 'vue'
import App from './App.vue'
import Notifications from '@kyvg/vue3-notification'
import axios from 'axios'

import NextButton from "./components/NextButton/NextButton.vue";
import EduVideoTile from "./components/EduVideoTile/EduVideoTile.vue";

import './assets/main.css'

const app = createApp(App)
app.config.globalProperties.$axios = axios;
app.use(Notifications)
app.mount('#app')

app.component('NextButton', NextButton)
app.component('EduVideoTile', EduVideoTile)

