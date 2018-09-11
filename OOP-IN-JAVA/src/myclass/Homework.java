package myclass;

public class Homework {
	public String name;
	public String[] Word;
	
	
	public void looper () {
		
		if(this.name.substring(1,5).equalsIgnoreCase("haya")) {
			for(int i = 0 ; i < this.name.length();i++){
				for(int j = 0; j < i;j++) {
					System.out.print("*");
					System.out.print(j);
				}
				System.out.println("");
			}
		}else {
			System.out.println("ERROR!!");
		}
	}
	
	public void arrayLoop(){
		for(int i=0;i<this.Word.length;i++) {
			System.out.println(this.Word[i]);
		}
		System.out.println("Length is " + this.Word.length);
	}
	public void STRLoop(String[]textInput){
		for(int i=0;i<textInput.length;i++) {
			for(int j = 0; j < i+1;j++) {
				System.out.print(textInput[j]);
			}
			System.out.println("");
		}
		System.out.println("Length is " + textInput.length);
	}
	public void PatternLoop(String[]textInput){
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
