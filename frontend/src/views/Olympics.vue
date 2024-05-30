<template>
  <div class="container mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Olympics</h2>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">Slug</th>
          <th class="px-4 py-2">End Date</th>
          <th class="px-4 py-2">Start Date</th>
          <th class="px-4 py-2">Location</th>
          <th class="px-4 py-2">Name</th>
          <th class="px-4 py-2">Year</th>
          <th class="px-4 py-2">Season</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="olympic in olympics" :key="olympic.game_slug" class="bg-white  text-black border-b">
          <td class="px-4 py-2">{{ olympic.game_slug }}</td>
          <td class="px-4 py-2">{{ olympic.game_end_date }}</td>
          <td class="px-4 py-2">{{ olympic.game_start_date }}</td>
          <td class="px-4 py-2">{{ olympic.game_location }}</td>
          <td class="px-4 py-2">{{ olympic.game_name }}</td>
          <td class="px-4 py-2">{{ olympic.game_year }}</td>
          <td class="px-4 py-2">{{ olympic.game_season }}</td>
        </tr>
        <tr v-if="olympics.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="7">No data available</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      olympics: [],
    };
  },
  mounted() {
    fetch('http://localhost:5000/olympics')
      .then((response) => response.json())
      .then((data) => {
        if (data.data) {
          this.olympics = data.data;
        }
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>
