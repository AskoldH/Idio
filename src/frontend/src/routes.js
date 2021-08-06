import Vue from 'vue'
import VueRouter from 'vue-router'
import Idiom from './views/Idiom.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'idiom',
            component: Idiom,
        },
    ]
})
