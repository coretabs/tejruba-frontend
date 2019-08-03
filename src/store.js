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
       {
        postID:0,
        postImg: 'https://images.unsplash.com/photo-1563714272638-882a6309ba7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
        postTitle: 'كيف اصبحت مبرمج محترف',
        postCategory:'تعلم',
        //--
        postDelta: undefined,
        //--
        postDate: '',
        //--
        postHearts: '',
        postLikes: '',
        postStars: '',
      },
    ],

    editorData: {
      postID:10,
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
    setPostId(state) {
      state.editorData.postID = state.altjarub.length;
    },  
    setPostTitle(state, payload) {
      state.editorData.postTitle = payload;
    },  
    setPostCategory(state, payload) {
      state.editorData.postCategory = payload;
    },
    setPostContent(state) {
      state.editorData.postContent = state.delta;
    },


    //
    publishPost(state){
      state.altjarub.push(state.editorData);
    }
  },

  getters: {
    delta: state => state.delta,
    contents: state => state.content,
    editorData: state => state.editorData,
    altejarub: state => state.altjarub,
  },
  actions: {}
});