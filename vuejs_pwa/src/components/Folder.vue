<template lang="html">
  <div class="centerx labelx">
	<el-col :span="6"><el-input placeholder="Please input" v-model="input"></el-input></el-col>
	<textarea>{{info}}</textarea>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      input: '',
      info: ''
    }
  },
  mounted () {
    var config = {
      headers: { 'Content-Type': 'application/json;charset=UTF-8', 'Access-Control-Allow-Origin': '*' }
    }
    axios
      .get('http://localhost:5000/photo_log/miyoshi%40example.com/folder/', config)
      .then(response => (this.info = response.data))
  }
}
</script>

<style lang="scss">
.labelx {
	margin-top: 20px;
	text-align: left;

	.vs-input {
    	margin: 10px;
	}
}
</style>
