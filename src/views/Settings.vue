<template>

    <div>
        <h1>Settings</h1>
    </div>
</template>

<script>
    export default {
    mounted: function (){
      this.$store.state.currentPage = this.$route.name; 
      console.log(this.$store.state.currentPage)
  }
    }
</script>

<style>

</style>