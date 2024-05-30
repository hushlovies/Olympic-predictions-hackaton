<template>
  <div class="container mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Winter Results</h2>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">ID</th>
          <th class="px-4 py-2">Discipline</th>
          <th class="px-4 py-2">Event</th>
          <th class="px-4 py-2">Game</th>
          <th class="px-4 py-2">Participant Type</th>
          <th class="px-4 py-2">Medal Type</th>
          <th class="px-4 py-2">Rank Equal</th>
          <th class="px-4 py-2">Rank Position</th>
          <th class="px-4 py-2">Country Code</th>
          <th class="px-4 py-2">Athlete URL</th>
          <th class="px-4 py-2">Value Unit</th>
          <th class="px-4 py-2">Value Type</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="result in winterResults" :key="result.id_result" class="bg-white  text-black border-b">
          <td class="px-4 py-2">{{ result.id_result }}</td>
          <td class="px-4 py-2">{{ result.discipline_title }}</td>
          <td class="px-4 py-2">{{ result.event_title }}</td>
          <td class="px-4 py-2">{{ result.slug_game }}</td>
          <td class="px-4 py-2">{{ result.participant_type }}</td>
          <td class="px-4 py-2">{{ result.medal_type }}</td>
          <td class="px-4 py-2">{{ result.rank_equal }}</td>
          <td class="px-4 py-2">{{ result.rank_position }}</td>
          <td class="px-4 py-2">{{ result.country_3_letter_code }}</td>
          <td class="px-4 py-2">{{ result.athlete_url }}</td>
          <td class="px-4 py-2">{{ result.value_unit }}</td>
          <td class="px-4 py-2">{{ result.value_type }}</td>
        </tr>
        <tr v-if="winterResults.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="12">No data available</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      winterResults: [],
    };
  },
  mounted() {
    fetch('http://localhost:5000/winter_results')
      .then((response) => response.json())
      .then((data) => {
        if (data.data) {
          this.winterResults = data.data;
        }
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>
