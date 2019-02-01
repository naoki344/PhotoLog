import Vue from 'vue';
import Album from '@/components/Album';
import Category from '@/components/Category';
import Folder from '@/components/Folder';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/gallery/album/:album_id',
      name: 'Album',
      component: Album
    },
    {
      path: '/gallery/album/:album_id/album_content/:album_content_id',
      name: 'Category',
      component: Category
    },
    {
      path: '/gallery/album/:album_id/album_content/:album_content_id/content/:album_content_folder_id',
      name: 'Folder',
      component: Folder
    }
  ]
});
