style='text-align: right' 
<template>
<div class="container">
  <div class='centred'>
    <div>Оформление заказа.</div>
    <div v-if="list_items === 'empty'" >Корзина пуста, пожалуйста добавьте товары</div>
    <div v-else>
      <div>Количество товаров: {{checkout['quantity']}}, Общая сумма: {{checkout['price']}} ₽.</div>
      <div class='check'> Проверьте выбранные товары:</div>
      <div v-for="(item, index) in list_items" :key='item.id'>  

        <b-card style='margin-top:5px' :img-src="item.image" img-alt="Изображение товара" img-left no-body img-height=100>
          <b-card-body style='line-height: 50px; padding-left: 5px; padding-right: 10px'>
            {{item.name}} 
            <span style='float: right'>
              {{item.price}} ₽
              <b-button variant='info' @click="del(item.id, index)"> X </b-button>
            </span>
          </b-card-body>
        </b-card> 

      </div>
        <user-form style='margin-top:20px' />
    </div> 
  </div>
    <div class='final'> После выполнения заказа мы свяжемся с Вами по указанным реквизитам для согласования заказа. </div>
</div>
</template>

<script>
  export default {
    data() {
      return {
        list_items: [],  
      }
    },    
    async fetch() {
      this.list_items = await this.$axios.$get(`cart/`);
    },
    methods:{
      del (id, index){
        this.$axios.delete(`cart/`+ id + `/`); 
        this.list_items.splice(index, 1);
        this.$store.commit('localStorage/remove_cart_total');
        if (this.list_items.length == 0)
          this.list_items = 'empty'
      },
    },
    computed: {
      //getter
      checkout() {
        let groups = {};
        let quantity = 0
        let price = 0
        for (let item of this.list_items) {
          price += Number(item.price)
        }
        groups['quantity']=this.list_items.length
        groups['price'] = price        
        return groups;
      }
    },
}
</script>

<style scoped>
.container { 
  max-width:960px;
  font-family: 'Corner One';
}

.centred {
  display: table;
  margin: 0 auto
}

.final {
  display: table;
  margin: 0 auto;
  margin-top: 15px;
}

.check {
  margin-top: 15px;
  margin-bottom: 15px;
}

</style>