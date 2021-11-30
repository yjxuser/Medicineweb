<template>
  <div class="box">
    <el-container>
      <!-- <el-header class="el-header" style="height: 180px">
        <div class="signin">
          <div class="signinbutton">
            <a href="#" class="footerwriter">sign in</a>
          </div>
          <div class="signinbutton1">
            <a href="#" class="footerwriter">sign up</a>
          </div>
        </div>
        <img class="img1" src="../assets/logo.png" />
      </el-header> -->
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

      <searchbar :search="search" />

      <el-container>
        <el-aside width="800px" style="height: 1100px" class="el-main">
          <div class="databasename">{{ this.$route.params.DBName }}</div>
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>Introduction</span>
            </div>
            <div v-for="(i, index) in lists" :key="index">
              <div class="databaseintroduction">{{ i.Introduction }}</div>
            </div>
          </el-card>
          <div class="white"></div>
          <el-card>
            <div slot="header" class="clearfix">
              <span>Main Literature</span>
            </div>
            <div class="text item">
              <div v-for="(i, index) in articles" :key="index">
                <div
                  class="articletitle"
                  @click="databasearticle(i.DOI)"
                  @mouseover="mouseOver($event)"
                  @mouseleave="mouseLeave($event)"
                >
                  <el-checkbox
                    v-model="checked"
                    style="margin-right: 2px"
                  ></el-checkbox>
                  {{ i.Title }}
                </div>
                <div class="articlewriter">
                  <i
                    style="
                      margin-right: 7px;
                      font-family: monospace;
                      font-weight: 500;
                    "
                    >{{ index + 1 }}</i
                  >
                  {{ i.Authors }}
                </div>
                <!-- <a href="#" class="download"
                  ><i class="el-icon-download"></i
                ></a> -->
                <!-- <div class="el-icon-download"></div> -->
                <!-- <el-row>
                  <el-col :span="24"> -->
                <div class="articleabstract">
                  <!-- <i>{{ index + 1 }}</i> -->
                  {{ i.Abstract }}
                </div>
                <!-- </el-col>
                </el-row> -->
                <div class="articleid">
                  {{ i.PM_ID }}
                </div>
                <div class="articledate">
                  <i style="font-size: 20px" class="el-icon-download"></i>
                  {{ i.date }}
                </div>
                <!-- </div> -->
              </div>
            </div>
          </el-card>
        </el-aside>
        <el-main class="aside" style="height: 1100px">
          <!-- <div v-for="(i, index) in lists" :key="index">
            <div>
              <div>Native Web Links</div>

              <div class="newdatabaseurl" @click="newdatabase()">
                <div class="a">
                  <el-button round type="primary"
                    ><i style="font-size: 25px" class="el-icon-position"></i
                  ></el-button>
                </div>
              </div>
            </div>
            <br />
            <div>
              <br />
              <br />
              <div class="newbaseurl">Relative Web Links</div>
              <div class="b">
                <el-button round type="warning" @click="MalaCardsdatabase()"
                  ><i style="font-size: 25px">MalaCards</i></el-button
                >
                <el-button round type="danger " @click="GeneCardsdatabase()"
                  ><i style="font-size: 25px">GeneCards</i></el-button
                >
              </div>
            </div>
          </div> -->

          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="用户管理" name="first">123</el-tab-pane>
            <el-tab-pane label="配置管理" name="second">456</el-tab-pane>
          </el-tabs>

          <!-- {{ i.DBUrl }} -->

          <!-- <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>Introduction</span>
            </div>
            <span>这里是网站的简介</span>
          </el-card>
          <div class="white"></div>
          <el-card>
            <div slot="header" class="clearfix">
              <span>主要文献</span>
            </div>
            <div v-for="o in 10" :key="o" class="text item">
              {{ "列表内容 " + o }}
            </div>
          </el-card> -->
        </el-main>
      </el-container>

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

<script scoped>
import searchbar from "@/components/searchbar.vue";
export default {
  name: "websitedetails",

  data() {
    //  搜索框
    return {
      searchtext: "",
      lists: [],
      params: "",
      articles: [],
      checked: false,
      activeName: "second",
    };
  },

  methods: {
    search() {
      Util.searchAPI(this.$router, this.searchtext);
    },
    getdata() {
      // const { DBName } = this.$route.params;
      this.$http
        .get("/api/db/search", {
          params: { dbname: this.$route.params.DBName },
        })
        .then((data) => {
          this.lists = data.data.results;
          // console.log(this.lists);
        })
        .catch((error) => {
          console.log(err);
        });
    },
    getmoredata() {
      // const { DBName } = this.$route.params;
      this.$http
        .get("/api/papers/db", {
          params: { name: this.$route.params.DBName },
        })
        .then((data) => {
          this.articles = data.data.results;
          // console.log(this.articles);
        })
        .catch((error) => {
          console.log(err);
        });
    },
    handleClick(tab, event) {
      console.log(tab, event);
    },
    newdatabase() {
      window.location.assign(this.lists[0].DBUrl);
      // console.log(this.lists[0].DBUrl);
    },
    databasearticle(url) {
      window.location.assign(url);
    },
    MalaCardsdatabase() {
      window.location.assign("https://www.malacards.org/");
    },
    GeneCardsdatabase() {
      window.location.assign("http://www.genecards.org/");
    },
    mouseOver($event) {
      $event.currentTarget.className = "articletitle active";
    },
    mouseLeave($event) {
      $event.currentTarget.className = "articletitle";
    },
  },
  created() {
    this.getdata();
    this.getmoredata();
    setTimeout(() => {
      this.loading = false;
    }, 90);
  },
  components: {
    searchbar,
  },

  computed: {
    search() {
      return this.$route.params.searchtext;
    },
  },
};
</script>

<style scoped>
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
  background-color: #fff;
  color: #333;
  text-align: center;
  margin-left: 100px;
  /* line-height: 600px; */
}

.clearfix {
  font-size: 22px;
}
.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
.white {
  padding: 40px;
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
.img1 {
  margin-top: 30px;
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
.detailsearch {
  height: 70px;
  background-color: #f1f1f1;
}

.searchlogo {
  float: left;
  padding-left: 12%;
  padding-right: 5%;
}
.inline-input {
  width: 50%;
}
.url {
  text-decoration: none;
}
.aside {
  font-size: 20px;
  margin-left: 35px;
  font-weight: 500;
  text-align: left;
}
.databasename {
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 30px;
}
.articletitle {
  text-decoration: none;
  text-align: left;
  font-size: 20px;
  color: #0071bc;
}
.active {
  color: #99a9bf;
}
.articleid {
  font-size: 15px;
  text-align: left;
  margin-left: 25px;
}
.articledate {
  font-size: 15px;
  margin-bottom: 15px;
  text-align: left;
}

.articleabstract {
  font-size: 15px;
  width: 100%; /*一定要设置宽度，或者元素内含的百分比*/
  overflow: hidden; /*溢出的部分隐藏*/
  white-space: nowrap; /*文本不换行*/
  text-overflow: ellipsis; /*ellipsis:文本溢出显示省略号（...）；clip：不显示省略标记（...），而是简单的裁切*/
  text-align: left;
  text-decoration: none;
  margin-left: 25px;
}
.articlewriter {
  font-size: 15px;
  width: 100%; /*一定要设置宽度，或者元素内含的百分比*/
  overflow: hidden; /*溢出的部分隐藏*/
  white-space: nowrap; /*文本不换行*/
  text-overflow: ellipsis; /*ellipsis:文本溢出显示省略号（...）；clip：不显示省略标记（...），而是简单的裁切*/
  text-align: left;
  text-decoration: none;
  font-weight: 600;
}
.databaseintroduction {
  font-size: 20px;
  text-align: left;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
.newdatabaseurl {
  float: left;
  text-align: center;
  display: block;
  font-size: 25px;
  font-family: monospace;
}
.download {
  float: left;
}
.a {
  margin-top: 10px;
}
.b {
  margin-top: 10px;
}
/deep/.el-tabs__item {
  font-size: 20px;
}
</style>