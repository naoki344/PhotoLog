import Vue from 'vue';
import Album from '@/components/Album';
import Category from '@/components/Category';
import Folder from '@/components/Folder';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/album/:album_id',
      name: 'Album',
      component: Album
    },
    {
      path: '/category/:category_id',
      name: 'Category',
      component: Category
    },
    {
      path: '/Folder/:folder_id',
      name: 'Folder',
      component: Folder
    }
  ]
});
