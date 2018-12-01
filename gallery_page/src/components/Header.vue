<template lang="html">
	<div id="c-header">
    <!-- Loader -->
    	<!-- Page title -->
    	<div class="page-title top-content">
    	    <div class="page-title-text wow fadeInUp">
    	    	<h1>思い出箱</h1>
				<img src="../assets/photo_log_top.png">
    	    </div>
    	</div>
	</div>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    };
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>

<style>
h1 {
	text-align: center;
}
.top-content img {
	width: 100%;
	height: auto;
}
</style>

