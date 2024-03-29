import {createApp} from 'vue'
import App from './App.vue'
import Notifications from '@kyvg/vue3-notification'
import axios from 'axios'
import {createRouter, createWebHashHistory} from 'vue-router'

import Homepage from "./components/HopePage/Homepage.vue";
import About from "./components/About/About.vue";
import './assets/main.css'


const routes = [
    {path: '/home', component: Homepage},
    {path: '/get_use_code', component: Homepage},
    {path: '/about', component: About},
];

const router = createRouter(
    {history: createWebHashHistory(),routes}
)

const app = createApp(App)

app.use(router)
app.config.globalProperties.$axios = axios;
app.use(Notifications)

app.mount('#app')

