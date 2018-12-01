import Vue from 'vue';
import Vuex from 'vuex';
import * as Folder from '@/model/folder';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    folder: Folder.FolderModel,
    folder_form: Folder.FolderFromModel
  },
  mutations: {
    setFolder (state, folder) {
      state.folder = folder;
    },
    setFolderForm (state, form) {
      state.folder = form;
    }
  },
  methods: {
  }
});
