import Vue from "vue";
import Vuex from "vuex";
import actions from './actions'
import mutations from './mutations'
import getters from './getters'
Vue.use(Vuex);

export default new Vuex.Store({
  state: {    // header 
    currentPage: '',
    experienceFilterValue:'',
    delta: undefined,
    content: '',
    FilterdExperiences: [],
    altjarub: [],
    snackbar:{
      trigger : false,
      message : '',
      color: ''
    },
  },

  getters,
  mutations,
  actions,
});