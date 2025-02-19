<!-- <template>
  <div id="app">
    <UserList />
  </div>
</template>

<script>
import UserList from './components/UserList.vue';

export default {
  components: {
    UserList,
  },
};
</script> -->





<template>
  <div id="app">
    <router-view />  
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
/* Add styles if needed */
</style>
