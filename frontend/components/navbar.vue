<template> 
  <b-navbar :sticky=true class="my_nav" toggleable="md" type='light'>  
    <div class="container">

      <b-navbar-nav class="pointer" @click="$emit('set_category', 'abouth')"> 
        <img src="favicon.ico" width="140" height="30" alt="название магаза">
      </b-navbar-nav>

      <b-navbar-toggle class="toggle" target="nav-collapse" ></b-navbar-toggle>      
      
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav >
          <b-nav-item @click="$emit('set_category', 'abouth')">О нас</b-nav-item>
        </b-navbar-nav>   

        <b-navbar-nav v-for="category in categories" :key=category.id>
          <b-nav-item @click="$emit('set_category', category.name)">{{category.name}}</b-nav-item>
        </b-navbar-nav>  

        <b-navbar-nav >
          <b-nav-item @click="$emit('set_category', 'checkout')">Оформить</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav @click="$emit('set_category', 'checkout')" class='pointer ml-auto d-none d-md-block'>
          <cart /> 
        </b-navbar-nav>  

      </b-collapse>
    </div>
  </b-navbar>
</template>

<script>
import axios from "axios";
  export default {      
    data() {
      return {
        categories: []
      }
    },

    async fetch() {
      this.categories = await this.$axios.$get(`category/`)
    }
  }
</script>

<style scoped>
.my_nav {
  font-family: 'Corner One';
  background-color: white;
  box-shadow: 0 5px 4px 0 rgba(0,0,0,.1); 
  margin-bottom: 15px

}

.margin {
  margin-left: 15px;
}

.container{
max-width:960px;
}

.toggle {
  border: none;
  outline: none;
}

.toggle:before {
    content:"Каталог";
    margin-right: 10px;
}

.pointer{
    cursor: pointer;
} 

</style> 

font-size: 16px;