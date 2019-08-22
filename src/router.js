import Vue from "vue";
import Router from "vue-router";

import Home from "./views/home/Home.vue";

import Editor from "./views/editor/Post_editor.vue"

import singlePostPage from "./views/singlePostPage/singlePostPage.vue"


import Profile from "./views/profile/Profile.vue"
  import UserAbout from "./views/profile/profile-views/User-about.vue"
  import UserFav from "./views/profile/profile-views/User-favourite.vue"
  import UserPosts from "./views/profile/profile-views/User-posts.vue"
  import ProfileEdit from "./views/profile/profile-views/ProfileEdit.vue"

  import Settings from "./views/Settings.vue"

  // remove 
  import SignIn from "./views/signin/SignIn.vue"
  import SignUp from "./views/signup/SignUp.vue"
  import CatPicker from "./views/CategoriesPicker.vue"

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "الرئيسيه",
      component: Home
    },

    //remove --------
    {
      path: "/postPage/:id",
      name: "تجربه",
      component: singlePostPage
    },
    {
      path: "/signin",
      name: "دخول",
      component: SignIn
    },
    {
      path: "/signup",
      name: "تسجيل",
      component: SignUp
    },
    {
      path: "/categories",
      name: "اختر",
      component: CatPicker
    },
    //---------------
    {
      path: "/editor",
      name: "كتابه تجربه",
      component: Editor
    },
 
    {
      path: "/profile",
      name: "البروفايل",
      component: Profile,
      children:[
        {
          path: "/about",
          name: "about",
          component: UserAbout
        },
        {
          path: "/posts",
          name: "posts",
          component: UserPosts
        },
        {
          path: "/favourites",
          name: "favourites",
          component: UserFav
        },
     
      ]
    },
   
    { 
      path: "/EditProfile",
      name: "تعديل",
      component: ProfileEdit
    },
    {
      path: "/settings",
      name: "الاعدادات",
      component: Settings
    },
    
    // {
    //   path: "",
    //   name: "",
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "")
    // }
  ]
});
