import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Simulation from '../components/Simulation.vue'
import Save from '../components/Save.vue'
import Build from '../components/Build.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },

    {
        path: '/Simulation',
        name: 'Simulation',
        component: Simulation,
    },

    {
        path: '/Save/:id',
        name: 'Save',
        component: Save,
    },

    {
        path: '/Build',
        name: 'Build',
        component: Build,
    }
]

const router = createRouter({

    history: createWebHistory(),

    routes
})

export default router