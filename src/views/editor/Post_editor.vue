<template>

<!-- 
                  #تعديلات مهمه #
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
-->

  <v-container fluid class="pa-2">
    <div class="clipped-header hidden-md-and-up"></div>

    <!-- toolbar -->

    <v-layout row justify-center align-center wrap>
      <v-btn router to="/signin">
        <v-icon small right class="primary--text  ml-2">fas fa-upload</v-icon>
        <span > رفع صوره </span>
      </v-btn>

      <v-btn router to="/signup">
        <v-icon small right class="primary--text ml-2">fas fa-search</v-icon>
        <span >unsplash</span>
      </v-btn>
<v-spacer></v-spacer>
      <v-btn router to="/preview" icon class="white">
        <v-icon small class="primary--text" >fas fa-eye</v-icon>
      </v-btn>
    </v-layout>

    <v-text-field
     box
     dark
     class="white--text mt-2"
      name="name" label="عنوان التجربه " ></v-text-field>
    <v-select
     label="إختر فئه التجربه"
      chips 
      solo
       prepend-icon="" 
       append-icon="fas fa-filter" 
       clearable
       :items="categories" v-model="selectedCategory" 
       >
      <template slot="selection" slot-scope="">
        <v-chip close :selected="selectedCategory">
          <strong>{{ selectedCategory }}</strong>&nbsp;
        </v-chip>
      </template>
    </v-select>
    <!-- editor -->

    <quill-editor v-model="content" class="editor-example" ref="myTextEditor" :options="editorOption"> </quill-editor>

    <!-- control -->
    <v-layout row wrap class="mb-5">
      <v-btn  > حفظ </v-btn>
      <v-spacer></v-spacer>
      <v-btn class="publish elevation-15" dark > نشر </v-btn>
    </v-layout>
  </v-container>
</template>


<script>
  import 'quill/dist/quill.bubble.css'
  // import 'quill/dist/quill.snow.css'
  import {
    quillEditor
  } from 'vue-quill-editor'
  import {
    mapGetters
  } from 'vuex'
  export default {
    components: {
      quillEditor
    },
    data() {
      return {

        content: '',
        isMounted: false,

        categories: [
          'السودان', 'العراق', 'مصر ', 'الجزائر', 'لبنان', 'تونس', 'الصومال'
        ],
        selectedCategory:[],
        
        editorOption: {
          theme: 'bubble',
          placeholder: "إبدا بكتابه تجربتك...",
          modules: {
            toolbar: [
              ['bold', 'italic', 'underline', 'strike'],
              [{
                'list': 'ordered'
              }, {
                'list': 'bullet'
              }],
              [{
                'header': [1, 2, 3, 4, false]
              }],
              [{
                'color': []
              }, {
                'background': []
              }],
              [{
                'font': []
              }],
              [{
                'align': []
              }],
              ['link', 'image'],
            ]
          },
        },
      }
    },
    mounted: function () {
      this.isMounted = true
      this.$store.state.currentPage = this.$route.name;

      if (!this.content && this.contents) {
        this.content = this.contents
      }
    },

    watch: {
      content(val) {
        if (!this.isMounted) {
          this.$store.commit('setDelta', this.$refs.myTextEditor.quill.getContents())
        }
        this.$store.commit('setContent', val)
        this.isMounted = false
      }
    },

    methods: {
      test: function () {
        console.log(this.$refs.myTextEditor.quill.getContents())
      }
    },
    computed: {
      ...mapGetters(['delta', 'contents'])
    },

  }
</script>

<style lang="scss" >

@import '../../styles/views/editor';

</style>