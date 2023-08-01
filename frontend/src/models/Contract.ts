import ContractorModel from '@/models/Contractor';
export default interface ContractModel {
  id: number;
  number: string;
  date: string;
  contractor: ContractorModel;
}
