<template> 
  <b-navbar :sticky=true class="my_nav" toggleable="md" type='light'>  
    <div class="container">

      <b-navbar-nav class='shop_name'> 
        Bird & Star
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

.shop_name {
  font-family: 'Corner One';
  font-size: 20pt;
  color: #CF5469;
  font-weight:bold;
  -webkit-mask-image: linear-gradient(
      -75deg, rgba(0,0,0,.6) 30%, #000 50%, rgba(0,0,0,.6) 70%);
  -webkit-mask-size: 200%;
  animation: shine 2s linear infinite;
}

@keyframes shine {
  from { -webkit-mask-position: 150%; }
  to { -webkit-mask-position: -50%; }
}

</style> 