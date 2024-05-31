<template>
  <div class="min-h-screen bg-white text-gray-900">
    <header class="w-full bg-white p-6 shadow">
      <div class="text-center max-w-4xl mx-auto">
        <img src="../assets/images/Paris 2024 - Logo HD.png" alt="Carte" class="mx-auto">
        <h1 class="text-3xl font-bold text-gray-800 mb-2">Jeux olympiques</h1>
        <p class="text-gray-600">This website serves as forecasting the winners of the 2024 Paris Olympics. Using advanced data analytics, historical performance metrics, 
          and expert insights, our platform provides up-to-date predictions for each event. 
          Stay ahead of the competition with real-time updates, in-depth athlete profiles, and comprehensive analyses, 
          ensuring you have the most accurate predictions for the upcoming Olympic Games.
        </p>
      </div>
    </header>

    <main class="w-full p-6">
      <div class="max-w-4xl mx-auto">
        <section class="mb-6">
          <h2 class="text-2xl font-bold text-gray-800 mb-4 ">Key Numbers</h2>
          <div class="grid grid-cols-2 gap-4 flex justify-center">
            <div class="bg-gray-200 p-4 rounded shadow"><h1 class="goldSpan">{{ totalAthletes }}</h1>Nombre total d'Athètes</div>
            <div class="bg-gray-200 p-4 rounded shadow"><h1 class="goldSpan">{{ totalCountries }}</h1>Total Pays participant</div>
          </div>
        </section>
        
        <section>
          
          <div class=" p-4 rounded shadow ">
            <i>In 2024, the Opening Ceremony will take place on the Seine, in the heart of the host city. Experience this exceptional event with your guests, enjoying quick access to the site, premium hospitality, and seats offering a breathtaking view of Paris and the celebrations.</i>
            <div class="mt-10 h-full flex items-center justify-center">
              <img src="../assets/images/xparis-olympics.jpg" alt="Carte" class="mx-auto">
            </div>
          </div>
          <br><br>
        </section>
      </div>
    </main>
  </div>
</template>
<style>
  .goldSpan{
    color:#D7C378;
  }
</style>
<script>
export default {
  data() {
    return {
      totalAthletes: 0,
      totalCountries: 0
    };
  },
  mounted() {
    fetch('http://localhost:5000/')
      .then(response => response.json())
      .then(data => {
        this.totalAthletes = data.totalAthletes;
        this.totalCountries = data.totalCountries;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }
};
</script>
