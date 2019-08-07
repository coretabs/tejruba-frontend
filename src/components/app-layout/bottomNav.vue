<template>
         <v-bottom-nav       
      color="primary"
      active.sync="bottomNav"
      :value="true"
      dark
      fixed
      shift 
    >
      <v-btn dark  router to="/">
        <span>الرئيسيه</span>
        <v-icon>fas fa-flask</v-icon>
      </v-btn>

      <v-btn dark  router to="/editor">
        <span>كتابه</span>
        <v-icon>fas fa-feather</v-icon>
      </v-btn>

      <v-btn dark  router to="/profile">
        <span>البروفايل</span>
        <v-icon>fas fa-user</v-icon>
      </v-btn>

      <v-btn dark class="caption" router to="/settings">
        <span>الإعدادات</span>
        <v-icon>fas fa-cog</v-icon>
      </v-btn>
    </v-bottom-nav>
</template>

<script>
export default {
  data(){
    return{
      bottomNav: 'home'
    }
  }

}
</script>

<style>

</style>
