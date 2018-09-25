package lab06_key;

import java.time.LocalDate;
import java.time.LocalTime;

public class electTricBill extends MainBill {

	public electTricBill(String billType, String name, int curUnit, int preUnit, int roomNumber) {
		super(billType, name, curUnit, preUnit, roomNumber);
		
	}
	
	public int checkUnitBill() {
		int unitResult =0;
		
		if(super.main_BillType.contains("Elect")) {
			unitResult = 8;
		}
		return unitResult;
	}

	@Override
	public String checkBillName() {
		String billName ="";
		if(super.main_BillType.contains("Elect")) {
			billName = "Electric Bill: ";
		}
		return billName;
	}
	
}
