<template>
  <div id="app">
    <TSIHeader/>
    <main>
      <router-view/>
    </main>
    <footer class="bg-dark d-flex flex-wrap justify-content-between align-items-center py-3">
      <div class="container">
        <div class="text-white col-md-4 d-flex align-items-center">
          <span class="mb-3 mb-md-0">© Yasuhiro & 13b Co. 2023 </span>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import TSIHeader from "@/components/TSIHeader.vue";
</script>

<style lang="stylus">
#app
  height 100%
  display flex
  flex-direction column
  font-family: var(--bs-font-sans-serif);
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50

html
  height 100vh

body
  height 100%

main
  flex 1

footer
  border-top 2px solid gray
  width 100%
  bottom 0
</style>
