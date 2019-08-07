import Vue from "vue";
import Vuex from "vuex";
import actions from './actions'
import mutations from './mutations'
import getters from './getters'
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // header 
    currentPage: '',

    // editor
    delta: undefined,
    content: '',

    // ------------------------

    altjarub:[
      
    ],

    editorData: {
      postID:10,
      postImg: 'https://images.unsplash.com/photo-1563714272638-882a6309ba7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
      postTitle: '',
      postCategory:'',
      //--
      postDelta: undefined,
      //--
      postDate: '',
      //--
      postHearts: '',
      postLikes: '',
      postStars: '',
    },
  },

  getters,
  mutations,
  actions,
});