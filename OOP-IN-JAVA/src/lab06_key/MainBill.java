package lab06_key;

import java.time.LocalDate;
import java.time.LocalTime;

public abstract class MainBill {
	//Attribute
		protected String main_TenantName,
		 			   main_BillType;
		protected int main_CurrentmainUnit,
					main_PreviousmainUnit,
					main_RoomNumber;
		
		private electTricBill main_objElect;
		private waterBill main_objWater;
		
				
		//Constructor
		public MainBill(String billType,String name,int curUnit,int preUnit,int roomNumber) {
		   this.main_TenantName = name;
		   this.main_CurrentmainUnit = curUnit;
		   this.main_PreviousmainUnit = preUnit;
		   this.main_RoomNumber =roomNumber;
		   this.main_BillType = billType;
		}
		
	   public MainBill(electTricBill objElect, waterBill objWater,String name,int roomNumber) {
		   this.main_TenantName = name;
		   this.main_RoomNumber =roomNumber;
		   this.main_objElect = objElect;
		   this.main_objWater = objWater;
	  }
		
		//Method
		
		private int checkUnitBill() {
			int unitResult =0;
			
			if(this.main_BillType.contains("Elect")) {
				unitResult = 7;
			}
			else if(this.main_BillType.contains("Water")) {
				unitResult =2;
			}
			return unitResult;
		}
		
		abstract String checkBillName();
		
		public LocalDate displayBillDate() {
			LocalDate localdate = LocalDate.now();
			return localdate;
		}
		public LocalTime displayBillTime() {
			LocalTime localdate = LocalTime.now();
			return localdate;
		}
		
		public int calculatemainUnit() {
			int result =0;
			 result = this.main_CurrentmainUnit- this.main_PreviousmainUnit;
			return result;
		}
		public int calculatemainBill() {
			return calculatemainUnit()*checkUnitBill();
		}
		/// Display Method ////
		public void displayUserDetail() {
			System.out.println("Tenant name: "+this.main_TenantName);
			System.out.println("Room Number: "+this.main_RoomNumber);
		}
		//Optional Bill (Elect/Water Bills)
		public void displayBill() {
			displayUserDetail();
			System.out.println("Date :"+displayBillDate());
			System.out.println("Time :"+displayBillTime());
			System.out.println("Total Unit:"+calculatemainUnit()+"*"+checkUnitBill());
			System.out.println(checkBillName()+calculatemainBill()+" THB");
		}
		//Final Bill//
		public void displayFinalBill() {
			displayUserDetail();
			System.out.println("Date :"+displayBillDate());
			System.out.println("Time :"+displayBillTime());
			
			int resultTotal  = this.main_objElect.calculatemainBill()+this.main_objWater.calculatemainBill();
			System.out.println("ElectBill result: "+this.main_objElect.calculatemainBill());
			System.out.println("WaterBill result: "+this.main_objWater.calculatemainBill());
			System.out.println("Total Bill: "+resultTotal+" THB");
			
			
		}

}
