<template lang="html">
  <div class="centerx labelx">
	  <el-row>
		<vue-picture-swipe :items="image_list"></vue-picture-swipe>
  		<!--el-col style="padding: 5px" :xs="24" :sm="12" :md="8" :lg="6" :xl="6" v-for="file in file_list">
			<img class="content__image" :src="'http://localhost:5000/trombone344%40gmail.com' + file.url">
  		</el-col-->
	  </el-row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      server_url: 'http://view.photolog.online',
      folder: '',
      file_list: '',
      image_list: []
    };
  },
  mounted () {
    var config = {
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*'
      }
    };
    axios
      .get(this.server_url + '/trombone344%40gmail.com/folder/' + this.$route.params.folder_id, config)
      .then(response => {
        var folder = response.data;
        this.folder = folder;
      });
    axios
      .get(this.server_url + '/trombone344%40gmail.com/folder/' + this.$route.params.folder_id + '/file', config)
      .then(response => {
        var FileList = response.data;
        this.file_list = FileList;
        FileList.forEach((file) => {
          var img = {
            src: this.server_url + '/trombone344%40gmail.com' + file.url,
            thumbnail: this.server_url + '/trombone344%40gmail.com' + file.url,
            w: file.shape_size.width,
            h: file.shape_size.height,
            alt: 'some numbers on a grey background' // optional alt attribute for thumbnail image<Paste>
          };
          this.image_list.push(img);
        });
      });
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
