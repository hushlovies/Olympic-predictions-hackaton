import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Athletes from '../views/Athletes.vue';
import Countries from '../views/Countries.vue';
import Medals from '../views/Medals.vue';
import Olympics from '../views/Olympics.vue';
import SummerResults from '../views/SummerResults.vue';
import WinterResults from '../views/WinterResults.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },// ok
  { path: '/athletes', name: 'Athletes', component: Athletes }, // ok
  { path: '/countries', name: 'Countries', component: Countries }, // ok
  { path: '/medals', name: 'Medals', component: Medals },// ok vide
  { path: '/olympics', name: 'Olympics', component: Olympics },// ok
  { path: '/summer-results', name: 'SummerResults', component: SummerResults }, // ok vide
  { path: '/winter-results', name: 'WinterResults', component: WinterResults },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
