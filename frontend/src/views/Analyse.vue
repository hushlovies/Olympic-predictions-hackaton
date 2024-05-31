<style scoped>

.inner-div {
  text-align: center;
  max-width: 900px;
}
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

<template>
  <div class="container text-black bg-white mx-auto mt-10 text-center">
    <h1 class="text-2xl font-bold mb-4 pt-7">Analyse</h1>
    <div class="inner-div mx-auto">
      <p class="mt-10">
        Here are some data graphs generated using the notebook. They include the top 10 countries participating in the Olympics and the age and gender distribution of the athletes. For more details, please refer to the notebook.
      </p>
      <div class="mx-auto my-4">
        <img src="../assets/images/medal1.png"  class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/medal2.png"  class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img :src="plotUrl" alt="Top 10 Countries Participated In Olympics" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/carte.png" alt="Carte" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/ageDist.png" alt="Age Distribution" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/season.png" alt="Season Distribution" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/distSex.png" alt="Distribution according to sex" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/womenPart.png" alt="Distribution according to sex" class="mx-auto">
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      plotUrl: ''
    };
  },
  mounted() {
    this.fetchPlot();
  },
  methods: {
    fetchPlot() {
      fetch('http://localhost:5000/plot')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.blob();
        })
        .then(blob => {
          const objectURL = URL.createObjectURL(blob);
          this.plotUrl = objectURL;
        })
        .catch(error => {
          console.error('Error fetching plot:', error);
        });
    }
  }
};
</script>