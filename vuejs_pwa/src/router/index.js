import Vue from 'vue';
import Hello from '@/components/Hello';
import Folder from '@/components/Folder';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/folder',
      name: 'Folder',
      component: Folder
    }
  ]
});
