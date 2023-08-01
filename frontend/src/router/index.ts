import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import DataView from '../views/DataView.vue'
import RegistersView from "@/views/RegistersView.vue";

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'data',
    component: DataView
  },
  {
    path: '/registers',
    name: 'registers',
    component: RegistersView
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
