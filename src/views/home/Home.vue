<template>
  <div class="home">
    <!-- <div class="gradient"></div> -->
    <div class="clipped-header hidden-md-and-up"></div>

    <categories-list class="mb-2" />

    <v-container class="pt-0  mb-5">
      <div class="cardsHolder">
        <v-flex ms12  class="mt-1 mb-3" v-for="tejruba in FilterdExperiences"   :key="tejruba.postID">
          <v-card  class="elevation-20 article_card mt-0"
           router :to="`/postPage/${tejruba.postID}`">
            <v-img :src="tejruba.postImg" aspect-ratio="2.75">
              <v-layout justify-start>
                <v-avatar class="box-shadow pa-3 ma-2" size="40" color="gray">
                  <img class="elevation-15" src="../../assets/img/avatar.png" alt="alt">
                </v-avatar>
              </v-layout>
            </v-img>

            <v-card-title primary-title class="pb-0 text-xs-right">
              <div>
                <h2 class="" ma-0>{{ tejruba.postTitle }}</h2>
              </div>
            </v-card-title>
            <v-card-text class="pt-2">
              <p class=" text-xs-right mb-0 caption"> </p>
            </v-card-text>
            <v-divider></v-divider>
            <v-layout row align-center class="py-0">
              <v-flex class="text-xs-right caption">
                <span class="mx-3"><span>5</span> تعليقات</span>
                <span><span>4</span> الاعجاب</span>
              </v-flex>
              <v-spacer></v-spacer>
              <v-btn fab icon small flat color="primary" dark>
                <v-icon>fas fa-bookmark</v-icon>
              </v-btn>
            </v-layout>
          </v-card>
        </v-flex>
      </div>
    </v-container>
  </div>
</template>


<script>
  import categoriesList from "../../components/CategoriesList.vue"
import { mapGetters } from 'vuex'

  export default {
    name: "home",
    components: {
      categoriesList,
    },

    computed:{
        ...mapGetters(['altejarub']),
        FilterdExperiences(){
          if (this.$store.state.experienceFilterValue){
          return this.altejarub.filter((exp)=>{
            return exp.postCategory === this.$store.state.experienceFilterValue;
          })
          }else{
            return this.altejarub
          }
        }
    },

    methods: {
      test: function () {
        console.log(store)
      }
    },
   
    mounted: function () {
      this.$store.state.currentPage = this.$route.name;
      console.log(this.$store.state.currentPage);
      // console.log(this.$route.name); 
    }

  };
</script>

<style lang="scss" scoped>
  @import '../../styles/views/Home';
</style>