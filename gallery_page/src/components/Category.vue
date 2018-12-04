<template lang="html">
  <div class="centerx labelx">
	  <el-row>
  		<el-col style="padding: 10px" :xs="24" :sm="12" :md="8" :lg="6" :xl="6" v-for="folder in folder_list">
  		  <el-card :body-style="{ padding: '8px' }">
			  <div class="card__image" :style="'background-image:url(' + folder.info.thumbnail_url + ');'">
				<a :href="'/#/folder/' + folder.folder_id">link</a>
			  </div>
  		    <div style="padding: 5px;">
			  <span class="card__title">{{ folder.info.name }}</span>
			  <span class="card__description">{{ folder.info.description }}</span>
  		      <div class="bottom clearfix">
				<el-tag size="small" >Folder</el-tag>
  		        <time class="time">{{ folder.info.last_update_date }}</time>
  		      </div>
  		    </div>
  		  </el-card>
  		</el-col>
	  </el-row>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      server_url: 'http://view.photolog.online',
      category: '',
      folder_list: ''
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
      .get(this.server_url + '/trombone344%40gmail.com/category/' + this.$route.params.category_id, config)
      .then(response => {
        var category = response.data;
        this.category = category;
      });
    axios
      .get(this.server_url + '/trombone344%40gmail.com/category/' + this.$route.params.category_id + '/folder', config)
      .then(response => {
        var FolderList = response.data;
        this.folder_list = FolderList;
      });
  }
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
