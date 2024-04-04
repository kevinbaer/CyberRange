<template>
  <h1 class="mb-4">Leaderboard</h1>
    <ul class="list-group" v-if="leaderboardData.length">
    <li class=list-group-item v-for="(team, index) in leaderboardData" :key="index">
      <strong>#{{ index + 1 }}</strong>: {{ team[1] }} - {{ team[2] }} points
    </li>
  </ul>
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
        const response = await axios.get('https://leaderboarded.club/api/leaderboard');
        this.leaderboardData = response.data;
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    }
  }
};
</script>

<style scoped>
</style>
