<template>
  <div>
    <h1>User List</h1>
    <ul v-if="users.length > 0">
      <li v-for="user in users" :key="user.id">
        {{ user.username }} ({{ user.email }})
      </li>
    </ul>
    <p v-else>Loading users...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [], // Array to store fetched users
    };
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/account/users/');
        this.users = response.data; // Assuming DRF returns a JSON array of users
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
  },
  created() {
    this.fetchUsers(); // Fetch users when the component is created
  },
};
</script>

<style scoped>
h1 {
  color: #42b983;
}
</style>