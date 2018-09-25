package lab06_key;

public class runner {

	public static void main(String[] args) {

		electTricBill objElect1 = new electTricBill("Elect","Davit", 100, 80,1);
		objElect1.displayBill();
		
		System.out.println();
		
		waterBill objWater1 = new waterBill("Water","Davit", 50, 20,1);
		objWater1.displayBill();
		
		
		
		System.out.println();
		
		
		MainBill objMain = new MainBill(objElect1, objWater1,"Davit",1);
		objMain.displayFinalBill();
		
	}
}

