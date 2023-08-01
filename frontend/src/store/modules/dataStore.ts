import ContractorModel from "@/models/Contractor";
import store from '@/store';
import api from '@/store/services/api'
import {Action, getModule, Module, Mutation, VuexModule} from 'vuex-module-decorators';
import ContractModel from "@/models/Contract";
import FractionModel from "@/models/Fraction";
import CarNumberModel from "@/models/CarNumber";
import RecordModel from "@/models/Record";
import RegistryModel from "@/models/Registry";

@Module({namespaced: true, name: 'data', store, dynamic: true})
class DataModule extends VuexModule {
  contractors: Array<ContractorModel> = [];
  contracts: Array<ContractModel> = [];
  fractions: Array<FractionModel> = [];
  car_numbers: Array<CarNumberModel> = [];
  records: Array<RecordModel> = [];

  get newContractor(): ContractorModel {
    return {id: NaN, title: ''};
  }

  get newContract(): ContractModel {
    return {id: NaN, number: '', date: '', contractor: this.newContractor};
  }

  get newFraction(): FractionModel {
    return {id: NaN, fraction: ''};
  }

  get newCarNumber(): CarNumberModel {
    return {id: NaN, number: ''};
  }

  get newRecord(): RecordModel {
    return {
      id: NaN,
      date: '',
      contractor: this.newContractor,
      fraction: this.newFraction,
      car_number: this.newCarNumber,
      driver_name: '',
      weight: 0
    };
  }

  get newRegistry(): RegistryModel {
    return {
      id: NaN,
      contract: this.newContract,
      contractor: this.newContractor,
      date_begin: '',
      date_end: ''
    };
  }

  @Mutation
  setContractors(payload: Array<ContractorModel>) {
    this.contractors = payload;
  }

  @Mutation
  setContracts(payload: Array<ContractModel>) {
    this.contracts = payload;
  }

  @Mutation
  setFractions(payload: Array<FractionModel>) {
    this.fractions = payload;
  }

  @Mutation
  setCarNumbers(payload: Array<CarNumberModel>) {
    this.car_numbers = payload;
  }

  @Mutation
  setRecords(payload: Array<RecordModel>) {
    this.records = payload;
  }

  @Action
  async fetchContractors() {
    await api.get('/api/contractors/')
      .then(response => {
          this.setContractors(response.data as Array<ContractorModel>);
        }
      )
      .catch(error => {
        console.log(error.message);
      })
  }

  @Action
  async fetchContracts() {
    await api.get('/api/contracts/')
      .then(response => {
          this.setContracts(response.data as Array<ContractModel>);
        }
      )
      .catch(error => {
        console.log(error.message);
      })
  }

  @Action
  async fetchFractions() {
    await api.get('/api/fractions/')
      .then(response => {
          this.setFractions(response.data as Array<FractionModel>);
        }
      )
      .catch(error => {
        console.log(error.message);
      })
  }

  @Action
  async fetchCarNumbers() {
    await api.get('/api/carnumbers/')
      .then(response => {
          this.setCarNumbers(response.data as Array<CarNumberModel>);
        }
      )
      .catch(error => {
        console.log(error.message);
      })
  }

  @Action
  async fetchRecords() {
    await api.get('/api/records/')
      .then(response => {
          this.setRecords(response.data as Array<RecordModel>);
        }
      )
      .catch(error => {
        console.log(error.message);
      })
  }
}

export default getModule(DataModule);
