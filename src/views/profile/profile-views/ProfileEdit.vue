<template>
    <div class="profileEdit">
        <v-container color="white" class="mb-5">  
                <v-avatar size="100" class=" mt-2 elevation-10">
                    <img src="../../../assets/avatar.png" class=" relative" alt="alt">
                    <div class="overaly">
                        <v-icon dark>fas fa-upload</v-icon>
                    </div>
                </v-avatar>
<v-divider class="my-4"></v-divider>

            <v-form class="">
                <v-text-field color="primary" label="الاسم"></v-text-field>
                <v-text-field color="primary" label="المهنه"></v-text-field>
                <v-text-field label="نبذه" textarea flat></v-text-field>
                <v-select label="العمر" :items="ages" v-model="user_age"></v-select>
                <v-select label="البلد" :items="country" v-model="userCountry" autocomplete></v-select>
            </v-form>
            <v-subheader>حسابات التواصل</v-subheader>
            <v-expansion-panel expand>
                <v-expansion-panel-content>
                    <div slot="header" class="text-xs-right">حسابات التواصل</div>
                    <v-card>

                        <v-text-field name="فيسبوك" label="فيسبوك" single-line prepend-icon="fas fa-facebook" small>
                        </v-text-field>
                        <v-text-field name="تويتر" label="تويتر" single-line prepend-icon="fas fa-twitter" small>
                        </v-text-field>
                        <v-text-field name="البريد" label="البريد" single-line prepend-icon="fas fa-mail" small>
                        </v-text-field>
                        <v-text-field name="موقع شخصي" label="موقع شخصي" single-line prepend-icon="fas fa-earth" small>
                        </v-text-field>

                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-btn round class="btn-color elevation-14 mx-0 mt-3" dark> حفظ </v-btn>
        </v-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                userAge: '',
                userCountry: '',
                country: [
                    'السودان', 'العراق', 'مصر ', 'الجزائر', 'لبنان', 'تونس', 'الصومال'
                ],
                ages: [
                    '14 - 18',
                    '19 - 30',
                    '31 - 40',
                    '41 - 50',
                    '50 +',
                ]
            }
        }
    }
</script>

<style lang="scss">
    @import '../../../styles/views/profile/profileViews/profileEdit';
</style>