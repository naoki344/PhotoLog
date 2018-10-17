<template lang="html">
  <div class="centerx labelx">
    <el-form ref="form" :model="folder_form" label-width="160px">
        <h4>フォルダー情報の更新</h4>
        <el-form-item label="フォルダーID"><el-input placeholder="Please input" v-model="folder_form.folder_id" :disabled="true"></el-input></el-form-item>
        <el-form-item label="フォルダー名"><el-input placeholder="Please input" v-model="folder_form.name"></el-input></el-form-item>
        <el-form-item label="説明"><el-input type="textarea" v-model="folder_form.description"></el-input></el-form-item>
        <el-form-item label="公開状態">
            <el-radio-group v-model="folder_form.release_status">
                  <el-radio label="OPEN">公開</el-radio>
                  <el-radio label="CLOSE">非公開</el-radio>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="公開範囲">
            <el-radio-group v-model="folder_form.share_range">
                  <el-radio label="PRIVATE">プライベート</el-radio>
                  <el-radio label="PUBLIC">パブリック</el-radio>
                  <el-radio label="PASSFRASE">パスワード認証</el-radio>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="公開URL"><el-input placeholder="Please input" v-model="folder_form.share_url" :disabled="true"></el-input></el-form-item>
        <el-form-item label="サムネイル画像URL"><el-input placeholder="Please input" v-model="folder_form.thumbnail_url"></el-input></el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">更新</el-button>
        </el-form-item>
    </el-form>
        <el-col :xs="24" :sm="24" :md="12" :lg="8" ><pre>{{info}}</pre></el-col>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      server_url: "http://localhost:5000/photo_log",
      folder_id: "",
      folder_form: {
        folder_id: "",
        name: "",
        release_status: ""
      },
      info: ""
    };
  },
  mounted() {
    var config = {
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*"
      }
    };
    axios
      .get(this.server_url + "/miyoshi%40example.com/folder/", config)
      .then(response => {
        var folders = response.data;
        this.folder_form = folders[0];
        this.folder_id = folders[0].folder_id;
        this.info = folders;
      });
  },
  methods: {
    onSubmit() {
      axios
        .put(
          this.server_url + "/miyoshi%40example.com/folder/" + this.folder_id,
          this.folder_form
        )
        .then(response => {
          this.$message({
            message: "Folder Info Update Sucsess",
            type: "success"
          });
        });
    }
  }
};
</script>

<style lang="scss">
.labelx {
  margin-top: 20px;
  max-width: 720px;
  text-align: left;

  .vs-input {
    margin: 10px;
  }
}
</style>
