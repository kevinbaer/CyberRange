<template>
  <div>
    <h1 class="mb-4">Leaderboard</h1>
    <ul class="list-group" v-if="leaderboardData.length">
      <li class="list-group-item" v-for="(team, index) in leaderboardData" :key="index" :class="{ 'striped-row': index % 2 === 0 }">
        <strong>#{{ index + 1 }}</strong>: {{ team[1] }} - {{ team[2] }} points
      </li>
    </ul>
    <div v-else>
      <p class="text-muted">No data available.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      leaderboardData: []
    };
  },
  created() {
    this.fetchLeaderboardData();
    setInterval(this.fetchLeaderboardData, 5000);
  },
  methods: {
    async fetchLeaderboardData() {
      try {
        // const response = await axios.get('https://leaderboarded.club/api/leaderboard');
        const response = await axios.get('http://localhost:5000/api/leaderboard');
        this.leaderboardData = response.data;
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    }
  }
};
</script>

<style scoped>
.striped-row {
  background-color: #f0f0f0; /* Change to your desired background color */
}
</style>
