<template>
    <div id="comments">
        <v-layout row wrap class="mb-4">
            <v-textarea ref="commentInput" outline class="commentInput pt-0 mx-0 " color="primary" background-color="gery" height="100"
                placeholder="أضف تعليق" v-model="Content">

            </v-textarea>
            <v-btn larg class="prymary_Gradient_Btn elevation-14 mt-0 mx-0" color="success" @click="onAddComment">إرسال
            </v-btn>
        </v-layout>
        <v-layout column height="400">
            <div class="commentPanel">
                <v-card class="commentCard my-2" v-for="comment in Comments" :key="comment.ID" :class="{'mr-3' : comment.isRepaly }" max-width="500" flat>
                    <v-card-title primary-title class="pa-2">
                        <v-layout row align-center>
                            <v-avatar size="32" color="red">
                                <img src="../../assets/img/avatar.png" alt="alt">
                            </v-avatar>
                            <span class="font-weight-bold mx-2">زيد اسامه</span>
                            <v-spacer></v-spacer>
                            <span class="caption">منذ ثانيه واحده</span>
                        </v-layout>
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text class="text-xs-right">
                        {{ comment.Content }}
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions class="pa-0">
                        <v-layout row class="px-0">
                            <!-- <v-spacer></v-spacer> -->
                            <v-btn flat small fab color="grey">
                                <v-icon small>fas fa-heart</v-icon>
                            </v-btn>
                            <v-spacer></v-spacer>
                            <v-btn flat small fab color="grey" @click="Replay">
                                <v-icon small>fas fa-reply</v-icon>
                            </v-btn>
                        </v-layout>
                    </v-card-actions>
                </v-card>
            </div>
        </v-layout>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                ID: '',
                Author: {
                    name:'',
                    avatar:''
                },
                isRepaly: false,
                Content: '',
                Hearts: '',
                Date: '',
            }
        },
        computed:{
            Comments(){
                return this.$store.getters.comments
            }
        },
        methods: {
            onAddComment: function () {
                
                let comment = {
                    ID: this.ID,
                    Author: this.Author,
                    isRepaly: this.isRepaly,
                    Content: this.Content,
                    Hearts: this.Hearts,
                    Date: '',
                }
                this.$store.commit('addComment',comment)
            },

            Replay: function(){
                this.isRepaly = true
                this.$refs.commentInput.focus({preventScroll: false})
            }
        }
    }
</script>
<style lang="scss" scoped>
    @import '../../styles/components/comments/comments';
</style>