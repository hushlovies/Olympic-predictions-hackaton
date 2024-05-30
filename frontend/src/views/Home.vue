<template>
  <div class="min-h-screen bg-white text-gray-900">
    <header class="w-full bg-white p-6 shadow">
      <div class="text-center max-w-4xl mx-auto">
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
          <h2 class="text-2xl font-bold text-gray-800 mb-4">Key Numbers</h2>
          <div class="grid grid-cols-3 gap-4">
            <div class="bg-gray-200 p-4 rounded shadow">Nombre total d'Athètes : {{ totalAthletes }}</div>
            <div class="bg-gray-200 p-4 rounded shadow">Total Pays participant : {{ totalCountries }}</div>
            <div class="bg-gray-200 p-4 rounded shadow">  </div>
          </div>
        </section>

        <section>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">Info</h2>
          <div class=" p-4 rounded shadow h-96">
            <p>En 2024, la Cérémonie d'ouverture aura lieu sur la Seine, au coeur de la ville hôte. Vivez cet évènement exceptionnel avec vos invités en profitant d'un accès rapide au site, d'une hospitalité haut de gamme et de places offrant une vue imprenable sur Paris et les célébrations.</p>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

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
