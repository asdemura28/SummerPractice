<template>
  <div class="data">
    <confirm-modal :modal-trigger="modalTrigger"
                   :text="approvedText"
                   :approve-handler="deleteObject"/>
    <div class="left-data">
      <div class="left-side-container d-flex flex-column flex-shrink-0 text-white bg-dark">
        <button type="button" class="select-btn btn btn-secondary"
                @click="selectType('Контрагенты')">
          Контрагенты
        </button>
        <button type="button" class="select-btn btn btn-secondary"
                @click="selectType('Контракты')">
          Контракты
        </button>
        <button type="button" class="select-btn btn btn-secondary"
                @click="selectType('Номера машин')">
          Номера машин
        </button>
        <button type="button" class="select-btn btn btn-secondary"
                @click="selectType('Фракции')">
          Фракции
        </button>
        <button type="button" class="select-btn btn btn-secondary"
                @click="selectType('Учет')">
          Учет
        </button>
      </div>
    </div>
    <div class="right-data">
      <div class="right-side-container" :style="isRecordsSelected ? 'width: 1300px' : ''">
        <h3 class="data-title">{{ selectedType }}</h3>
        <div v-if="!loading">
          <div class="data-container" v-if="isContractorsSelected">
            <div class="data-input">
              <div class="input-group" v-for="contractor in currentContractors"
                   :key="contractor.id">
                <input type="text" class="form-control" v-model="contractor.title">
                <button class="btn btn-success" type="button"
                        :disabled="!isContractorChanged(contractor.id)"
                        @click="editContractor(contractor)">
                  Изменить
                </button>
                <button class="btn btn-danger" type="button"
                        @click="showConfirmModal(contractor, 'контрагента')">
                  Удалить
                </button>
              </div>
              <div class="create-input-group" v-if="contractorCreating">
                <div class="input-group">
                  <input type="text" class="form-control" v-model="newContractor.title">
                  <button class="btn btn-success" type="button"
                          :disabled="!newContractor.title.length"
                          @click="addContractor(newContractor)">
                    Добавить
                  </button>
                  <button class="btn btn-danger" type="button" @click="cancelContractorAddition">
                    Удалить
                  </button>
                </div>
              </div>
              <div class="add-btn-container" v-if="!contractorCreating">
                <button type="button" class="btn btn-primary"
                        @click="createNewContractor">
                  Добавить
                </button>
              </div>
            </div>
          </div>

          <div class="data-container" v-if="isContractsSelected">
            <div class="data-input">
              <b-form inline class="input-group" v-for="contract in currentContracts"
                      :key="contract.id">
                <b-form-input type="date" v-model="contract.date"></b-form-input>
                <b-form-input type="text" v-model="contract.number"></b-form-input>
                <b-form-select :options="contractorsTitlesOptions"
                               v-model="contract.contractor"></b-form-select>
                <b-button class="btn btn-success" type="button"
                          :disabled="!isContractChanged(contract.id)"
                          @click="editContract(contract)">
                  Изменить
                </b-button>
                <button class="btn btn-danger" type="button"
                        @click="showConfirmModal(contract, 'контракт')">
                  Удалить
                </button>
              </b-form>
              <div class="create-input-group" v-if="contractCreating">
                <b-form inline class="input-group">
                  <b-form-input type="date" v-model="newContract.date"></b-form-input>
                  <b-form-input type="text" v-model="newContract.number"></b-form-input>
                  <b-form-select :options="contractorsTitlesOptions"
                                 v-model="newContract.contractor.id">
                    <!--                   <b-form-select-option :value="dataStore.newContractor">-->
                    <!--                     Please select an option-->
                    <!--                   </b-form-select-option>-->
                  </b-form-select>
                  <b-button class="btn btn-success" type="button"
                            :disabled="!isEmptyContractFields"
                            @click="addContract(newContract)">
                    Добавить
                  </b-button>
                  <b-button class="btn btn-danger" type="button" @click="cancelContractAddition">
                    Удалить
                  </b-button>
                </b-form>
              </div>
              <div class="add-btn-container" v-if="!contractCreating">
                <button type="button" class="btn btn-primary"
                        @click="createNewContract">
                  Добавить
                </button>
              </div>
            </div>
          </div>

          <div class="data-container" v-if="isCarNumbersSelected">
            <div class="data-input">
              <div class="input-group" v-for="car_number in currentCarNumbers" :key="car_number.id">
                <input type="text" class="form-control" v-model="car_number.number">
                <button class="btn btn-success" type="button"
                        :disabled="!isCarNumberChanged(car_number.id)"
                        @click="editCarNumber(car_number)">
                  Изменить
                </button>
                <button class="btn btn-danger" type="button"
                        @click="showConfirmModal(car_number, 'номер машины')">
                  Удалить
                </button>
              </div>
              <div class="create-input-group" v-if="carNumberCreating">
                <div class="input-group">
                  <input type="text" class="form-control" v-model="newCarNumber.number">
                  <button class="btn btn-success" type="button"
                          :disabled="!newCarNumber.number.length"
                          @click="addCarNumber(newCarNumber)">
                    Добавить
                  </button>
                  <button class="btn btn-danger" type="button" @click="cancelCarNumberAddition">
                    Удалить
                  </button>
                </div>
              </div>
              <div class="add-btn-container" v-if="!carNumberCreating">
                <button type="button" class="btn btn-primary"
                        @click="createNewCarNumber">
                  Добавить
                </button>
              </div>
            </div>
          </div>

          <div class="data-container" v-if="isFractionsSelected">
            <div class="data-input">
              <div class="input-group" v-for="fraction in currentFractions" :key="fraction.id">
                <input type="text" class="form-control" v-model="fraction.fraction">
                <button class="btn btn-success" type="button"
                        :disabled="!isFractionChanged(fraction.id)"
                        @click="editFraction(fraction)">
                  Изменить
                </button>
                <button class="btn btn-danger" type="button"
                        @click="showConfirmModal(fraction, 'фракцию')">
                  Удалить
                </button>
              </div>
              <div class="create-input-group" v-if="fractionCreating">
                <div class="input-group">
                  <input type="text" class="form-control" v-model="newFraction.fraction">
                  <button class="btn btn-success" type="button"
                          :disabled="!newFraction.fraction.length"
                          @click="addFraction(newFraction)">
                    Добавить
                  </button>
                  <button class="btn btn-danger" type="button" @click="cancelFractionAddition">
                    Удалить
                  </button>
                </div>
              </div>
              <div class="add-btn-container" v-if="!fractionCreating">
                <button type="button" class="btn btn-primary"
                        @click="createNewFraction">
                  Добавить
                </button>
              </div>
            </div>
          </div>

          <div class="data-container" v-if="isRecordsSelected">
            <div class="data-input">
              <b-form inline class="input-group" v-for="record in currentRecords"
                      :key="record.id">
                <b-form-input type="date" v-model="record.date"></b-form-input>
                <b-form-select :options="contractorsTitlesOptions"
                               v-model="record.contractor"></b-form-select>
                <b-form-select :options="carNumbersTitlesOptions"
                               v-model="record.car_number"></b-form-select>
                <b-form-input type="text" v-model="record.driver_name"></b-form-input>
                <b-form-input type="text" v-model="record.weight"></b-form-input>
                <b-form-select :options="fractionsTitlesOptions"
                               v-model="record.fraction"></b-form-select>
                <b-button class="btn btn-success" type="button"
                          :disabled="!isRecordChanged(record.id)"
                          @click="editRecord(record)">
                  Изменить
                </b-button>
                <button class="btn btn-danger" type="button"
                        @click="showConfirmModal(record, 'учет')">
                  Удалить
                </button>
              </b-form>
              <div class="create-input-group" v-if="recordCreating">
                <b-form inline class="input-group">
                  <b-form-input type="date" v-model="newRecord.date"></b-form-input>
                  <b-form-select :options="contractorsTitlesOptions"
                                 v-model="newRecord.contractor.id"></b-form-select>
                  <b-form-select :options="carNumbersTitlesOptions"
                                 v-model="newRecord.car_number.id"></b-form-select>
                  <b-form-input type="text" v-model="newRecord.driver_name"></b-form-input>
                  <b-form-input type="text" v-model="newRecord.weight"></b-form-input>
                  <b-form-select :options="fractionsTitlesOptions"
                                 v-model="newRecord.fraction.id"></b-form-select>
                  <b-button class="btn btn-success" type="button"
                            :disabled="!isEmptyRecordFields"
                            @click="addRecord(newRecord)">
                    Добавить
                  </b-button>
                  <b-button class="btn btn-danger" type="button" @click="cancelRecordAddition">
                    Удалить
                  </b-button>
                </b-form>
              </div>
              <div class="add-btn-container" v-if="!recordCreating">
                <button type="button" class="btn btn-primary"
                        @click="createNewRecord">
                  Добавить
                </button>
              </div>
            </div>
          </div>
        </div>
        <div v-else>
        <b-spinner class="loader"></b-spinner>
      </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator'
import ContractorModel from "@/models/Contractor";
import ContractModel from "@/models/Contract";
import FractionModel from "@/models/Fraction";
import CarNumberModel from "@/models/CarNumber";
import dataStore from "@/store/modules/dataStore";
import _ from "lodash";
import api from "@/store/services/api";
import ConfirmModal from "@/components/confirmModal.vue";
import RecordModel from "@/models/Record";

@Component({
  components: {ConfirmModal}
})
export default class DataView extends Vue {
  selectedType = 'Контрагенты';
  loading = true;
  modalTrigger = 0;
  approvedText = '';

  dataStore = dataStore;

  contractorCreating = false;
  contractCreating = false;
  fractionCreating = false;
  carNumberCreating = false;
  recordCreating = false;

  contractorDeletingId = NaN;
  contractDeletingId = NaN;
  fractionDeletingId = NaN;
  carNumberDeletingId = NaN;
  recordDeletingId = NaN;

  contractors: Array<ContractorModel> = [];
  contracts: Array<ContractModel> = [];
  fractions: Array<FractionModel> = [];
  carNumbers: Array<CarNumberModel> = [];
  records: Array<RecordModel> = [];

  newContractor: ContractorModel = _.cloneDeep(this.dataStore.newContractor);
  newContract: ContractModel = _.cloneDeep(this.dataStore.newContract);
  newFraction: FractionModel = _.cloneDeep(this.dataStore.newFraction);
  newCarNumber: CarNumberModel = _.cloneDeep(this.dataStore.newCarNumber);
  newRecord: RecordModel = _.cloneDeep(this.dataStore.newRecord);

  async created() {
    await this.dataStore.fetchContractors();
    await this.dataStore.fetchContracts();
    await this.dataStore.fetchFractions();
    await this.dataStore.fetchCarNumbers();
    await this.dataStore.fetchRecords();
    this.contractors = _.cloneDeep(this.dataStore.contractors);
    this.contracts = _.cloneDeep(this.dataStore.contracts);
    this.fractions = _.cloneDeep(this.dataStore.fractions);
    this.carNumbers = _.cloneDeep(this.dataStore.car_numbers);
    this.records = _.cloneDeep(this.dataStore.records);
    this.loading = false;
  }

  async editContractor(contractor: ContractorModel) {
    await api.put(`/api/contractors/${contractor.id}/`, contractor)
      .then(() => {
        this.dataStore.setContractors(this.currentContractors);
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async editContract(contract: ContractModel) {
    await api.put(`/api/contracts/${contract.id}/`, contract)
      .then(() => {
        this.dataStore.setContracts(this.currentContracts);
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async editFraction(fraction: FractionModel) {
    await api.put(`/api/fractions/${fraction.id}/`, fraction)
      .then(() => {
        this.dataStore.setFractions(this.currentFractions);
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async editCarNumber(car_number: CarNumberModel) {
    await api.put(`/api/carnumbers/${car_number.id}/`, car_number)
      .then(() => {
        this.dataStore.setCarNumbers(this.currentCarNumbers);
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async editRecord(record: RecordModel) {
    await api.put(`/api/records/${record.id}/`, record)
      .then(() => {
        this.dataStore.setRecords(this.currentRecords);
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async addContractor(contractor: ContractorModel) {
    await api.post('/api/contractors/', contractor)
      .then(response => {
        this.contractors.push(response.data as ContractorModel);
        this.dataStore.setContractors(this.currentContractors);
        this.newContractor.title = "";
        this.contractorCreating = false;
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async addContract(contract: ContractModel) {
    await api.post('/api/contracts/', {...contract, contractor: contract.contractor.id})
      .then(response => {
        this.contracts.push(response.data as ContractModel);
        this.dataStore.setContracts(this.currentContracts);
        this.newContract = _.cloneDeep(this.dataStore.newContract);
        this.contractCreating = false;
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async addCarNumber(car_number: CarNumberModel) {
    await api.post('/api/carnumbers/', car_number)
      .then(response => {
        this.carNumbers.push(response.data as CarNumberModel);
        this.dataStore.setCarNumbers(this.currentCarNumbers);
        this.newCarNumber = _.cloneDeep(this.dataStore.newCarNumber);
        this.carNumberCreating = false;
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async addFraction(fraction: FractionModel) {
    await api.post('/api/fractions/', fraction)
      .then(response => {
        this.fractions.push(response.data as FractionModel);
        this.dataStore.setFractions(this.currentFractions);
        this.newFraction = _.cloneDeep(this.dataStore.newFraction);
        this.fractionCreating = false;
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async addRecord(record: RecordModel) {
    await api.post('/api/records/', {
      ...record,
      contractor: record.contractor.id,
      car_number: record.car_number.id,
      fraction: record.fraction.id,
    })
      .then(response => {
        this.records.push(response.data as RecordModel);
        this.dataStore.setRecords(this.currentRecords);
        this.newRecord = _.cloneDeep(this.dataStore.newRecord);
        this.recordCreating = false;
      })
      .catch(error => {
        console.log(error.message);
      })
  }

  async deleteObject() {
    if (!_.isNaN(this.contractorDeletingId)) {
      await api.delete(`/api/contractors/${this.contractorDeletingId}`)
        .then(() => {
          this.contractors = this.contractors.filter(x => x.id !== this.contractorDeletingId);
          this.contractorDeletingId = NaN;
        })
        .catch(error => {
          console.log(error.message);
        })
    } else if (!_.isNaN(this.contractDeletingId)) {
      await api.delete(`/api/contracts/${this.contractDeletingId}`)
        .then(() => {
          this.contracts = this.contracts.filter(x => x.id !== this.contractDeletingId);
          this.contractDeletingId = NaN;
        })
        .catch(error => {
          console.log(error.message);
        })
    } else if (!_.isNaN(this.fractionDeletingId)) {
      await api.delete(`/api/fractions/${this.fractionDeletingId}`)
        .then(() => {
          this.fractions = this.fractions.filter(x => x.id !== this.fractionDeletingId);
          this.fractionDeletingId = NaN;
        })
        .catch(error => {
          console.log(error.message);
        })
    } else if (!_.isNaN(this.carNumberDeletingId)) {
      await api.delete(`/api/carnumbers/${this.carNumberDeletingId}`)
        .then(() => {
          this.carNumbers = this.carNumbers.filter(x => x.id !== this.carNumberDeletingId);
          this.carNumberDeletingId = NaN;
        })
        .catch(error => {
          console.log(error.message);
        })
    } else {
      await api.delete(`/api/records/${this.recordDeletingId}`)
        .then(() => {
          this.records = this.records.filter(x => x.id !== this.recordDeletingId);
          this.recordDeletingId = NaN;
        })
        .catch(error => {
          console.log(error.message);
        })
    }
  }

  showConfirmModal(
    deletingObject: ContractorModel | ContractModel | FractionModel | CarNumberModel | RecordModel,
    objectTitle: string) {
    this.contractorDeletingId = NaN;
    this.contractDeletingId = NaN;
    this.fractionDeletingId = NaN;
    this.carNumberDeletingId = NaN;
    this.recordDeletingId = NaN;
    if (objectTitle == 'контрагента') {
      this.contractorDeletingId = deletingObject.id
      this.approvedText = `Удалить контрагента: ${(deletingObject as ContractorModel).title}`;
    } else if (objectTitle == 'контракт') {
      this.contractDeletingId = deletingObject.id;
      this.approvedText = `Удалить контракт: ${(deletingObject as ContractModel).number}`;
    } else if (objectTitle == 'фракцию') {
      this.fractionDeletingId = deletingObject.id;
      this.approvedText = `Удалить фракцию: ${(deletingObject as FractionModel).fraction}`;
    } else if (objectTitle == 'номер машины') {
      this.carNumberDeletingId = deletingObject.id;
      this.approvedText = `Удалить номер машины: ${(deletingObject as CarNumberModel).number}`;
    } else {
      this.recordDeletingId = deletingObject.id;
      this.approvedText = `Удалить учет за: ${(deletingObject as RecordModel).date}`;
    }
    this.modalTrigger++;
  }


  createNewContractor() {
    this.contractorCreating = true;
  }

  createNewContract() {
    this.contractCreating = true;
  }

  createNewCarNumber() {
    this.carNumberCreating = true;
  }

  createNewFraction() {
    this.fractionCreating = true;
  }

  createNewRecord() {
    this.recordCreating = true;
  }

  cancelContractorAddition() {
    this.newContractor.title = "";
    this.contractorCreating = false;
  }

  cancelContractAddition() {
    this.newContract = _.cloneDeep(this.dataStore.newContract);
    this.contractCreating = false;
  }

  cancelCarNumberAddition() {
    this.newCarNumber.number = "";
    this.carNumberCreating = false;
  }

  cancelFractionAddition() {
    this.newFraction.fraction = "";
    this.fractionCreating = false;
  }

  cancelRecordAddition() {
    this.newRecord = _.cloneDeep(this.dataStore.newRecord);
    this.recordCreating = false;
  }

  selectType(type_to_select: string) {
    this.selectedType = type_to_select;
  }

  isContractorChanged(id: number) {
    return !_.isEqual(this.currentContractors.filter(x => x.id === id)[0], this.dataStore.contractors.filter(x => x.id === id)[0])
  }

  isContractChanged(id: number) {
    return !_.isEqual(this.currentContracts.filter(x => x.id === id)[0], this.dataStore.contracts.filter(x => x.id === id)[0])
  }

  isFractionChanged(id: number) {
    return !_.isEqual(this.currentFractions.filter(x => x.id === id)[0], this.dataStore.fractions.filter(x => x.id === id)[0])
  }

  isCarNumberChanged(id: number) {
    return !_.isEqual(this.currentCarNumbers.filter(x => x.id === id)[0], this.dataStore.car_numbers.filter(x => x.id === id)[0])
  }

  isRecordChanged(id: number) {
    return !_.isEqual(this.currentRecords.filter(x => x.id === id)[0], this.dataStore.records.filter(x => x.id === id)[0])
  }

  get contractorsTitlesOptions() {
    return this.currentContractors.map(item => {
      return {value: item.id, text: item.title};
    })
  }

  get carNumbersTitlesOptions() {
    return this.currentCarNumbers.map(item => {
      return {value: item.id, text: item.number};
    })
  }

  get fractionsTitlesOptions() {
    return this.currentFractions.map(item => {
      return {value: item.id, text: item.fraction};
    })
  }

  get isEmptyContractFields() {
    return (this.newContract.contractor.id && this.newContract.number.length
      && this.newContract.date.length);
  }

  get isEmptyRecordFields() {
    return this.newRecord.fraction.id &&
      this.newRecord.car_number.id &&
      this.newRecord.weight &&
      this.newRecord.date.length &&
      this.newRecord.driver_name.length &&
      this.newRecord.contractor.id;
  }

  get currentContractors() {
    return this.contractors;
  }

  get currentContracts() {
    return this.contracts;
  }

  get currentFractions() {
    return this.fractions;
  }

  get currentCarNumbers() {
    return this.carNumbers;
  }

  get currentRecords() {
    return this.records;
  }

  get isContractorsSelected() {
    return this.selectedType === 'Контрагенты';
  }

  get isContractsSelected() {
    return this.selectedType === 'Контракты';
  }

  get isFractionsSelected() {
    return this.selectedType === 'Фракции';
  }

  get isCarNumbersSelected() {
    return this.selectedType === 'Номера машин';
  }

  get isRecordsSelected() {
    return this.selectedType === 'Учет';
  }
}
</script>

<style lang="stylus" scoped>
.data
  display flex
  flex-direction row
  height 100%

.data-title
  border-bottom 2px solid gray
  margin-top 0.5rem
  padding-bottom 0.5rem

.data-container
  padding-bottom 1rem

.data-input
  margin-left 1rem
  margin-right 1rem

.input-group
  margin-top 1rem

.right-data
  display flex
  justify-content center
  width 100%

.right-side-container
  height fit-content
  min-height 500px
  border 4px solid gray
  border-radius 15px
  margin-top 3rem
  margin-bottom 3rem
  width 1000px

.add-btn-container
  margin-top 1rem

.left-side-container
  height 100%
  width 250px
  align-items center
  gap 2rem
  padding 3rem

.select-btn
  cursor pointer
  margin-top 1rem

.loader
  width 5rem
  height 5rem

</style>
