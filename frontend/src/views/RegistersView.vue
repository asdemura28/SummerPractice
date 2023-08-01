<template>
  <div class="main-wrapper">
    <div class="main-content" v-if="!loading">
      <b-form class="input-group" inline>
        <b-input type="date" v-model="registry.date_begin"></b-input>
        <b-input type="date" v-model="registry.date_end"></b-input>
        <b-form-select :options="contractorsTitlesOptions"
                       v-model="registry.contractor"></b-form-select>
        <b-form-select class="contract-select" :options="contractsTitlesOptions"
                       v-model="registry.contract"></b-form-select>
      </b-form>
      <b-table :fields="tableFields" :items="tableItems" :bordered="true"></b-table>
      <div v-if="!tableItems.length">
        <h4>Укажите данные для реестра</h4>
      </div>
    </div>
    <div v-else>
      <b-spinner class="loader"></b-spinner>
    </div>
  </div>
</template>

<script lang="ts">
import {Vue, Component} from 'vue-property-decorator';
import ContractorModel from "@/models/Contractor";
import dataStore from "@/store/modules/dataStore";
import ContractModel from "@/models/Contract";
import RecordModel from "@/models/Record";
import _ from "lodash";
import RegistryModel from "@/models/Registry";

@Component({})
export default class RegistersView extends Vue {
  dataStore = dataStore;

  loading = true;

  contractors: Array<ContractorModel> = [];
  contracts: Array<ContractModel> = [];
  records: Array<RecordModel> = [];

  registry: RegistryModel = _.cloneDeep(this.dataStore.newRegistry);

  async created() {
    await this.dataStore.fetchContractors();
    await this.dataStore.fetchContracts();
    await this.dataStore.fetchRecords();
    this.contractors = _.cloneDeep(this.dataStore.contractors);
    this.contracts = _.cloneDeep(this.dataStore.contracts);
    this.records = _.cloneDeep(this.dataStore.records);
    this.loading = false;
  }

  get tableFields() {
    return [
      {key: 'date', label: 'Дата'},
      {key: 'car_number', label: 'Номер машины'},
      {key: 'weight', label: 'Вес'},
      {key: 'driver', label: 'Водитель'}
    ]
  }

  get currentContractors() {
    return this.contractors;
  }

  get currentContracts() {
    return this.contracts;
  }

  get contractorsTitlesOptions() {
    return this.currentContractors.map(item => {
      return {value: item, text: item.title};
    })
  }

  get contractsTitlesOptions() {
    return this.currentContracts.map(item => {
      return {value: item, text: item.number};
    })
  }

  get currentRegistry() {
    return this.registry;
  }

  get filteredRecords() {
    let filteredArray = this.records.filter(x =>{
      return Date.parse(x.date) >= Date.parse(this.currentRegistry.date_begin) &&
      (x.contractor as unknown as number) === this.currentRegistry.contractor.id &&
      (x.contractor as unknown as number) === (this.currentRegistry.contract.contractor as unknown as number)
    })
    if (this.registry.date_end)
      filteredArray = filteredArray.filter(x => Date.parse(x.date) <= Date.parse(this.registry.date_end!))
    return filteredArray;
  }

  get tableItems() {
    return this.filteredRecords.map(item => {
      return {
        date: item.date, car_number: item.car_number, weight: item.weight, driver: item.driver_name
      }
    })
  }

}
</script>

<style scoped lang="stylus">
.main-wrapper
  display flex
  justify-content center
  margin-top 1rem

.input-group
  margin-bottom 1rem

.contract-select
  border-radius var(--bs-border-radius)
  border-top-left-radius 0
  border-bottom-left-radius 0

.loader
  position absolute
  top 50%
  width 5rem
  height 5rem

</style>
