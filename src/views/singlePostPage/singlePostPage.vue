<template>
    <div class="pb-4">
        <div class="postImg mb-2 ">
            <v-img :src="post.postImg" alt="user" aspect-ratio="1.4" height="200"></v-img>
            <div class="postCategory font-weight-bold mx-3">{{ post.postCategory }}</div>
        </div>
        <v-container fluid>

            <div class="postTitle text-xs-right my-3">
                <h1>{{ post.postTitle }}</h1>
            </div>

            <v-layout row align-center class="my-4">

                <v-flex shrink>
                    <v-avatar size="28" color="primary">
                        <img src="../../assets/img/avatar.png" alt="user">
                    </v-avatar>
                    <span class="gray--text font-weight-bold mx-2 body-1">زيد حسان</span>
                </v-flex>

                <v-spacer></v-spacer>

                <v-flex shrink>
                    <span>30-JULY</span>
                </v-flex>
            </v-layout>
            <div class="postContent text-xs-right my-4 body-1" >
              <p id="postViewer" ref="postViewer"></p>
            </div>


            <v-bottom-nav color="white" :value="true" dark fixed class="mb-5">
                <v-btn dark fab icon small flat color="accent lighten-3">
                    <v-icon class="accent--text">fas fa-thumbs-up</v-icon>
                </v-btn>


                <v-btn dark fab icon small flat color="error lighten-3">
                    <v-icon class="error--text">fas fa-heart</v-icon>
                </v-btn>

                <v-btn dark fab icon small flat color="yellow lighten-3">
                    <v-icon class="yellow--text darken-1">fas fa-bookmark</v-icon>
                </v-btn>
            </v-bottom-nav>
        </v-container>

    </div>
</template>

<script>
    import { mapGetters } from 'vuex'
    import Quill from 'quill'

    export default {
        data() {
            return {}
        },
        computed: {
        ...mapGetters(['delta','editorData']),

            post() {
                const id = parseInt(this.$route.params.id);
                return this.$store.state.altjarub.filter(function (tejrba) {
                    return tejrba.postID === id;
                })[0];
            }
        },

        mounted(){
        // let article = document.createElement('p')
        // let quill = new Quill(article , {})
        // quill.setContents(this.post.postDelta)
        // setTimeout(()=>{ this.$refs.postViewer.appendChild(article) },0)
        let article = this.$refs.postViewer
        let quill = new Quill(article , {readOnly:true})
        setTimeout(()=>{ 
        quill.setContents(this.post.postDelta)
        },0)
        // setTimeout(()=>{ this.$refs.postViewer.appendChild(article) },0)
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/views/singlePostPage/singlePostPage';
</style>