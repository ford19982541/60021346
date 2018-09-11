package myclass;

public class runer {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Homework H1 = new Homework();
		H1.name = "phayao";
		H1.Word = []{"p","h","a","y","a","o"};
		H1.arrayLoop();
		H1.looper();
		String[] Newworld = {"p","h","a","y","a","o"};
		
		
	}
	public static void arrayLoop(String[]textInput){
		for(int i=0;i<textInput.length;i++) {
			System.out.println(textInput[i]);
		}
		System.out.println("Length is " + textInput.length);
	}
	public static void STRLoop(String[]textInput){
		for(int i=0;i<textInput.length;i++) {
			for(int j = 0; j < i+1;j++) {
				System.out.print(textInput[j]);
			}
			System.out.println("");
		}
		System.out.println("Length is " + textInput.length);
	}
	public static void PatternLoop(String[]textInput){
		int temp = textInput.length ;
		for(int i=0;i<textInput.length;i++) {
			for (int sp =1;sp <= temp;sp++) {
				System.out.print(" ");
			}
			temp--;
			for(int j =1 ; j<=i;j++) {
				System.out.print("#");
				System.out.print(j);
			}
			System.out.println("");
		}
		
	}
}
