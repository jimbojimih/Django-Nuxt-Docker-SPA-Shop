<template>
  <div>
    <navbar @set_category="get_category"/>
         
    <transition>
      <abouth v-if="category === 'abouth'"/> 
      <checkout v-else-if="category === 'checkout'"  /> 
      <items v-else :category="category" :key="index" />
    </transition>

    <div v-if="category != 'checkout'" @click="get_category('checkout')" class="circle d-md-none" >
      <cart  class='cart' />    
    </div>
  </div>
</template>

<script>
export default { 
  data () {
    return {
      category: 'abouth',
      index: 1,
    }
  },

  methods: {
    get_category (data) {
      this.category = data,
      this.index++        
    }
  }
}
</script>

<style scoped>
.v-enter-active{
  transition: opacity 1s;
}

.v-enter, .v-leave-to  {
  opacity: 0;
}

.circle{
    position: fixed;
    bottom: 15px;
    right : 15px;
    cursor: pointer;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: white;
    box-shadow: 0 0.5em 0.5em 0 rgba(0,0,0,.1); 
} 

.cart{
    margin-top: 12px;
    margin-left: 10px;
} 

</style>

.cart{
    position: fixed;
    bottom: 15px;
    right : 15px;
    cursor: pointer;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: white;
    box-shadow: 0 0.6em 0.6em 0 rgba(0,0,0,.1); 
} 
