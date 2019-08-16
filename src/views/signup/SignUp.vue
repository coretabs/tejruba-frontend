<template>
    <div class="signin">
        <div class="clipped-e-header hidden-md-and-up">
            <img src="../../assets/img/T_logo.svg" class="logo" alt="logo">
            <div class="overlay">
            </div>
        </div>
        <v-container fluid>
            <v-layout column class="full py-0" align-center justify-center>
                <v-spacer></v-spacer>

                <v-form ref="signUpForm">
                    <v-text-field name="name" label="الاسم" :rules="nameRules" required></v-text-field>
                    <v-text-field name="email" label="الايميل" :rules="emailRules" required></v-text-field>
                    <v-text-field name="password" label=" كلمه السر " :rules="passwordRules" required>
                    </v-text-field>
                    <v-text-field name="password" label="  أعد كلمه السر" :rules="passwordRules1" required></v-text-field>
                    <v-btn round @click="signUp" class="btn-color white--text my-4 elevation-11">استمرار</v-btn>
                </v-form>

                <v-spacer></v-spacer>

                <v-flex>
                    <p>ليس لديك حساب؟ <span class="primary--text font-weight-bold ">انشاء حساب</span></p>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                name: '',
                nameRules: [
                    v => !!v || 'قم بإدخال إسم المستخدم ',
                    v => (v && v.length <= 10) || ' أسم المستخدم على الاقل 10 أحرف',
                ],
                email: '',
                emailRules: [
                    v => !!v || ' يجب إدخال البريدالإلكترني',
                    v => /.+@.+\..+/.test(v) || 'يجب إدخال بريد إلكتروني صالح',
                ],
                password: '',
                passwordRules: [
                    v => !!v || 'قم بإدخال كلمه المرور',
                    v => (v && v.length <= 8) || 'كلمه المرور على الاقل 8 أحرف',
                ],
                password1: '',

                passwordRules1: [
                    v => !!v || ' أعد إدخال كلمه المرور',
                    v => (v && v.length <= 8) || 'على الاقل 8 أحرف',
                ],

            }
        },
        methods: {
            signUp: function(){
                if(this.$refs.signUpForm.validate()){
                    console.log('success');
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/views/signup/SignUp';
</style>