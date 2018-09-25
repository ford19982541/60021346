package TEST_LAP;

import com.sun.org.apache.bcel.internal.classfile.Method;

public class run {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[]a = {"P","H","A","Y","A","O"};
		method_lap objtest = new method_lap(a);
		objtest.showloopByArray();
		System.out.println(" ");
		
		method_lap objtest2 = new method_lap("A",5);
		objtest2.showloopBytext();
		System.out.println(" ");
		
		String[]b = {"S","E"};
		method_lap objtest3 = new method_lap(b,5,"SE");
		objtest3.showloopBytext();
		System.out.println(" ");
	}
		
	
	
	
	
}
