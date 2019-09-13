<template>
  <div class="user-about mb-5">
    <v-layout column class="text-xs-right">
      <v-card v-for="card in infoCards" :key="card.id" v-show="card.data" class="my-1 elevation-4">
        <v-card-title primary-title class="py-2">
          <h4 class="primary--text">{{ card.title }}</h4>
        </v-card-title>
        <v-divider inset></v-divider>
        <v-card-text auto-grow>
          <p class="mb-0">{{ card.data }}</p>
        </v-card-text>
      </v-card>
      <v-layout row justify-center align-center>
        <v-btn v-for="icon in icons" :key="icon" class="mx-3 grey--text" icon :href="icon.url" target="blank">
          <v-icon size="24px">{{ icon.icon }}</v-icon>
        </v-btn>
      </v-layout>
    </v-layout>
  </div>
</template>

<script>
  import {
    mapGetters
  } from 'vuex'
  export default {
    data() {
      return {
        infoCards: [{
            id: 0,
            title: 'اسمي',
            data: this.$store.getters.userInfo.FullName
          },
          {
            id: 1,
            title: 'نبذه عني',
            data: this.$store.getters.userInfo.Bio
          },

          {
            id: 2,
            title: 'مهنتي',
            data: this.$store.getters.userInfo.Job
          },
          {
            id: 3,
            title: 'عمري',
            data: this.$store.getters.userInfo.Age
          },
          {
            id: 4,
            title: 'بلدي',
            data: this.$store.getters.userInfo.Country
          },
        ],
        icons: [{
            icon: 'fab fa-facebook',
            url: this.$store.getters.userInfo.facebook
          },
          {
            icon: 'fab fa-twitter',
            url: this.$store.getters.userInfo.twitter
          },
          {
            icon: 'fas fa-link',
            url: this.$store.getters.userInfo.website
          }
        ]
      }
    },
    computed: {
      ...mapGetters(['userInfo']),
    }

  }
</script>

<style>
</style>