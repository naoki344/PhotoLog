<template>
  <div id="app">
	  <el-container>
		<el-aside style="width:230px; position: fixed; height:100vh;" >
			<c-sidebar></c-sidebar>
		</el-aside>
		<el-container class="el-main-container">
			<el-header >
				<c-header></c-header>
			</el-header>
			<el-main>
				<router-view></router-view>
			</el-main>
		</el-container>
	  </el-container>
  </div>
</template>

<script>
export default {
  name: "app"
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

.el-main-container {
  padding-left: 230px;
}
.el-header {
  position: fixed;
  width: 100%;
  padding: 0;
  height: 60px;
}

.el-main {
  padding-top: 60px;
}
</style>
