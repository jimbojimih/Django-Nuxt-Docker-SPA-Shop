<template>
  <div>
    <b-container class="container">
      <div v-for="sub_category in sub_categories" :key=sub_category.id>
        <p class="sub_cat">{{sub_category.name}}</p>
        <b-row>
          <b-col cols="6" sm="4" v-for="product in grouped[sub_category.name]" :key=product.id v-b-modal.modal_item @click="open_modal(product.id)" class="cards text">       
            <card :product="product"/>  
          </b-col>
        </b-row>
      </div>
    </b-container>

    <b-modal centered :hide-header=true :hide-footer=true size="md" id="modal_item">
      <item-in-modal :one_item="one_item_data" @close_modal='$bvModal.hide("modal_item")' />
    </b-modal>

  </div>
</template>

<script>
import axios from "axios";
  export default {
    props: ['category', ],

    data() {
      return {
        products: [],
        sub_categories: [],
        one_item_data: '',        
      }
    },

    async fetch() {
      const [one, two ] = await axios.all([
        this.$axios.get(`products/`, {
          params:{category: this.category}
        }),
        this.$axios.get(`sub_category/`, {
          params:{category: this.category}
        }),
      ])

      this.products = one.data 
      this.sub_categories = two.data
    },

    methods:{
      open_modal (data){
        this.one_item_data = this.products.filter((filter) => filter.id === data)[0]
      },
    },

//разделяем товары на группы по под_категориям 
    computed: {
      grouped() {
        const groups = {};
        this.products.forEach(product => {
        groups[product.sub_category] = groups[product.sub_category] || [];
        groups[product.sub_category].push(product);  
        })
        return groups;
      }
    },
  }
</script>

<style>

.container{
max-width:960px;
}

.card_image{
border-radius:5%;
}

.cards:hover .card_image {
transform: scale(1.07);
transition-duration: .3s;
}

.sub_cat{
    font-family: 'Corner One';
    display: table;
    margin: 0 auto;
    font-size: 16pt;
    text-decoration-line: underline;
}

.text{
font-family: 'Corner One';
}
</style>

