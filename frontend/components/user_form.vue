<template>
<div>
  <b-form class="form_style" @submit="send_user_fields">
    <b-form-group id="input-group-1" label-for="input-1" description="Обязательное поле.">
      <b-form-input id="input-1" v-model="form.first_name" type="text" placeholder="Как к Вам обращаться." required>
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-group-6" label-for="input-6" description="Обязательное поле.">
      <b-form-input id="input-6" v-model="form.number_phone" type="text" placeholder="Введите номер телефона" required>
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label-for="input-2">
      <b-form-input id="input-2" v-model="form.email" type="email" placeholder="Введите почту">
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-group-3" label-for="input-3">
      <b-form-input id="input-3" v-model="form.city" type="text" placeholder="Введите город">
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-group-4" label-for="input-4">
      <b-form-input id="input-4" v-model="form.street" type="text" placeholder="Введите улицу">
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-group-5" label-for="input-5">
      <b-form-input id="input-5" v-model="form.house" type="text" placeholder="Введите дом">
      </b-form-input>
    </b-form-group>

    <b-form-group id="input-group-7" label-for="input-7">
      <b-form-input id="input-7" v-model="form.comments" type="text" placeholder="Комментарии">
      </b-form-input>
    </b-form-group>

    <b-button type="submit" variant="info" >Купить</b-button>
  </b-form>    
    
    <b-modal class="buy_modal" :hide-header=true :hide-footer=true :no-close-on-backdrop=true centered ref="buy_modal">Спасибо за покупку</b-modal>
</div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email : "",
        first_name : "",
        city : "",  
        street : "",
        house : "",
        number_phone : "",
        comments : "",  
      }
    }
  },
    methods:{
      send_user_fields(event) {  
        event.preventDefault()       
        this.$axios.patch(`user/`, {
          first_name: this.form.first_name, 
          email: this.form.email,
          profile:{
            city: this.form.city,
            street: this.form.street,
            house: this.form.house,
             number_phone: this.form.number_phone,
             comments: this.form.comments
           }
         }).then(result => this.buy())                         
      },
        buy(){
          this.$axios.get(`buy/`)  
          this.$store.commit('localStorage/clear_cart_total')
          this.$refs.buy_modal.show()
          setTimeout(() => {this.$router.go()} , 5000)      
        }
    }
}    
</script>

<style scoped>
.form_style{
max-width:400px;
}

</style>