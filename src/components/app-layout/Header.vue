<template>
<div class="toolbar">
    <div class="gradient"></div>
    <v-toolbar app dark color="primary">
        <v-layout row align-center justify-space-between>

            <!-- pageName -->
            <span class="center pr-2 white--text">
                {{ currentPage }}
            </span>

            <!-- logo -->

            <img src="../../assets/T_logo.svg" class="ml-3 " height="25px" />
            <!-- Avatar -->

            <v-avatar size="33" color="primary" >
                <img   src="../../assets/avatar.png"
                    alt="avatar">
            </v-avatar>

        </v-layout>
    </v-toolbar>
</div>
   
</template>

<script>
    export default {
        computed: {
            currentPage() {
                console.log('form header ' + this.$store.state.currentPage);
                return this.$store.state.currentPage
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/components/app-layout/Header';
</style>