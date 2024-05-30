<style>
  .navigation{
  margin-bottom: 50px;
  }
</style>
<template>
   <div class="navigation bg-gray-300" >
      <NavbarTab />
    </div>
  <div class="container mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Winter Results</h2>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">Discipline</th>
          <th class="px-4 py-2">Event</th>
          <th class="px-4 py-2">Game</th>
          <th class="px-4 py-2">Participant Type</th>
          <th class="px-4 py-2">Medal Type</th>
          <th class="px-4 py-2">Rank Position</th>
          <th class="px-4 py-2">Country Code</th>
          <th class="px-4 py-2">Athlete URL</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="result in winterResults" :key="result.id_result" class="bg-white  text-black border-b">
          <td class="px-4 py-2">{{ result.discipline_title }}</td>
          <td class="px-4 py-2">{{ result.event_title }}</td>
          <td class="px-4 py-2">{{ result.slug_game }}</td>
          <td class="px-4 py-2">{{ result.participant_type }}</td>
          <td class="px-4 py-2">{{ result.medal_type }}</td>
          <td class="px-4 py-2">{{ result.rank_position }}</td>
          <td class="px-4 py-2">{{ result.country_name }}</td>
          <td class="px-4 py-2">{{ result.athlete_url }}</td>
        </tr>
        <tr v-if="winterResults.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="12">No data available</td>
        </tr>
      </tbody>
    </table>
    <!-- Pagination buttons -->
    <div class="flex justify-center my-4">
      <button @click="goToFirstPage" :disabled="currentPage === 1" class="mx-2 p-2 border rounded">First</button>
      <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1" class="mx-2 p-2 border rounded">Previous</button>
      <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages" class="mx-2 p-2 border rounded">Next</button>
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
      winterResults: [],
      currentPage: 1,
      totalPages: 1,
      perPage: 25,
    };
  },
  mounted() {
    this.fetchResults();
  },
  methods: {
    fetchResults() {
      fetch(`http://localhost:5000/winter_results?page=${this.currentPage}&per_page=${this.perPage}`)
        .then(response => response.json())
        .then(data => {
          if (data.data) {
            this.winterResults = data.data;
            this.totalPages = Math.ceil(data.total / this.perPage);
          }
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    changePage(page) {
      if (page > 0 && page <= this.totalPages) {
        this.currentPage = page;
        this.fetchResults();
      }
    },
    goToFirstPage() {
      this.changePage(1);
    },
  },
};
</script>
