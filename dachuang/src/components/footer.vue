<template>
  <el-footer class="el-footer" style="height: 200px">
    <div class="footer"></div>
    <el-row :gutter="20">
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">Follow us</a>
        </div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">Services</a>
        </div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">Support</a>
        </div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">Accessibility</a>
        </div></el-col
      >
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6"
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
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">About</a>
        </div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">Careers</a>
        </div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <a href="#" class="footerwriter">Help</a>
        </div></el-col
      >
    </el-row>
    <el-divider><a href="#" class="fenge">BioDataPortal.com</a></el-divider>
    <div class="banquan">&copy;版权所有BJTU</div></el-footer
  >
</template>

<script>
export default {};
</script>

<style>
.el-footer {
  background-color: #3e52b5;
  color: #fff;
  text-align: center;
  /* line-height: 200px; */
  /* footer的高度不能在这设置，header同理 */
  flex: 0 0 auto;
}
.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;

  font-size: 19px;
}
.footer {
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