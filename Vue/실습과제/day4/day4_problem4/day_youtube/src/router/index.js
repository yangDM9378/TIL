import Vue from 'vue'
import VueRouter from 'vue-router'
import SaffyTube from '@/views/YoutubeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/ssafytube',
    name: 'ssafytube',
    component: SaffyTube
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router
