import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import Popup from '@/components/Popup'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/popup',
      name: 'Popup',
      component: Popup
    }
  ]
})
