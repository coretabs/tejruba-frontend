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
      <v-btn @click="uploadDialog = true">
        <v-icon small right class="primary--text  ml-2">fas fa-upload</v-icon>
        <span> صوره </span>
      </v-btn>

      <!-- dialog -->
      <v-dialog v-model="uploadDialog" max-width="500px">
        <v-card>
          <v-card-title>
            إختيار صوره
          </v-card-title>
          <v-card-text>
            <v-layout column wrap align-start>
              <v-flex shrink>
                <v-btn router to="/signin" class="mb-3">
                  <v-icon small right @click="uploadDialog = true" class="primary--text">fas fa-upload</v-icon>
                  <span> إختيار صوره من الجهاز </span>
                </v-btn>
              </v-flex>
              <v-divider class="mx-4" dark></v-divider>
              <v-flex>
                <v-text-field solo append-icon="fas fa-link" label="عنوان الصوره" placeholder="لصق رابط الصوره"
                  v-model="ImgUrl"></v-text-field>
              </v-flex>
            </v-layout>
          </v-card-text>
          <v-card-actions>
            <v-btn class="publish ml-3" color="success" text @click="save">
              حفظ
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="white darken-1" @click="uploadDialog = false">
              إغلاق
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- dialog -->
      <v-btn router to="/signup">
        <v-icon small right class="primary--text ml-2">fas fa-search</v-icon>
        <span>unsplash</span>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn router to="/preview" icon class="white">
        <v-icon small class="primary--text">fas fa-eye</v-icon>
      </v-btn>
    </v-layout>
    <v-form ref="editorForm">
      <v-text-field box color="gray" dark class="white--text mt-2" name="name" label="عنوان التجربه" v-model="Title"
        :rules="[v => !!v || 'قم بإدخال عنوان للتجربه']" required>
      </v-text-field>

      <v-select :items="categories" :rules="[v => !!v || 'يجب إختيار فئه للتجربه']" v-model="Category"
        label="إختر فئه التجربه" chips solo clearable required>
      </v-select>

      <!-- editor -->

      <quill-editor v-model="content" id="editorQuill" ref="myTextEditor" :options="editorOption"> </quill-editor>

    </v-form> <!-- control -->
    <v-layout row wrap class="mb-5">
      <v-btn @click="test()"> حفظ </v-btn>
      <v-spacer></v-spacer>
      <v-btn class="publish elevation-15" @click="publish()" dark> نشر </v-btn>
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
  import moment from 'moment'
  export default {
    components: {
      quillEditor
    },
    data() {
      return {
        content: '',
        isMounted: false,
        uploadDialog: false,

        ID: '',
        ImgUrl: '',
        Title: '',
        Category: '',
        Delta: '',
        Hearts: '',
        Likes: '',
        Stars: '',

        categories: [
          'رياضه',
          'فن',
          'صحه',
          'تعليم',
          'مهارات حياه',
          'تصميم',
          'ترفيه',
          'برمجه'
        ],


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
          // this.$store.commit('setPostDelta', this.$refs.myTextEditor.quill.getContents()/
          // this.$store.commit('setPostContent')
        }
        this.$store.commit('setContent', val)
        this.isMounted = false
      },
    },

    computed: {
      ...mapGetters(['delta', 'contents', 'editorData']),
    },
    methods: {
      publish: function () {
        this.$store.commit('publishPost', {
          ID: this.$store.state.altjarub.length,
          Img: this.ImgUrl,
          Title: this.Title,
          Category: this.Category,
          //--
          Delta: this.delta,
          //--
          Date: this.$moment().fromNow(),
          //--
          Hearts: this.Hearts,
          Stars: this.Stars,
          Likes: this.Likes,
        });
        this.$router.push('/');
        this.$refs.editorForm.reset();
      },
      save: function () {
        this.uploadDialog = false
      },
      test: function () {
        // console.log(this.$refs.myTextEditor.quill.getContents())
        console.log(this.$store.state.editorData.postDelta);

      }
    },
  }
</script>

<style lang="scss">
  @import '../../styles/views/editor';
</style>