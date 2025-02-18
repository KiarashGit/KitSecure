import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from './components/LoginForm.vue';
import UserList from './components/UserList.vue';
import NotFound from './components/NotFound.vue'; // Optional, for 404 pages

const routes = [
  { path: '/', redirect: '/login' }, // Redirect root to /login
  { path: '/login', component: LoginForm },
  { path: '/users', component: UserList },
  { path: '/:pathMatch(.*)*', component: NotFound } // Catch-all route
];

const router = createRouter({
  history: createWebHistory(), // Enables history mode (no # in URL)
  routes,
});

export default router;
