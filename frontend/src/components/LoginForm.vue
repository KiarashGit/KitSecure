<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="credentials.username" required />

      <label for="password">Password:</label>
      <input type="password" id="password" v-model="credentials.password" required />

      <button type="submit">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/', this.credentials);
        const { access, refresh } = response.data;
        
        // Store tokens in localStorage
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        // Redirect to the user list page
        this.$router.push('/users');
      } catch (error) {
        this.error = 'Invalid credentials';
        console.error('Login failed:', error);
      }
    },
  },
};
</script>