//mutations
export default {
    setDelta(state, payload) {
      state.delta = payload;
    },

    setContent(state, payload) {
      state.content = payload;
    },
    
    publishPost(state ,payload){
      state.altjarub.push({...payload});
    },

    updateSnackbar(state, payload) {
      state.snackbar.trigger = true
      state.snackbar.message = payload.message
      state.snackbar.color = payload.color
    },
}