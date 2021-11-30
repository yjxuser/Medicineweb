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
      <div class="webname">Biomedicine Database Portal</div>
      <br />
      <div class="textcontent">
        For the first time, the concept of database portal management in the
        field of biomedicine is proposed, which realizes multi-source
        integration of database resources and cross-database retrieval,and
        builds classification catalogs of various databases and hot data
        resource portals, which greatly improves the efficiency of scientific
        researchers when searching databases.
      </div>
      <br />
      <div class="webname">About us</div>
      <br />
      <div class="textcontent">
        We are an undergraduate development team from Beijing Jiaotong
        University. We rely on the biomedical engineering laboratory and
        cognitive computing and machine learning laboratory of Beijing Jiaotong
        University for development. Our project is to propose an example
        database portal for the difficulties in biomedical data search and the
        lack of integration of biomedical databases in today's big data era, In
        order to facilitate medical workers to retrieve information.
      </div>
      <br />
      <div class="webname">Search in BDP</div>
      <br />
      <div class="textcontent">
        In our portal website, you can search the databases related to medicine,
        and our website can also link the databases related to the data you
        search, which can better help you with retrieval services. In addition,
        our portal also provides URL search and paper search services, which can
        meet your relevant requirements for medical data retrieval to a greater
        extent.
      </div>
      <br />
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

<script scoped>
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
/* .left {
  flex-basis: auto;
  white-space: nowrap;
  background: #fff;
}
.right {
  width: 100%;
  background: #fff;
  padding: 0% 0% 2% 3%;
}
.address {
  height: 30%;
  font-size: 20px;
  text-align: left;
  padding: 15px;

  border-left: 1px solid #797979;
  border-right: 1px solid #797979;
}
.color {
  padding: 2% 0% 2% 4%;
  height: 8%;
  font-size: 25px;
  background-color: #f1f1f1;
  text-align: left;
  font-weight: 540;
  border: 1px solid #797979;
}
.contactus {
  height: 40%;
  font-size: 20px;
  text-align: left;
  padding: 15px;

  border-left: 1px solid #797979;
  border-right: 1px solid #797979;
  border-bottom: 1px solid #797979;
}
.mapcolor {
  padding: 1% 0% 2% 3%;
  height: 5%;
  font-size: 25px;
  background-color: #f1f1f1;
  text-align: left;
  font-weight: 540;
  border: 1px solid #797979;
}
.map {
  height: 85%;
  font-size: 20px;
  text-align: left;
  padding: 15px;
  border-left: 1px solid #797979;
  border-right: 1px solid #797979;
  border-bottom: 1px solid #797979;
} */
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
.webname {
  color: #3e52b5;
  font-size: 28px;
  text-align: left;
}
.textcontent {
  font-size: 20px;
  text-align: left;
}
</style>