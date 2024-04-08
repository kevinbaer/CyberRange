<template>
  <div>
    <h1 class="mb-4">Leaderboard</h1>
    <ul class="list-group" v-if="leaderboardData.length">
      <li class="list-group-item" v-for="(college, index) in sortedLeaderboardData" :key="index">
        <strong>{{ college.name }}</strong>: {{ college.count }} times
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
    setInterval(this.fetchLeaderboardData, 10000);
  },
  computed: {
    sortedLeaderboardData() {
      return this.leaderboardData.slice().sort((a, b) => b.count - a.count);
    }
  },
  methods: {
    async fetchLeaderboardData() {
      try {
        // const response = await axios.get('https://leaderboarded.club/api/challenge_state');
        const response = await axios.get('http://localhost:5000/api/challenge_state');
        const data = response.data;

        // Counting occurrences of each college
        const collegeCounts = {};
        for (const challenge in data) {
          for (const college of data[challenge]) {
            if (!collegeCounts[college]) {
              collegeCounts[college] = 0;
            }
            collegeCounts[college]++;
          }
        }

        // Creating an array of objects with college name and count
        this.leaderboardData = Object.keys(collegeCounts).map(college => ({
          name: college,
          count: collegeCounts[college]
        }));
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    }
  }
};
</script>

