<template>
<!-- 
                  #تعديلات مهمه #
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
-->
  <div id="app">
    <v-app>
      <Header/>
      <v-content>
        <!-- <cat-picker/> -->
          <router-view/>
      </v-content>
      <bottom-nav/>
    </v-app>
  </div>
</template>

<script>
import bottomNav from './components/app-layout/bottomNav.vue'
import Header from './components/app-layout/Header.vue'
import catPicker from './views/CategoriesPicker.vue'
export default {
  components:{
    bottomNav,
    Header,
    catPicker
  }
  
}
</script>
<style lang="scss">
@import './styles/app';
</style>