<template lang="html">
  <div class="centerx labelx">
	  <el-row>
  		<el-col style="padding: 10px" :xs="24" :sm="12" :md="8" :lg="6" :xl="6" v-for="content in category_content_list[album_content_id]">
  		  <el-card :body-style="{ padding: '8px' }">
			  <div class="card__image" :style="'background-image:url(' + content.content.info.thumbnail_url + ');'">
				<a :href="url_gallery_album_content + '/content/' + content.content.content_id">link</a>
			  </div>
  		    <div style="padding: 5px;">
			  <span class="card__title">{{ content.content.info.name }}</span>
			  <span class="card__description">{{ content.content.info.description }}</span>
  		      <div class="bottom clearfix">
				<el-tag size="small" >Folder</el-tag>
  		        <time class="time">{{ content.content.info.last_update_date }}</time>
  		      </div>
  		    </div>
  		  </el-card>
  		</el-col>
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
    this.album_content_id = this.$route.params.album_content_id;
    var target = {
      album_id: this.$route.params.album_id,
      album_content_id: this.$route.params.album_content_id,
      album_content_folder_id: ''
    };
    this.$store.commit('SetTarget', target);
    this.$store.commit('SetCategoryContentList');
    this.$store.commit('SetGalleryAlbumContentUrl');
  },
  computed: mapState([
    'category_content_list',
    'url_gallery_album_content'
  ])
};
</script>

<style lang="scss">
.labelx {
  margin-top: 20px;
  text-align: left;

  .vs-input {
    margin: 10px;
  }
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  text-align: right;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
}

.clearfix:after {
    clear: both
}
.card__image {
	height: 250px;
	background-position: top center;
    background-repeat: no-repeat;
    background-size: cover;
	position: relative;
	a {
    	position: absolute;
    	top: 0;
    	left: 0;
    	width: 100%;
    	height: 100%;
    	text-indent: -999px;
	}
	a:hover {
		background-color: #FFF;
    	opacity: 0.5;
	}
}

.card__description {
	display: block;
	color: #666;
}

.card__title {
	display: block;
	font-size: 18px;
}
</style>
