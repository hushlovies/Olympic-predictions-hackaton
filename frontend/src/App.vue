<template>
  <div>
    <Navbar />
    <NavbarTab />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import NavbarTab from './components/NavbarTab.vue';
import Footer from './components/Footer.vue';

export default {
  components: {
    Navbar,
    NavbarTab,
    Footer
  }
}
</script>
