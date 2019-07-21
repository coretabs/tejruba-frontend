<template>
  <div class="scrollableMenu mt-3 mx-3">
    <div class="scrollableMenu__item  ml-1 active">أفضل التجارب</div>
      <div v-for="category in categories" :key="category" 
           class="scrollableMenu__item  mx-1 "> {{ category }} </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
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
    }
  }
</script>

<style lang="scss" scoped>
  @import '../styles/components/CategoriesList';
</style>