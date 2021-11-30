<template>
  <div class="box">
    <!-- <el-container> -->
    <!-- <el-header class="el-header" style="height: 180px"> -->
    <div class="header">
      <div class="signin">
        <div class="signinbutton">
          <a href="#" class="footerwriter">sign in</a>
        </div>
        <div class="signinbutton1">
          <a href="#" class="footerwriter">sign up</a>
        </div>
      </div>

      <img class="img1" src="../assets/logo.png" />
      <!-- </el-header> -->
    </div>
    <searchbar :search="searchcontent" />
    <div class="main">
      <!-- <el-main class="el-main"> -->
      <div class="listpadding">
        <div v-for="(i, index) in lists" :key="index">
          <router-link :to="'/websitedetails/' + i.DBName">
            <div
              class="information-title"
              @mouseover="mouseOver($event)"
              @mouseleave="mouseLeave($event)"
            >
              {{ i.DBName }}
            </div>
          </router-link>

          <div class="information-writer">
            {{ i.Introduction }}
          </div>

          <div class="information-summary">
            {{ i.date }}
          </div>
        </div>
      </div>
      <!-- </el-main> -->
    </div>
    <div class="footer">
      <!-- <el-footer class="el-footer" style="height: 200px"> -->
      <div class="footerpadding"></div>
      <el-row :gutter="20">
        <el-col :span="8"
          ><div class="grid-content bg-purple">
            <router-link :to="'/contact/'" class="footerwriter">
              Follow us
            </router-link>
          </div></el-col
        >
        <el-col :span="8"
          ><div class="grid-content bg-purple">
            <router-link :to="'/services/'" class="footerwriter">
              Services
            </router-link>
          </div></el-col
        >
        <el-col :span="8"
          ><div class="grid-content bg-purple">
            <router-link :to="'/support/'" class="footerwriter">
              Support
            </router-link>
          </div></el-col
        >
      </el-row>
      <el-row :gutter="20">
        <el-col :span="8"
          ><div class="picture">
            <a href="#" class="footerwriter"
              ><i class="el-icon-phone-outline"></i
            ></a>
            <a href="#" class="footerwriter"
              ><i class="el-icon-chat-dot-round"></i
            ></a>
            <a href="#" class="footerwriter"
              ><i class="el-icon-share"></i
            ></a></div
        ></el-col>
        <el-col :span="8"
          ><div class="grid-content bg-purple">
            <router-link :to="'/about/'" class="footerwriter">
              About
            </router-link>
          </div></el-col
        >

        <el-col :span="8"
          ><div class="grid-content bg-purple">
            <router-link :to="'/help/'" class="footerwriter">
              Help
            </router-link>
          </div></el-col
        >
      </el-row>
      <el-divider><a href="#" class="fenge">BioDataPortal.com</a></el-divider>
      <div class="banquan">&copy;版权所有BJTU</div>
      <!-- </el-footer > -->
    </div>
    <!-- </el-container> -->
  </div>
</template>
<script>
import searchbar from "@/components/searchbar.vue";

export default {
  name: "result",

  data() {
    //  搜索框
    return {
      lists: [],
      params: "",
    };
  },

  methods: {
    getdata() {
      const { searchtext } = this.$route.params;
      this.$http
        .get("/api/db/search", {
          params: { dbname: searchtext },
        })
        .then((data) => {
          this.lists = data.data.results;
          // console.log(this.lists);
        })
        .catch((error) => {
          console.log(err);
        });
    },
    mouseOver($event) {
      $event.currentTarget.className = "information-title active";
    },
    mouseLeave($event) {
      $event.currentTarget.className = "information-title";
    },
  },
  created() {
    this.getdata();
    setTimeout(() => {
      this.loading = false;
    }, 90);
  },
  beforeRouteUpdate(to, from, next) {
    next();
    this.getdata();
  },
  components: {
    searchbar,
  },
  computed: {
    searchcontent() {
      return this.$route.params.searchtext;
    },
  },
};
</script>

<style scoped>
.box {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  text-align: center;
  /* overflow-x: hidden; */
}
.main {
  flex: 1;
  color: #333;
  text-align: center;
  /* line-height: 600px; */
  padding: 20px 300px 20px 300px;
  background-color: #fff;
}
.header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  /* line-height: 300px; */
  background-color: #3e52b5;
  /* background: url(../assets/sky2.jpg);
  background-image: url(../assets/sky2.jpg); */
  background-position-x: center;
  background-position-y: center;
  background-size: cover;
  background-attachment: initial;
  background-origin: initial;
  background-clip: initial;
  height: 180px;
}
.footer {
  height: 200px;
  padding: 0px 10px 0px 10px;
  background-color: #3e52b5;
  color: #fff;
  text-align: center;
}
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  /* line-height: 300px; */
  background-color: #3e52b5;
  /* background: url(../assets/sky2.jpg);
  background-image: url(../assets/sky2.jpg); */
  background-position-x: center;
  background-position-y: center;
  background-size: cover;
  background-attachment: initial;
  background-origin: initial;
  background-clip: initial;
}
.el-footer {
  background-color: #3e52b5;
  color: #fff;
  text-align: center;
  /* line-height: 200px; */
  /* footer的高度不能在这设置，header同理 */
}

.el-main {
  color: #333;
  text-align: center;
  /* line-height: 600px; */
  padding: 20px 300px 20px 300px;
  background-color: #fff;
}

.listpadding {
  padding: 40px;
}
.item {
  margin-bottom: 20px;
}
.img1 {
  margin-top: 30px;
}

.information-title {
  font-size: 23px;
  width: 100%; /*一定要设置宽度，或者元素内含的百分比*/
  overflow: hidden; /*溢出的部分隐藏*/
  white-space: nowrap; /*文本不换行*/
  text-overflow: ellipsis; /*ellipsis:文本溢出显示省略号（...）；clip：不显示省略标记（...），而是简单的裁切*/
  text-align: left;
  color: #0071bc;
  text-decoration: none;
}
.active {
  color: #99a9bf;
}
.information-writer {
  font-size: 20px;
  width: 100%; /*一定要设置宽度，或者元素内含的百分比*/
  overflow: hidden; /*溢出的部分隐藏*/
  white-space: nowrap; /*文本不换行*/
  text-overflow: ellipsis; /*ellipsis:文本溢出显示省略号（...）；clip：不显示省略标记（...），而是简单的裁切*/
  text-align: left;
  color: #212121;
}
.information-summary {
  font-size: 16px;
  width: 100%; /*一定要设置宽度，或者元素内含的百分比*/
  overflow: hidden; /*溢出的部分隐藏*/
  white-space: nowrap; /*文本不换行*/
  text-overflow: ellipsis; /*ellipsis:文本溢出显示省略号（...）；clip：不显示省略标记（...），而是简单的裁切*/
  text-align: left;
  color: #4d8055;
  margin-bottom: 20px;
}
.inline-input {
  width: 50%;
}

/deep/.el-button {
  background-color: #102785;
  border-color: #102785;
}
.detailsearch {
  height: 70px;
  background-color: #f1f1f1;
}
.position {
  height: 20px;
  background-color: #f1f1f1;
}
.searchlogo {
  float: left;
  padding-left: 12%;
  padding-right: 5%;
}
.signinbutton {
  margin-top: 10px;
  margin-right: 10px;
  float: right;
  padding: 10px 10px;
  color: #f9fafc;
  font-size: 20px;
  border: 1px solid rgba(255, 255, 255, 0.5);
}
.signinbutton1 {
  margin-top: 10px;
  margin-right: 10px;
  float: right;
  padding: 10px 10px;
  color: #f9fafc;
  font-size: 20px;
  border: 1px solid rgba(255, 255, 255, 0.5);
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  color: #fff;
  font-size: 19px;
}
.footerpadding {
  padding: 15px;
}
.footerwriter {
  color: #fff;
  text-decoration: none;
}
.fenge {
  text-decoration: none;
}
.banquan {
  text-align: center;
}
.picture {
  border-radius: 4px;
  font-size: 30px;
}
.url {
  text-decoration: none;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
</style>