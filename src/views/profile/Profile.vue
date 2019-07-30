<template>
<!-- 
                  #تعديلات مهمه #
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
  [جعل الشادو الخاص بالهيدر يظهر رغم لوب الخلفيه الابيض] #  
-->
  <div class="profile white">
    <div  class=" userCard  elevation-6">
      <v-btn 
            small
            absolute 
            left="0" 
            router to="/EditProfile"
            fab
            color="white"  
            class="my-3 pt-2">
        <v-icon  color="primary">fas fa-pen</v-icon>
      </v-btn>
      
      <v-layout column justify-center align-center class="pt-4">
        <v-avatar class="elevation-10" size="95" color="gey">
          <img
            src="../../assets/avatar.png"
            alt="alt">
        </v-avatar>
        <div class="white--text mt-3">
          <h2 class="font-weight-light ">  حسان ثابت  </h2>
          <p class="font-weight-light caption">مطور مواقع</p>
        </div>
      </v-layout>

      <v-tabs fixed xs12 md6 justify-center v-model="model" grow 
      color="transparent" slider-color="white">
        <v-tab active ml-5 router to="/about"  class="white--text">
          <span>المزيد </span>
        </v-tab>
        <v-tab active ml-5 router to="/posts" class="white--text">
          <span>تجاربي</span>
        </v-tab>
        <v-tab active ml-5 router to="/favourites" class="white--text">
          <span>المفضله</span>
        </v-tab>
      </v-tabs>
    </div>
    <div class="block"></div>
    <v-container>
      <router-view />
    </v-container>
  </div>
</template>

<script>
  export default {
    mounted: function () {
      this.$store.state.currentPage = this.$route.name;
      console.log(this.$store.state.currentPage)
    }
  }
</script>

<style lang="scss" scoped>
 @import '../../styles/views/profile/profile';
</style>


