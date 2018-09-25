package lab06_key;

import java.time.LocalDate;
import java.time.LocalTime;

public class waterBill extends MainBill {

	public waterBill(String billType, String name, int curUnit, int preUnit, int roomNumber) {
		super(billType, name, curUnit, preUnit, roomNumber);
		
	}
	public int checkUnitBill() {
		int unitResult =0;
		
		if(super.main_BillType.contains("Water")) {
			unitResult = 5;
		}
		return unitResult;
	}
	@Override
	public String checkBillName() {
		String billName ="";
		if(super.main_BillType.contains("Water")) {
			billName = "Water Bill: ";
		}
		return billName;
	}
	

	
	
}
