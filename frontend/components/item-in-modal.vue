<template>
  <div>
    <b-carousel indicators controls :interval="0">
      <div v-for="image_dict in one_item.images" > 
        <b-carousel-slide :img-src="image_dict.image"></b-carousel-slide>
      </div>
    </b-carousel>
    
    <div class='name'> {{one_item.name}} </div>
    <div class='text'> {{one_item.description}} </div>
    <div class='text' v-if='one_item.available === true'> Цена {{one_item.price}} ₽</div>
    <div class='articul'> Артикул №{{one_item.id}} </div>

    <b-button variant='info' @click="buy(one_item.id), $emit('close_modal')" v-if='one_item.available === true'>
      Купить
    </b-button>
  </div>
</template>

<script>
export default {
  props: ['one_item', ],  
  
  methods:{
    async buy (id, store){
      const response = await this.$axios.post(`cart/`, {
        item: this.one_item.id
      })
      if (response.data == 'already added') 
        this.$root.$bvToast.toast('Товар уже в корзине', {
          noCloseButton: true,
          variant: 'primary',
          autoHideDelay: 1500,
          toaster: 'b-toaster-bottom-center'
          })
      else
        this.$store.commit('localStorage/add_cart_total')       
    }
  }
}

</script>

<style scoped>
.text {
  font-family: 'Corner One';
}

.articul {
  font-size: 10pt;
}

.name {
  font-family: 'Corner One';
  font-size: 14pt;
}
</style>