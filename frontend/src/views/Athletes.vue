<style>
.medal {
  display: inline-block;
  vertical-align: middle;
}

.medal-count {
  display: inline-block;
  vertical-align: middle;
  margin-left: 2px;
  margin-right: 10px; 
}
.navigation{
margin-bottom: 50px;
}
</style>

<template>
  <div class="navigation bg-gray-300" >
      <NavbarTab />
  </div>
  <div class="container mx-auto mb-5">
    <h2 class="text-2xl font-bold mb-4">Athletes</h2>
    
    <div class="mb-4">
      <input v-model="filters.name" type="text" placeholder="Filtre par prénom" class="p-2 border rounded">
      <input v-model="filters.participation" type="number" placeholder="Filtre par participation" class="p-2 border rounded">
      <input v-model="filters.year" type="text" placeholder="Filtre par année de naissance" class="p-2 border rounded">
      <input v-model="filters.country" type="text" placeholder="Filtre par pays" class="p-2 border rounded">
    </div>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">Nom/Prénom</th>
          <th class="px-4 py-2">Nombre de participation</th>
          <th class="px-4 py-2">Première participation</th>
          <th class="px-4 py-2">Date naissance</th>
          <th class="px-4 py-2">Médailles obtenues</th>
          <th class="px-4 py-2">Pays d'origine</th>
          <th class="px-4 py-2">discipline_title</th>
          <th class="px-4 py-2">event_title</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="athlete in filteredAthletes" :key="athlete.athlete_url" class="bg-white text-black border-b">
          <td class="px-4 py-2">
            <a :href="athlete.athlete_url" target="_blank">{{ athlete.athlete_full_name }}</a>
          </td>
          <td class="px-4 py-2">{{ athlete.games_participations }}</td>
          <td class="px-4 py-2">{{ athlete.first_game }}</td>
          <td class="px-4 py-2">{{ athlete.athlete_year_birth }}</td>
          <td class="px-4 py-2">
            <span class="medal"><img src="../assets/gold.png" class="h-4"> <span class="medal-count">{{ parseMedals(athlete.athlete_medals, 'G') }}</span></span>
            <span class="medal"><img src="../assets/silver.png" class="h-4"> <span class="medal-count">{{ parseMedals(athlete.athlete_medals, 'S') }}</span></span>
            <span class="medal"><img src="../assets/bronze.png" class="h-4"> <span class="medal-count">{{ parseMedals(athlete.athlete_medals, 'B') }}</span></span>
          </td>
          <td class="px-4 py-2">{{ athlete.country_name }}</td>
          <td class="px-4 py-2">{{ athlete.discipline_title }}</td>
          <td class="px-4 py-2">{{ athlete.event_title }}</td>
        </tr>
        <tr v-if="filteredAthletes.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="8">No data available</td>
        </tr>
      </tbody>
    </table>

    <div class="flex justify-center my-4">
      <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1" class="mx-2 p-2 border rounded">Précédent</button>
      <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages" class="mx-2 p-2 border rounded">Suivant</button>
    </div>
  </div>
</template>

<script>
import NavbarTab from './../components/NavbarTab.vue';
export default {
  components: {
    NavbarTab
  },
  data() {
    return {
      athletes: [],
      filters: {
        name: '',
        country: '',
        year: '',
        participation: ''
      },
      currentPage: 1,
      perPage: 25,
      totalPages: 0
    };
  },
  computed: {

    filteredAthletes() {
      return this.athletes.filter(athlete => {
        return (!this.filters.name || athlete.athlete_full_name.toLowerCase().includes(this.filters.name.toLowerCase())) &&
               (!this.filters.country || athlete.country_3_letter_code.toLowerCase().includes(this.filters.country.toLowerCase())) &&
               (!this.filters.year || athlete.athlete_year_birth.toString().startsWith(this.filters.year)) &&
               (!this.filters.participation || athlete.games_participations.toString().startsWith(this.filters.participation));
      });
    }
  },
  methods: {
    parseMedals(data, medalType) {
      const regex = new RegExp(`(\\d+)${medalType}`, 'i');
      const match = data.match(regex);
      return match ? match[1] : 0;
    },
    fetchAthletes() {
      const params = new URLSearchParams({
        page: this.currentPage,
        per_page: this.perPage,
        name: this.filters.name,
        country: this.filters.country,
        year: this.filters.year,
        participation: this.filters.participation
      }).toString();
      
      fetch(`http://localhost:5000/athletes?${params}`)
        .then(response => response.json())
        .then(data => {
          this.athletes = data.data;
          this.totalPages = Math.ceil(data.total / this.perPage);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    changePage(page) {
      if (page < 1 || page > this.totalPages) return;
      this.currentPage = page;
      this.fetchAthletes();
    }
  },
  watch: {
    filters: {
      deep: true,
      handler() {
        this.fetchAthletes();
      }
    }
  },
  mounted() {
    this.fetchAthletes();
  }
};
</script>


