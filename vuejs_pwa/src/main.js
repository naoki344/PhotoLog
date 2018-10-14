// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'
import App from './App'

import Sidebar from '@/components/Sidebar'
import Header from '@/components/Header'

import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ja'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
Vue.component('c-sidebar', Sidebar)
Vue.component('c-header', Header)
Vue.use(ElementUI, {locale})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
