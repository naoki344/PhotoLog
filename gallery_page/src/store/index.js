import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    server_url: 'http://localhost:5000',
    album_id: '',
    album_content_id: '',
    album_content_folder_id: '',
    album_content_list: [],
    image_list: {},
    category_content_list: {},
    url_gallery_album: '',
    url_gallery_album_content: '',
    url_gallery_album_content_folder: ''
  },
  mutations: {
    SetAlbumContentList (state) {
      var config = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8',
          'Access-Control-Allow-Origin': '*'
        },
        withCredentials: true
      };
      axios
        .get(state.server_url + '/gallery/album/' + state.album_id + '/album_content/', config)
        .then(response => {
          var AlbumContentList = response.data;
          state.album_content_list = AlbumContentList.content_list;
        });
    },
    SetCategoryContentList (state) {
      var config = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8',
          'Access-Control-Allow-Origin': '*'
        }
      };
      axios
        .get(state.server_url + '/gallery/album/' + state.album_id + '/album_content/' + state.album_content_id + '/content', config)
        .then(response => {
          var CategoryContentList = response.data;
          Vue.set(state.category_content_list, state.album_content_id, CategoryContentList.content_list);
        });
    },
    SetTarget (state, target) {
      state.album_id = target.album_id;
      state.album_content_id = target.album_content_id;
      state.album_content_folder_id = target.album_content_folder_id;
      Vue.set(state.category_content_list, state.album_content_id, []);
      Vue.set(state.image_list, state.album_content_folder_id, []);
    },
    SetGalleryAlbumUrl (state) {
      state.url_gallery_album = '/#/gallery/album/' + state.album_id;
    },
    SetGalleryAlbumContentUrl (state) {
      state.url_gallery_album_content = '/#/gallery/album/' + state.album_id + '/album_content/' + state.album_content_id;
    },
    SetGalleryFolderUrl (state) {
      state.url_gallery_album_content_folder = '/#/gallery/album/' + state.album_id + '/album_content/' + state.album_content_id + '/content/' + state.album_content_folder_id;
    },
    GetContentFileList (state) {
      var config = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8',
          'Access-Control-Allow-Origin': '*'
        }
      };
      axios
        .get(state.server_url + '/gallery/album/' + state.album_id + '/album_content/' + state.album_content_id + '/content/' + state.album_content_folder_id + '/file', config)
        .then(response => {
          var FileList = response.data;
          var ImageList = [];
          FileList.forEach((file) => {
            var img = {
              src: state.server_url + file.url,
              thumbnail: state.server_url + file.url,
              w: file.shape_size.width,
              h: file.shape_size.height,
              alt: 'some numbers on a grey background' // optional alt attribute for thumbnail image<Paste>
            };
            ImageList.push(img);
          });
          Vue.set(state.image_list, state.album_content_folder_id, ImageList);
        });
    }
  },
  getters: {
  },
  methods: {
  }
});
// .get(ServerUrl + '/gallery/album/' + this.$route.params.album_id, config)

// .get(this.server_url + '/gallery/album/' + this.$route.params.album_id + '/album_content/' + this.$route.params.content_id + '/content', config)
// .get(this.server_url + '/gallery/album/' + this.$route.params.album_id + '/album_content/' + this.$route.params.content_id + '/content/' + this.$route.params.folder_id, config)
