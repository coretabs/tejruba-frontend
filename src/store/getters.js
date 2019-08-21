//getters
export default {
        delta: state => state.delta,
        contents: state => state.content,
        textContent: state => {
                var tag = document.createElement('div')
                tag.innerHTML = state.content
                return tag.innerText
        },
        editorData: state => state.editorData,
        altejarub: state => state.altjarub,
}