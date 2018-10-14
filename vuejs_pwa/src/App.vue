<template>
  <div id="app">
	<div class="c-header" >
		<c-header></c-header>
  	</div>
	<div class="c-sidebar" >
		<c-sidebar></c-sidebar>
  	</div>
    <main>
		<router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

main {
  text-align: center;
  display: block;
  padding-left: 230px;
  padding-top: 3rem;
}

.c-sidebar {
	position: fixed;
	top: 4rem;
	width: 230px;
	height: calc( 100vh - 4rem );
	overflow-y: auto;
	margin-bottom: 0;
}
.c-header {
	position: fixed;
	width: 100%;
	background-color: #fff;
	z-index: 2;
}

</style>
