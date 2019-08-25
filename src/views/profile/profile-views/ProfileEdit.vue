<template>
    <div class="profileEdit">
        <v-container color="white" class="mb-5">
            <v-layout column justify-center align-center>
                <v-avatar size="100" class=" my-2 elevation-10">
                    <img :src="avatar || 'http://s3.amazonaws.com/37assets/svn/765-default-avatar.png'" class=" relative" alt="alt">
                    <div class="overaly" v-show="uploadOverlay" @click="onPickAvatar">
                        <v-icon dark @click="updateAvatar">fas fa-upload</v-icon>
                    </div>
                </v-avatar>
                <input v-show="false" type="file" ref="avatarInput" accept="image/*" @change="onImgUploaded">
                <v-layout row my-3>
                    <v-btn color="primary" v-show="isReady">حفظ</v-btn>
                <v-btn  v-show="isReady" @click="onPickAvatar">تعديل</v-btn>
                </v-layout>
            </v-layout>
            <v-form ref="userInfoForm" class="">
                <v-text-field color="primary" label="الأسم الكامل*" v-model="FullName" required :rules="nameRules">
                </v-text-field>
                <v-text-field color="primary" label="*المهنه" v-model="Job" required
                    :rules="[v => !!v || 'يجب تحديد مهنتك']"></v-text-field>
                <v-textarea outline class="mt-3" label="نبذه عنك*" flat v-model="Bio" required :rules="BioRules">
                </v-textarea>
                <v-select label="العمر" :items="ages" v-model="Age"></v-select>
                <v-autocomplete label="البلد*" :items="contries" v-model="Country" required
                    :rules="[v => !!v || 'يجب تحديد بلدك']"></v-autocomplete>
            </v-form>
            <v-expansion-panel expand class="mt-2">
                <v-expansion-panel-content>
                    <div slot="header" class="text-xs-right">حسابات التواصل</div>
                    <v-card class="px-3 py-2 grey lighten-4">
                        <v-text-field prepend-icon="fab fa-facebook" label="فيسبوك" v-model="facebook"></v-text-field>
                        <v-text-field prepend-icon="fab fa-twitter" label="تويتر" v-model="twitter"></v-text-field>
                        <v-text-field prepend-icon="fas fa-link" label="موقعك الشخصي" v-model="website"></v-text-field>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-btn round class="btn-color elevation-14 mx-0 mt-3" dark @click="onSave"> حفظ </v-btn>
            <snack-bar />
        </v-container>
    </div>
</template>

<script>
    import snackBar from '@/components/sharedComponents/snackbar.vue'
    export default {
        components: {
            snackBar,
        },
        data() {
            return {
                uploadOverlay: true,
                isReady: false,
                FullName: '',
                avatar: '',
                Bio: '',
                Job: '',
                Age: '',
                Country: '',
                facebook: '',
                twitter: '',
                website: '',
                contries: [
                    'السودان', 'العراق', 'مصر ', 'الجزائر', 'لبنان', 'تونس', 'الصومال'
                ],
                ages: [
                    '14 - 18',
                    '19 - 30',
                    '31 - 40',
                    '41 - 50',
                    '50 +',
                ],
                nameRules: [
                    v => !!v || 'يجب ادخال الإسم',
                    v => (v && v.length >= 12) || ' أسم على الاقل 12 أحرف',
                ],
                BioRules: [
                    v => !!v || 'يجب ادخال نبذه عنك',
                    v => (v && v.length >= 120) || 'طول النبذه على الأقل 120 حرف',
                ],
            }
        },

        methods: {
            onPickAvatar: function () {
                this.$refs.avatarInput.click()
            },
            onImgUploaded: function (event) {
                const file = event.target.files[0]
                let fileName = file.name
                this.image = file
                const allowedType = ['image/jpeg', 'image/png']
                const isAllowedType = allowedType.includes(file.type)
                if (fileName.lastIndexOf('.') <= 0) {
                    return alert('قم باضافه صوره صالحه')
                }
                const fileReader = new FileReader()
                fileReader.addEventListener('load', () => {
                    this.avatar = fileReader.result
                })
                    //-- to server---
                    this.uploadOverlay = false
                    this.isReady = true
                fileReader.readAsDataURL(file)
            },

            updateAvatar: function () {
                this.$store.commit('UpdateUserAvatar', this.avatar)
            },

            onSave: function () {
                if (this.$refs.userInfoForm.validate()) {
                    let userInfo = {
                        avatar: this.avatar,
                        FullName: this.FullName,
                        Bio: this.Bio,
                        Job: this.Job,
                        Age: this.Age,
                        Country: this.Country,
                        facebook: this.facebook,
                        twitter: this.twitter,
                        website: this.website,
                    }
                    this.$store.commit('UpdateUserInfo', userInfo)
                } else {
                    let snackbar = {
                        message: 'بعض الحقول ضروريه',
                        color: 'error'
                    }
                    this.$store.commit('updateSnackbar', snackbar)
                }
            },
        }
    }
</script>

<style lang="scss">
    @import '../../../styles/views/profile/profileViews/profileEdit';
</style>