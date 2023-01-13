<template>
<div>
  <b-card class="card_style" :class="{selled: !product.available}">
    <b-card-img class="card_image"  :src="product.images[0].image" alt="Изображение">
    </b-card-img>  

    <div class='name'> {{product.name}} </div>

    <b-card-text v-if='product.available === true' class="price"> 
      {{product.price}} ₽
    </b-card-text>
    <b-card-text v-else class="price"> 
        Товар продан
    </b-card-text> 
  </b-card>
</div>
</template>

<script>
  export default {
    props: ['product', ],
  }    
</script>

<style>
.card_style {
border: none;
}

.name {
margin-top: 5px
}

.price {
text-align: right;
margin-bottom: 0px
}

.selled {
opacity: 0.4;
}
</style>