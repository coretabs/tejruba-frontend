import Vue from "vue";
import Vuex from "vuex";

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
      postImg: '',
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

  mutations: {
    setDelta(state, payload) {
      state.delta = payload;
    },
    setPostDelta(state, payload) {
      state.editorData.postDelta = payload;
    },
    setContent(state, payload) {
      state.content = payload;
    },
//-- edtor mutation 
    setPostTitle(state, payload) {
      state.editorData.postTitle = payload;
    },  
    setPostCategory(state, payload) {
      state.editorData.postCategory = payload;
    },
    setPostContent(state) {
      state.editorData.postContent = state.delta;
    },
  },

  getters: {
    delta: state => state.delta,
    contents: state => state.content,
    editorData: state => state.editorData,
    altejarub: state => state.alejarub,
  },
  actions: {}
});