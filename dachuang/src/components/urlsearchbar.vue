<template>
  <div class="homesearchposition">
    <div class="logo">
      <img src="../assets/BDP.png" />
    </div>
</br>
    <div class="searchposition">
      <el-row :gutter="20">
  <el-col :span="17"><div class="box1"><el-autocomplete
        class="inline-input"
        placeholder="Please enter the keyword you want to search"
        @keyup.enter.native="search"
        v-model="searchtext"
      ></el-autocomplete></div></el-col>
  <el-col :span="6"><div class="box2"><el-button
        type="primary"
        icon="el-icon-search "
        @click="search"
        @mouseover="mouseOver($event)"
        @mouseleave="mouseLeave($event)"
        >Search</el-button
      ></div></el-col>
</el-row>
      
      <!-- <el-autocomplete
        class="inline-input"
        placeholder="Please enter the keyword you want to search"
        @keyup.enter.native="search"
        v-model="searchtext"
      ></el-autocomplete>

      <el-button
        type="primary"
        icon="el-icon-search "
        @click="search"
        @mouseover="mouseOver($event)"
        @mouseleave="mouseLeave($event)"
        >Search</el-button
      > -->
    </div>
</div>
</template>

<script>
import URL from "@/common/URL";
export default {
  name: "urlsearchbar",
  data() {
    //  搜索框
    return {
      diseaseList: [], //这个值是需要匹配的值
      disease: "", //这个值是用户正在输入的值
      searchtext: "",
    };
  },

  methods: {
    search() {
      URL.searchAPI(this.$router, this.searchtext);
    },
    mouseOver($event) {
      $event.currentTarget.className = "button active";
    },
    mouseLeave($event) {
      $event.currentTarget.className = "button";
    },

    // getdata() {
    //   this.$http
    //     .get("/api/db/search?dbname")
    //     .then((res) => {
    //       console.log(res);
    //     })
    //     .catch((error) => {
    //       console.log(err);
    //     });
    // },
  },
  // mounted() {
  //   this.getdata();
  //   setTimeout(() => {
  //     this.loading = false;
  //   }, 90);
  // },
};
</script>

<style scoped>
.logo {
  /* margin-top: 5%; */
  /* height: 50px; */
  float: left;
  margin-left: 21%;
}
.inline-input {
  width: 70%;
}
.searchposition {
  /* 搜索框和按钮的div */
  margin-top: 3%;
  /* height: 60px; */
  text-align: center;
}
/deep/.el-button {
  background-color: #102785;
  border-color: #102785;
}
.button {
  background-color: #102785;
  border-color: #102785;
}
.active {
  background-color: cornflowerblue;
  border-color: cornflowerblue;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.bg-purple {
  background: #d3dce6;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.box1 {
  text-align: right;
}
.box2 {
  text-align: left;
}
.homesearchposition {
  padding: 0px 10px 0px 10px;
  height: 110px;
}
</style>