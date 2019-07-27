<template>
  <v-container fluid class="pa-2">
    
    <v-btn color="lightgreen" router to="/editor">editor</v-btn>
        <v-card>
            <div>lo</div>
        </v-card>
        <v-card>
            <div ref="contentViewer">lo</div>
        </v-card>
    </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import Quill from 'quill'
export default {
    data(){
        return{
            content:''
        }
    },
    computed:{
        ...mapGetters(['delta'])
    },
    mounted(){
        let article = document.createElement('article')
        let quill = new Quill(article , {})
        quill.setContents(this.delta)
        setTimeout(()=>{ this.$refs.contentViewer.appendChild(article) },0)
    }

}
</script>

<style>

</style>
