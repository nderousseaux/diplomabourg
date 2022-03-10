import {createRouter, createWebHistory} from 'vue-router'

// @ : est le chemin : src/
import Home from '@/views/Home.vue'
import Maps from '@/views/Maps.vue'

const routes = [
    {
        path: "/",
        name: 'Maps',
        component: Maps
    },
    {
        path: "/Home",
        name: 'Home',
        component: Home
    }
]

const router = createRouter({
    history : createWebHistory(process.env.BASE_URL),
    routes

})

export default router