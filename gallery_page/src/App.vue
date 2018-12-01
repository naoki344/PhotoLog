<template>
  <div id="app">
				<c-header></c-header>
				<router-view></router-view>
	  <!--el-container>
		<el-container class="el-main-container">
			<el-header >
			</el-header>
			<el-main>
			</el-main>
		</el-container>
	  </el-container-->
  </div>
</template>

<script>
export default {
  name: 'app'
};
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

/*
.el-header {
  position: fixed;
  width: 100%;
  padding: 0;
  height: 60px;
}

.el-main {
  padding-top: 60px;
}
*/
</style>
