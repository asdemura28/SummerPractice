<template>
  <div>
    <input v-model="idContractor" type="number"/>
    <button @click="getContractor(idContractor)">Click</button>
    <p>{{ contractor }}</p>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import api from '@/store/services/api';

@Component({})
export default class example extends Vue {
  idContractor = 0;
  contractor = 'empty';
  async getContractor(id: number) {
    await api.get(`/api/contractors/${id}`).then(
      response => {
        this.contractor = response.data.title;
      }
    ).catch(
      error => {
        console.log(error.message);
      })
  }
}
</script>


<style scoped lang="stylus">

</style>
