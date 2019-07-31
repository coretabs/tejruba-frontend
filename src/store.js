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
       {
        postID:1,
        postImg: 'https://images.unsplash.com/photo-1558980394-4c7c9299fe96?ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80',
        postTitle: 'رحلتي الى سويسرا ',
        postCategory:'سياحه',
        //--
        postDelta: undefined,
        //--
        postDate: '',
        //--
        postHearts: '',
        postLikes: '',
        postStars: '',
      },
       {
        postID:2,
        postImg: 'https://images.unsplash.com/photo-1563714272638-882a6309ba7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
        postTitle: 'تجربتي مع رياضه الباركور',
        postCategory:'رياضه',
        //--
        postDelta: undefined,
        //--
        postDate: '',
        //--
        postHearts: '',
        postLikes: '',
        postStars: '',
      },
       {
        postID:3,
        postImg: '',
        postTitle: 'كيف تمكنت من التغلب على المرض',
        postCategory:'صحه',
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
      postID:'',
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
    altejarub: state => state.altjarub,
  },
  actions: {}
});