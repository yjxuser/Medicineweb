<template>
  <div>
    <el-container>
      <el-header class="el-header" style="height: 260px">
        <div class="signin">
          <div class="signinbutton">
            <a href="#" class="footerwriter">sign in</a>
          </div>
          <div class="signinbutton1">
            <a href="#" class="footerwriter">sign up</a>
          </div>
        </div>
        <img src="../assets/logo.png" />
        <!-- 水平的导航栏菜单，有六个分类 -->

        <el-menu
          class="el-menu-demo"
          mode="horizontal"
          background-color="#fff"
          text-color="#606266"
          active-text-color="#ffd04b"
        >
          <!-- 菜单颜色自行修改 -->
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
            <router-link :to="'/download/'">
              Download
            </router-link></el-menu-item
          >
          <el-menu-item class="el-menu-item" index="5" style="font-size: 20px">
            <router-link :to="'/contact/'">
              Contact us
            </router-link></el-menu-item
          >
        </el-menu>
        <!-- 去官网看看怎么选择，，index的使用方法，还有其他种类的，自行更改吧 -->
      </el-header>

      <!-- <img src="../assets/9.png" /> -->
      <!-- <el-row :gutter="20">
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
      </el-row> -->
      <!-- <Homesearchbar /> -->
      <el-main class="el-main" style="height: 700px">
        <!-- 这里是搜索框和按钮，有一些用法，链接留给你了，可以自行删改，指路
        https://blog.csdn.net/qq_42268364/article/details/97375138?utm_term=elementui%E6%90%9C%E7%B4%A2%E6%A1%86&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-5-97375138&spm=3001.4430
         -->

        <!-- introduction -->
        <!-- <el-row :gutter="10">
          <el-col :span="6"
            ><div class="classify"><img src="../assets/brain.png" /></div
          ></el-col>
          <el-col :span="6"
            ><div class="classify"><img src="../assets/heart.png" /></div
          ></el-col>
          <el-col :span="6"
            ><div class="classify"><img src="../assets/virus.png" /></div
          ></el-col>
          <el-col :span="6"
            ><div class="classify"><img src="../assets/dna.png" /></div
          ></el-col>
        </el-row> -->
        <br />
        <div class="searchposition"><Homesearchbar /></div>
        <br />
        <el-row :gutter="10">
          <el-col :span="6"
            ><div class="classify"><img src="../assets/brain.png" /></div
          ></el-col>
          <el-col :span="6"
            ><div class="classify"><img src="../assets/heart.png" /></div
          ></el-col>
          <el-col :span="6"
            ><div class="classify"><img src="../assets/virus.png" /></div
          ></el-col>
          <el-col :span="6"
            ><div class="classify"><img src="../assets/dna.png" /></div
          ></el-col>
        </el-row>
        <div class="introduction">
          <span>Introduction</span>
          <el-divider></el-divider>
          <div class="content">
            For the first time, the concept of database portal management in the
            field of biomedicine is proposed,
          </div>
          <div class="content">
            which realizes multi-source integration of database resources and
            cross-database retrieval,
          </div>
          <div class="content">
            and builds classification catalogs of various databases and hot data
            resource portals,
          </div>
          <div class="content">
            which greatly improves the efficiency of scientific researchers when
            searching databases.
          </div>
        </div>
      </el-main>

      <el-footer class="el-footer" style="height: 200px">
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
      </el-footer>
    </el-container>
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
.el-header {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  /* line-height: 300px; */
  /* background: url(../assets/sky2.jpg); */
  /* background-image: url(../assets/sky2.jpg); */
  background-color: #3e52b5;
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
  background-color: #fff;
}
.el-menu-item {
  width: 20%;
}
.el-menu-demo {
  margin-left: -20px;
  margin-right: -20px;
}

.signin {
  height: 60px;
}

.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
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
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.footerpadding {
  padding: 15px;
}

.signinbutton {
  margin-top: 10px;
  margin-right: -10px;
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
/deep/.el-button {
  background-color: #102785;
  border-color: #102785;
}

.introduction {
  margin-top: 5%;
  font-size: 30px;
  font-weight: 600;
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
.searchposition {
  height: 20%;
}
.classify {
  height: 5%;
}
</style>
