<template lang="html">
  <div class="centerx labelx">
    <vs-input vs-label="フォルダー名" placeholder="フォルダーの表示名" v-model="folder_name"/>
	<vs-textarea counter="20" label="フォルダーの説明" :counter-danger.sync="counterDanger" v-model="description" />
    <vs-input vs-label="フォルダー名" placeholder="フォルダーの表示名" v-model="folder_"/>
  </div>
</template>

<script>
export default {
  data () {
    return {
      folder_name: '',
      value2: '',
      description: '',
      counterDanger: false
    }
  }
}
</script>

<style lang="scss">
.labelx {
	text-align: left;

	.vs-input {
    	margin: 10px;
	}
}
</style>
