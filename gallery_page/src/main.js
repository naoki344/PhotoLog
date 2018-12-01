// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import router from './router';
import App from './App';

import store from '@/store';
import Header from '@/components/Header';

import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/ja';
import 'element-ui/lib/theme-chalk/index.css';
import VuePictureSwipe from 'vue-picture-swipe';

Vue.config.productionTip = false;
Vue.component('c-header', Header);
Vue.component('vue-picture-swipe', VuePictureSwipe);
Vue.use(ElementUI, { locale });

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
});
