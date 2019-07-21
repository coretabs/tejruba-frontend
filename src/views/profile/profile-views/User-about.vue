<template>
    <div class="user-about mb-5">
        <v-layout column class="text-xs-right"> 
            <v-card v-for="card in infoCards" :key="card.id" class="my-1 elevation-4 ">
                <v-card-title primary-title class="py-2">
                        <h4 class="primary--text">{{ card.title }}</h4>
                </v-card-title>
                 <v-divider inset></v-divider>
                <v-card-text >
                        <p class="mb-0">{{ card.data }}</p>
                </v-card-text>
            </v-card>
        </v-layout>
    </div>
</template>

<script>  
export default {
    data(){
        return{
            infoCards:[
                {
                  id:0,
                  title:'اسمي',
                  data:'حسان ثابت محمداحمد' 
                },
                {
                  id:1,
                  title:'نبذه عني',
                  data: 'نص يحتويي على نبذه عن الكاتب صاحب التجربه' 
                },
                
                {
                  id:2,
                  title:'مهنتي',
                  data:'مطور مواقع' 
                },
                {
                  id:3,
                  title:'عمري',
                  data:'21' 
                },
                {
                  id:4,
                  title:'بلدي',
                  data:'السودان' 
                },
            ]
        }
    }

}
</script>

<style>
</style>
