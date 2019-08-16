<template>
    <div class="signin">
        <div class="clipped-e-header hidden-md-and-up">
            <img src="../../assets/img/T_logo.svg" class="logo" alt="logo">
            <div class="overlay">
            </div>
        </div>
        <v-container fluid>
            <v-layout column class="full" align-center justify-center>
                <v-spacer></v-spacer>

                <v-form ref="signInForm">
                    <v-text-field name="email" label="البريد" v-model="email" :rules="emailRules" required>
                    </v-text-field>
                    <v-text-field name="password" type="password" label=" كلمه السر " hint="At least 8 characters"
                        :rules="passwordRules" required></v-text-field>
                    <v-btn round @click="login" class="btn-color white--text my-4">استمرار</v-btn>
                </v-form>
                <v-spacer></v-spacer>

                <v-flex>
                    <p>ليس لديك حساب؟ <span class="primary--text font-weight-bold " router to="/singUp">انشاء حساب</span></p>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                email: '',
                emailRules: [
                    v => !!v || ' يجب إدخال البريدالإلكترني',
                    v => /.+@.+\..+/.test(v) || 'يجب إدخال بريد إلكتروني صالح',
                ],

                password: '',
                passwordRules: [
                    v => !!v || 'قم بإدخال كلمه المرور',
                    v => (v && v.length >= 8) || 'كلمه المرور على الاقل 8 أحرف',
                ],

            }
        },
        methods: {
            login: function() {
                if(this.$refs.signInForm.validate()){
                    console.log('success');
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/views/signin/SignIn';
</style>