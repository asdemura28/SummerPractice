import ContractorModel from '@/models/Contractor';
import CarNumberModel from "@/models/CarNumber";
import FractionModel from "@/models/Fraction";
export default interface RecordModel {
  id: number;
  date: string;
  contractor: ContractorModel;
  car_number: CarNumberModel;
  driver_name: string;
  fraction: FractionModel;
  weight: number;
}
