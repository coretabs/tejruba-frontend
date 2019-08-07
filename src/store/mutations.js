//mutations
export default {
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
}