import { createRouter, createWebHashHistory } from 'vue-router';
import LoginForm from './components/LoginForm.vue';
import UserList from './components/UserList.vue';

const routes = [
  { path: '/', redirect: '/login' }, 
  { path: '/login', component: LoginForm },
  { path: '/users', component: UserList },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router;