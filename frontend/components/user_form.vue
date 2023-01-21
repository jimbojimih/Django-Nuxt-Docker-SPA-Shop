<template>
<div>
  <b-form class="form_style" @submit="send_user_fields">
    <b-form-group id="input-group-1" label-for="input-1" description="Обязательное поле.">
      <b-form-input 
        id="input-1" 
        :value=$store.state.localStorage.first_name 
        @input="set_form_value('first_name', 'input-1')"
        type="text" 
        placeholder="Как к Вам обращаться." 
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-6" label-for="input-6" description="Обязательное поле.">
      <b-form-input 
        id="input-6" 
        :value=$store.state.localStorage.number_phone 
        @input="set_form_value('number_phone', 'input-6')"
        type="tel" 
        placeholder="Введите номер телефона" 
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label-for="input-2">
      <b-form-input 
        id="input-2" 
        :value=$store.state.localStorage.email 
        @input="set_form_value('email', 'input-2')"
        type="email" 
        placeholder="Введите почту" 
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-3" label-for="input-3">
      <b-form-input 
        id="input-3" 
        :value=$store.state.localStorage.city 
        @input="set_form_value('city', 'input-3')"
        type="text" 
        placeholder="Введите город"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-4" label-for="input-4">
      <b-form-input 
        id="input-4" 
        :value=$store.state.localStorage.street 
        @input="set_form_value('street', 'input-4')"
        type="text" 
        placeholder="Введите улицу"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-5" label-for="input-5">
      <b-form-input 
        id="input-5" 
        :value=$store.state.localStorage.house 
        @input="set_form_value('house', 'input-5')" 
        type="text" 
        placeholder="Введите дом"
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-7" label-for="input-7">
      <b-form-input 
        id="input-7" 
        :value=$store.state.localStorage.comments 
        @input="set_form_value('comments', 'input-7')"
        type="text" 
        placeholder="Комментарии"
      ></b-form-input>
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
      set_form_value(key, id) {
        let value = document.getElementById(id).value 
        let payload = {'key' : key, 'value': value}
        this.$store.commit('localStorage/set_form_value', payload)
        this.form[key] = value
      },
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
          setTimeout(this.$router.go() , 5000)      
        }
    },
    mounted() {
      for (let key in this.form) {
        this.form[key] = this.$store.state.localStorage[key]
      }       
    }
}    
</script>

<style scoped>
.form_style{
max-width:400px;
}

</style> 