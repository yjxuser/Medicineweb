<template>
  <div class="box">
    <div class="header">
      <el-row :gutter="10">
        <el-col :span="8"
          ><div class="pic"><img src="../assets/littlelogo.png" /></div
        ></el-col>
        <el-col :span="10"
          ><div class="home">
            <router-link :to="'/'" class="footerwriter"> Home </router-link>
          </div></el-col
        >
      </el-row>
    </div>
    <div class="main">
      <div class="servicesname">Search</div>
      <br />
      <div class="textcontent">
        Our website provides search services, including database search, URL
        search and paper related information search, and we can also link to the
        database related to your search information, which can provide one-stop
        services for your search information.
      </div>
      <br />
      <div class="servicesname">Download</div>
      <br />
      <div class="textcontent">
        Our website provides download service. If you have papers you want to
        download, we will provide you with links, which can save time for your
        search and download to a greater extent.
      </div>
      <br />
      <div class="servicesname">User Submission</div>
      <br />
      <div class="textcontent">
        Our website also has user login and registration functions. You can
        register as a member of our website, and we will provide you with better
        services. In addition, if you find that there are errors or missing
        information in our website, you are also welcome to give us feedback,
        and we will revise our website and add relevant information according to
        your opinions.
      </div>
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
import searchbar from "./searchbar.vue";
export default {
  components: { searchbar },
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
  padding: 1% 10% 3% 10%;
}
.header {
  height: 80px;
  padding: 0px 20px 0px 20px;
  background-color: #3e52b5;
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
.item {
  padding: 6px;
}

.home {
  text-align: right;
  font-size: 25px;
  padding: 3% 0% 2% 3%;
  color: #fff;
}
.pic {
  text-align: right;
  padding: 2% 0% 0% 3%;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.servicesname {
  color: #3e52b5;
  font-size: 28px;
  text-align: left;
}
.textcontent {
  font-size: 20px;
  text-align: left;
}
</style>