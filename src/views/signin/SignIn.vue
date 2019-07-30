<template>
    <div class="signin">
        <div class="clipped-e-header hidden-md-and-up">
            <img src="../../assets/t_logo.png" class="logo" alt="logo">
            <div class="overlay">
            </div>
        </div>
        <v-container fluid>
            <v-layout column class="full" align-center justify-center>
                <v-spacer></v-spacer>

                <v-form>
                    <v-text-field name="name" label="الاسم"></v-text-field>
                    <v-text-field name="name" label=" كلمه السر " hint="At least 8 characters" min="8"></v-text-field>
                    <v-btn round class="btn-color white--text my-4">استمرار</v-btn>
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

    }
</script>

<style lang="scss" scoped>
    @import '../../styles/views/signin/SignIn';
</style>