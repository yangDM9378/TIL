import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import NocolorView from '@/views/NocolorView'
import NotfoundView from '@/views/NotfoundView'
import SsafleafView from '@/views/SsafleafView'
import SsaflingView from '@/views/SsaflingView'
import SsaflowerView from '@/views/SsaflowerView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/happeed',
    name: 'NocolorView',
    component: NocolorView
  },
  {
    path: '/*',
    name: 'NotfoundView',
    component: NotfoundView
  },
  {
    path: '/happling',
    name: 'SsafleafView',
    component: SsafleafView
  },
  {
    path: '/happlossome',
    name: 'SsaflingView',
    component: SsaflingView
  },
  {
    path: '/happlower',
    name: 'SsaflowerView',
    component: SsaflowerView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
