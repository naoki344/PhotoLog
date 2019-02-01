<template lang="html">
  <div class="centerx labelx">
	  <el-row>
		<vue-picture-swipe :items="image_list[album_content_folder_id]"></vue-picture-swipe>
	  </el-row>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data () {
    return {
    };
  },
  created () {
    var target = {
      album_id: this.$route.params.album_id,
      album_content_id: this.$route.params.album_content_id,
      album_content_folder_id: this.$route.params.album_content_folder_id
    };
    this.$store.commit('SetTarget', target);
    this.$store.commit('SetGalleryFolderUrl');
    this.$store.commit('GetContentFileList');
  },
  computed: {
    ...mapState([
      'album_content_list',
      'album_content_folder_id',
      'url_gallery_album',
      'image_list'
    ])
  }
};
</script>

<style lang="scss">
.content__image {
	width: 100%;
}

.my-gallery{
	display: flex;
	flex-wrap: wrap;
    //justify-content: space-around;
 	figure {
    	margin: 0;
		@media screen and (max-width: 580px) {
			width: 100%;
		}
		@media (min-width: 580px) and (max-width: 1020px) {
			width: 50%;
		}
		@media (min-width: 1020px) and (max-width: 1500px) {
			width: 33%;
		}
		width: 25%;
		a img {
			width: 100%;
			display: block;
		}
	}
}
</style>
