<template>
  <div class="home">

    <!-- <div class="gradient"></div> -->
    <div class="clipped-header hidden-md-and-up"></div>

    <categories-list />

    <v-container class="pt-0  mb-5">
      <v-layout column wrap>
        <v-flex ms12 class="my-3">
          <v-card class="elevation-20 article_card">
            <v-img src="https://images.unsplash.com/photo-1563714272638-882a6309ba7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" aspect-ratio="2.75">
              <v-layout justify-start>
                <v-avatar class="box-shadow pa-3 ma-2" size="40" color="gray">
                  <img class="elevation-15" src="../../assets/avatar.png" alt="alt">
                </v-avatar>
              </v-layout>
            </v-img>

            <v-card-title primary-title class="pb-0">
              <div>
                <h2 ma-0>كيف أصبحت طبيبا مطورا </h2>
              </div>
            </v-card-title>
            <v-card-text class="pt-2">
              <p class="post-text text-xs-right mb-0 body-2"> خمس اسطر تحتوي على نص مقصوصمن الاصلي الذي يتحدث فيه الكاتب عن
                هذا الموضوع حيث ينقل تجربته للعامه للاستفاده منها خمس اسطر تحتوي على نص مقصوصمن الاصلي الذي يتحدث فيه
                الكاتب عن هذا الموضوع </p>
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
      </v-layout>
    </v-container>
  </div>
</template>


<script>
  import categoriesList from "../../components/CategoriesList.vue"

  export default {
    name: "home",
    components: {
      categoriesList,
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