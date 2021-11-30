<template>
  <div>
    <div class="position"></div>
    <div class="detailsearch">
      <el-row :gutter="14">
        <el-col :span="6"
          ><div class="logo1">
            <img src="../assets/BDP.png" /></div
        ></el-col>
        <el-col :span="12"
          ><div class="box1">
            <el-autocomplete
              class="inline-input"
              placeholder="Please enter the keyword you want to search"
              @keyup.enter.native="dosearch"
              v-model="search"
            ></el-autocomplete></div
        ></el-col>
        <el-col :span="4"
          ><div class="box2">
            <el-button type="primary" icon="el-icon-search" @click="dosearch"
              >Search</el-button
            >
          </div></el-col
        >
      </el-row>
    </div>
  </div>
</template>

<script>
import Util from "@/common/Util";
export default {
  name: "searchbar",
  props: ["search"],

  data() {
    //  搜索框
    return {
      diseaseList: [], //这个值是需要匹配的值
      disease: "", //这个值是用户正在输入的值
      search: "",
      lists: [],
      params: "",
    };
  },

  methods: {
    dosearch() {
      Util.searchAPI(this.$router, this.search);
      //   this.$http
      //     .get("/api/db/search", {
      //       params: { dbname: this.$route.params.search },
      //     })
      //     .then((data) => {
      //       // this.lists = data.data.results;
      //       console.log(this.lists);
      //     })
      //     .catch((error) => {
      //       console.log(err);
      //     });
      // },
    },
    // mounted() {
    //   this.dosearch();
    //   setTimeout(() => {
    //     this.loading = false;
    //   }, 90);
    // },
  },
};
</script>

<style scoped>
.detailsearch {
  height: 70px;
  background-color: #f1f1f1;
  padding: 0px 10px 0px 10px;
}
.position {
  height: 20px;
  background-color: #f1f1f1;
}
.logo1 {
  text-align: right;
}
.inline-input {
  width: 100%;
}
/deep/.el-button {
  background-color: #102785;
  border-color: #102785;
}
.box1 {
  text-align: right;
}
.box2 {
  text-align: left;
}
</style>