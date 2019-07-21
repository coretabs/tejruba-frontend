import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@fortawesome/fontawesome-free/css/all.css'

 Vue.use(Vuetify, {
  iconfont: 'fa',
  rtl: true,
  // #475bd0 , #4f98e8 , #19006c,#3f1ab8
  theme: {
    primary: '#273486',
    secondary: '#34c5e5',
    accent: '#475bd0',
    error: '#e91e4d',
    success:'#4caf50'
  },
})
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");