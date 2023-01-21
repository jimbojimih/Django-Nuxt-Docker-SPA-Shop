<template>
<div class="container">
  
  <b-carousel indicators controls :interval="5000" class="abouth_carusel">
    <b-carousel-slide 
      style="text-shadow: 0px 0px 2px #000"
      img-src="../static/1.png"
      caption="Описание 1"
    ></b-carousel-slide>
    <b-carousel-slide 
      style="text-shadow: 0px 0px 2px #000"
      img-src="../static/2.png"
      caption="Описание 2"
    ></b-carousel-slide>
    <b-carousel-slide 
      style="text-shadow: 0px 0px 2px #000"
      img-src="../static/3.png"
      caption="Описание 3"
    ></b-carousel-slide>
  </b-carousel>
 
  <div class='centred' style="margin-top: 15px">
    <strong>Bird & star</strong> — лаконичный и минималистичный бренд детских игрушек и декора для комнаты малыша. Игрушки и декор изготавливаются из натуральных тканей и материалов.
    Все игрушки и декор выполнены с любовью к детям, они безопасны и призваны радовать ребенка, а также способствовать его развитию. Если товар продан, то напишите нам его артикул.
  </div>
    <div style="margin-top: 15px">
      По всем интересующим вопросам пишите нам в <b-link  href="https://t.me/NinaStrateichyk"> Telegram</b-link>.
    </div>  

</div>
</template> 
 
<script>  
</script>
  
<style scoped>
.container{
  max-width:960px;
  font-family: 'Corner One';
  font-size: 16px;
}

.centred {
  display: table;
  margin: 0 auto
}

.abouth_carusel {
  display: table;
  margin: 0 auto;
  max-width: 600px;

}

</style>