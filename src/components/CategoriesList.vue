<template>
  <div class="scrollableMenu mt-3 mx-3">
    <div class="scrollableMenu__item  ml-1">أفضل التجارب</div>
    <div v-for="category in categories" :key="category" 
    class="scrollableMenu__item  mx-1"
    :class="{ active : active == category }"
      @click="filterValue(category)"> {{ category }} </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        active : '',
        isActive: false,
        categories: [
          'رياضه',
          'فن',
          'صحه',
          'تعليم',
          'مهارات حياه',
          'تصميم',
          'ترفيه',
          'برمجه'
        ]
      }
    },
    methods: {
      filterValue(category) {
        this.$store.state.experienceFilterValue = category;
        this.active = category;
        this.isActive = true;
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import '../styles/components/CategoriesList';
</style>