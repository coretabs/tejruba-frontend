import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // header 
    currentPage:'',
  
    // editor
    delta: undefined,
    content:''
},
  mutations: {
    setDelta( state, payload){
      state.delta = payload;
    },
    setContent( state, payload){
      state.content = payload;
    }
  },

  getters:{
    delta : state => state.delta ,
    contents : state => state.content
  },
  actions: {}
});
