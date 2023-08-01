<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';

@Component({})
export default class TSIHeader extends Vue {

}
</script>

<template>
  <div class="header p-3 bg-dark text-white">
    <div class="container">
      <div
        class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li>
            <router-link class="nav-link px-3 text-white" :to="{name: 'data'}">
              Данные
            </router-link>
          </li>
          <li>
            <router-link class="nav-link px-3 text-white" :to="{name: 'registers'}">
              Реестры
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped lang="stylus">
.header
  border-bottom 2px solid gray
</style>
