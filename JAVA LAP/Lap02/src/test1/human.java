package test1;

public class human {
	public String H_name="";
	public int H_age ;
	public String Uni_name="" ;
	
	public String showDetail() {
		return "Myname :"+H_name+" "+H_age+" "+"year old.";
		
	}
	public void fc (int start , int end) {
		System.out.println(Uni_name.substring(start,end));
		System.out.println(Uni_name.substring(start,end).length());
		if(Uni_name.substring(start,end).equalsIgnoreCase("WARE")) {
			System.out.println("TRUE");
		}else {
			System.out.println("FALSE");
		}
	}
	
	public void looper () {
		for(int i =0; i < Uni_name.length();i++) {
			for(int j = 0 ;j < i; j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}
	
}
