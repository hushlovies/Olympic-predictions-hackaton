<style>
.medal {
  display: inline-block; /* Assure que l'image et le texte sont sur la même ligne */
  vertical-align: middle; /* Centre verticalement les images avec le texte */
}

.medal-count {
  display: inline-block;
  vertical-align: middle;
  margin-left: 2px; /* Espacement entre l'image et le texte */
  margin-right: 10px; /* Espacement entre les groupes de médailles */
}
</style>


<template>
  <div class="container mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Athletes</h2>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">Full Name</th>
          <th class="px-4 py-2">Games Participations</th>
          <th class="px-4 py-2">First Game</th>
          <th class="px-4 py-2">Year of Birth</th>
          <th class="px-4 py-2">Medals</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="athlete in athletes" :key="athlete.athlete_url" class="bg-white border-b">
          <td class="px-4 py-2">{{ athlete.athlete_full_name }}</td>
          <td class="px-4 py-2">{{ athlete.games_participations }}</td>
          <td class="px-4 py-2">{{ athlete.first_game }}</td>
          <td class="px-4 py-2">{{ athlete.athlete_year_birth }}</td>
          <td class="px-4 py-2">
            <span class="medal"><img src="../assets/gold.png" class="h-4"> <span class="medal-count">{{ parseMedals(athlete.athlete_medals, 'G') }}</span></span>
            <span class="medal"><img src="../assets/silver.png" class="h-4"> <span class="medal-count">{{ parseMedals(athlete.athlete_medals, 'S') }}</span></span>
            <span class="medal"><img src="../assets/bronze.png" class="h-4"> <span class="medal-count">{{ parseMedals(athlete.athlete_medals, 'B') }}</span></span>
          </td>
        </tr>
        <tr v-if="athletes.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="5">No data available</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      athletes: []
    };
  },
  methods: {
    parseMedals(data, medalType) {
      const regex = new RegExp(`(\\d+)${medalType}`, 'i');
      const match = data.match(regex);
      return match ? match[1] : 0;
    }
  },
  mounted() {
    fetch('http://localhost:5000/athletes')
      .then(response => response.json())
      .then(data => {
        this.athletes = data.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>
