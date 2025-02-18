// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')


import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import the router

const app = createApp(App);
app.use(router); // Make sure Vue Router is used
app.mount('#app'); // Mount the app
