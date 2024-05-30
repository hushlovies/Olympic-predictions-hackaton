<template>
  <div class="container mx-auto mt-10">
    <h1>Miscellaneous HERE</h1>
    <h2 class="text-2xl font-bold mb-4">Countries</h2>
    
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">Country Name</th>
          <th class="px-4 py-2">3 Letter Code</th>
          <th class="px-4 py-2">Gold Medal</th>
          <th class="px-4 py-2">Silver Medal</th>
          <th class="px-4 py-2">Bronze Medal</th>
          <th class="px-4 py-2">No. of ahtletes</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="country in countries" :key="country.country_3_letter_code" class="bg-white  text-black border-b">
          <td class="px-4 py-2">{{ country.country_name }}</td>
          <td class="px-4 py-2">{{ country.country_3_letter_code }}</td>
          <td class="px-4 py-2">{{ country.total_gold }}</td>
          <td class="px-4 py-2">{{ country.total_silver }}</td>
          <td class="px-4 py-2">{{ country.total_bronze }}</td>
          <td class="px-4 py-2">{{ country.athlete_count }}</td>
        </tr>
        <tr v-if="countries.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="2">No data available</td>
        </tr>
      </tbody>
    </table>
    <!-- Ajout des boutons de pagination ici -->
    <div class="flex justify-center my-4">
  <button @click="goToFirstPage" :disabled="currentPage === 1" class="mx-2 p-2 border rounded">First</button>
  <button @click="changePage(currentPage - 1)" :disabled="currentPage <= 1" class="mx-2 p-2 border rounded">Previous</button>
  <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages" class="mx-2 p-2 border rounded">Next</button>
</div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      countries: [],
      currentPage: 1,
      perPage: 25,
      totalPages: 0,
    };
  },
  methods: {
    fetchCountries() {
      const params = new URLSearchParams({
        page: this.currentPage,
        per_page: this.perPage,
      }).toString();
      
      fetch(`http://localhost:5000/countries?${params}`)
        .then((response) => response.json())
        .then((data) => {
          if (data.data) {
            this.countries = data.data;
            this.totalPages = Math.ceil(data.total / this.perPage); // Ensure your backend returns the total count
          } else {
            this.countries = [];
            this.totalPages = 0;
          }
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
          this.countries = [];
          this.totalPages = 0;
        });
    },
    changePage(page) {
      if (page < 1 || page > this.totalPages) return;
      this.currentPage = page;
      this.fetchCountries();
    },
    goToFirstPage() {
      if (this.currentPage !== 1) {
        this.currentPage = 1;
        this.fetchCountries();
      }
    }
  },
  mounted() {
    this.fetchCountries();
  },
  watch: {
    perPage(newPerPage, oldPerPage) {
      // Reset current page when changing items per page
      if (newPerPage !== oldPerPage) {
        this.currentPage = 1;
        this.fetchCountries();
      }
    },
  },
};
</script>
