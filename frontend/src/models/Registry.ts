import ContractModel from "@/models/Contract";
import ContractorModel from "@/models/Contractor";

export default interface RegistryModel {
  id: number;
  contractor: ContractorModel;
  contract: ContractModel;
  date_begin: string;
  date_end: string | null;
}
