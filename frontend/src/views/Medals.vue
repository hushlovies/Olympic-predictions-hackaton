<template>
  <div class="container mx-auto mt-10">
    <h2 class="text-2xl font-bold mb-4">Medals</h2>
    <table class="min-w-full table-auto">
      <thead class="bg-gray-800 text-white">
        <tr>
          <th class="px-4 py-2">ID</th>
          <th class="px-4 py-2">Discipline</th>
          <th class="px-4 py-2">Game</th>
          <th class="px-4 py-2">Event</th>
          <th class="px-4 py-2">Gender</th>
          <th class="px-4 py-2">Medal Type</th>
          <th class="px-4 py-2">Participant Type</th>
          <th class="px-4 py-2">Athlete URL</th>
          <th class="px-4 py-2">Country Code</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="medal in medals" :key="medal.id_medal" class="bg-white border-b">
          <td class="px-4 py-2">{{ medal.id_medal }}</td>
          <td class="px-4 py-2">{{ medal.discipline_title }}</td>
          <td class="px-4 py-2">{{ medal.slug_game }}</td>
          <td class="px-4 py-2">{{ medal.event_title }}</td>
          <td class="px-4 py-2">{{ medal.event_gender }}</td>
          <td class="px-4 py-2">{{ medal.medal_type }}</td>
          <td class="px-4 py-2">{{ medal.participant_type }}</td>
          <td class="px-4 py-2">{{ medal.athlete_url }}</td>
          <td class="px-4 py-2">{{ medal.country_3_letter_code }}</td>
        </tr>
        <tr v-if="medals.length === 0" class="bg-white border-b">
          <td class="px-4 py-2" colspan="9">No data available</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      medals: [],
    };
  },
  mounted() {
    fetch('http://localhost:5000/medals')
      .then((response) => response.json())
      .then((data) => {
        if (data.data) {
          this.medals = data.data;
        }
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>
