animation='throb'
shift-h=20 shift-v=-10
<template>
  <div class= 'opacity'>
    <b-icon class="icon"  icon="BIconCart" font-scale=2></b-icon>    
    {{ $store.state.localStorage.cart_total }}
  </div>
</template>

<script>
import {BIcon, BIconCart} from 'bootstrap-vue'
export default{
  components: {
    BIcon,
   BIconCart,
  }
}
</script>

<style scoped>
.opacity {
  opacity: 0.6
}
</style>