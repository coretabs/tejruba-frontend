/<template>
    <div class="snackbar">
        <v-snackbar auto-height class="snackbar_error" :color="snackbar.color" :timeout="timeout"
            v-model="snackbar.trigger">
            {{ snackbar.message }}
            <!-- <v-btn flat color="white" @click.native="snackbar.trigger = false">فهمت</v-btn> -->
        </v-snackbar>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
    export default {
        data() {
            return {
        timeout:parseInt('3000'),

            }
        },
        computed: {
      ...mapGetters(['snackbar']),

        },
    }
</script>