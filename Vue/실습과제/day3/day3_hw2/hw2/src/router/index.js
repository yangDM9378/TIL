import Vue from 'vue'
import VueRouter from 'vue-router'
import FirstView from '@/views/FirstView'
import SecondView from '@/views/SecondView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/First',
    name: 'First',
    component: FirstView
  },
  {
    path: '/Second',
    name: 'Second',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: SecondView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
