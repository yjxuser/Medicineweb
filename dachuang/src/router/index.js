import Vue from 'vue'
import Router from 'vue-router'


import search from '@/components/search'
import websitedetails from '@/components/websitedetails'
import result from '@/components/result'
import databasesearch from '@/components/databasesearch'
import urlsearch from '@/components/urlsearch'
import papersearch from '@/components/papersearch'
import download from '@/components/download'
import contact from '@/components/contact'
import help from '@/components/help'
import services from '@/components/services'
import support from '@/components/support'
import about from '@/components/about'
import urlresult from '@/components/urlresult'
import paperresult from '@/components/paperresult'






Vue.use(Router)

//const router = new VueRouter({})

export default new Router({
  routes: [

    {
      path: '/',
      name: 'search',
      component: search
    },

    {
      path: '/websitedetails/:DBName',
      name: 'websitedetails',
      component: websitedetails
    },

    {
      path: '/result/:searchtext',
      name: 'result',
      component: result
    },
    {
      path: '/urlresult/:searchtext',
      name: 'urlresult',
      component: urlresult
    },
    {
      path: '/paperresult/:searchtext',
      name: 'paperresult',
      component: paperresult
    },
    {
      path: '/databasesearch/',
      name: 'detabasesearch',
      component: databasesearch
    },

    {
      path: '/urlsearch/',
      name: 'urlsearch',
      component: urlsearch
    },
    {
      path: '/papersearch/',
      name: 'papersearch',
      component: papersearch
    },
    {
      path: '/contact/',
      name: 'contact',
      component: contact
    },
    {
      path: '/download/',
      name: 'download',
      component: download
    },
    {
      path: '/help/',
      name: 'help',
      component: help
    },
    {
      path: '/about/',
      name: 'about',
      component: about
    },
    {
      path: '/services/',
      name: 'services',
      component: services
    },
    {
      path: '/support/',
      name: 'support',
      component: support
    },


  ],
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 }
  }



})
// // ????????????????????????????????????
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth == true) {
//     // ????????? ????????????
//     // token
//     if (window.localStorage.getItem('token') != undefined) {
//       // ???????????????
//       next()
//     } else {
//       // new??????????????????
//       new Vue().$message.error('??????????????????')
//       // ?????????
//       router.push('/login')
//     }
//   } else {
//     // ?????????
//     next()
//   }
// })
