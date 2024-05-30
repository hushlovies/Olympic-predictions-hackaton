<template>
  <div class="container mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Données</h2>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">3 Letter Code</th>
          <th class="px-4 py-2">Country Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="country in countries" :key="country.country_3_letter_code" class="bg-white  text-black border-b">
          <td class="px-4 py-2">{{ country.country_3_letter_code }}</td>
          <td class="px-4 py-2">{{ country.country_name }}</td>
        </tr>
        <tr v-if="countries.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="2">No data available</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      countries: []
    };
  },
  mounted() {
    fetch('http://localhost:5000/data')
      .then(response => response.json())
      .then(data => {
        if (data.data) {
          this.countries = data.data;
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }
};
</script>
