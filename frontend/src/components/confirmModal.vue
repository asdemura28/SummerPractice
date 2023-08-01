<template>
  <div>
    <b-modal v-model="modalVisible" @hide="hideModal" centered hide-footer title="Вы уверены?">
      <p>{{ text }}</p>
      <div class="action-btns">
      <b-button class="btn-danger" @click="approve">Удалить</b-button>
      <b-button class="btn-secondary" @click="hideModal">Отменить</b-button>
    </div>
    </b-modal>
  </div>
</template>

<script lang="ts">
import {Vue, Component, Prop, Watch} from 'vue-property-decorator';

@Component({})
export default class confirmModal extends Vue {
  @Prop({required: true}) modalTrigger!: number;
  @Prop({required: true}) text!: string;
  // eslint-disable-next-line @typescript-eslint/ban-types
  @Prop({required: true}) approveHandler!: Function;

  modalVisible = false;

  @Watch('modalTrigger')
  showModal() {
    this.modalVisible = true;
  }

  hideModal() {
    this.modalVisible = false;
  }

  async approve() {
    await this.approveHandler();
    this.hideModal();
  }
}
</script>

<style scoped lang="stylus">
.action-btns
  display flex
  justify-content flex-end
  gap 0.5rem
</style>
