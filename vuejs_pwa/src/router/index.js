import Vue from 'vue';
import Hello from '@/components/Hello';
import Album from '@/components/Album';
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
      path: '/album',
      name: 'Album',
      component: Album
    },
    {
      path: '/folder',
      name: 'Folder',
      component: Folder
    }
  ]
});
