<template>
  <div class="box">
    <div class="header">
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#3e52b5"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <!-- 菜单颜色自行修改 -->
        <el-menu-item class="el-menu-item" index="5" style="font-size: 20px">
          <router-link :to="'/'"> Home </router-link></el-menu-item
        >
        <el-menu-item class="el-menu-item" index="1" style="font-size: 20px">
          <router-link :to="'/databasesearch/'">
            Database Search
          </router-link></el-menu-item
        >
        <el-menu-item class="el-menu-item" index="2" style="font-size: 20px">
          <router-link :to="'/urlsearch/'">
            BioSearch
          </router-link></el-menu-item
        >
        <el-menu-item class="el-menu-item" index="3" style="font-size: 20px">
          <router-link :to="'/papersearch/'">
            Paper Search
          </router-link></el-menu-item
        >
        <el-menu-item class="el-menu-item" index="4" style="font-size: 20px">
          <router-link :to="'/papersearch/'">
            Download
          </router-link></el-menu-item
        >
      </el-menu>
    </div>
    <div class="main">
      <div class="searchpic"><img src="../assets/DBsearch.png" /></div>
      <Homesearchbar />
      <!-- <div class="img">
        <img src="../assets/BDPsearch.png" />
      </div>
      <br />

      <el-autocomplete
        class="inline-input"
        placeholder="Please enter the keyword you want to search"
        @keyup.enter.native="dosearch"
        v-model="search"
      ></el-autocomplete>
      <el-button type="primary" icon="el-icon-search" @click="dosearch"
        >Search</el-button
      > -->
    </div>
    <div class="footer">
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
    </div>
  </div>
</template>

<script>
import Homesearchbar from "@/components/Homesearchbar.vue";
export default {
  name: "search",
  components: {
    Homesearchbar,
  },
};
</script>

<style scoped>
.box {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  text-align: center;
}
.main {
  flex: 1;
}
.header {
  height: 60px;
  padding: 0px 20px 0px 20px;
}
.footer {
  height: 200px;
  padding: 0px 10px 0px 10px;
  background-color: #3e52b5;
  color: #fff;
  text-align: center;
}
.img {
  margin-top: 6%;
}
.el-menu-item {
  width: 20%;
}
.el-menu-demo {
  margin-left: -20px;
  margin-right: -20px;
}

.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  color: #fff;
  font-size: 19px;
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
.content {
  font-size: 20px;
  margin-top: 10px;
}
a {
  text-decoration: none;
}
.router-link-active {
  text-decoration: none;
}
.footerpadding {
  padding: 15px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.inline-input {
  width: 50%;
}
.searchpic {
  margin-top: 5%;
  margin-bottom: 3%;
  text-align: center;
}
</style>