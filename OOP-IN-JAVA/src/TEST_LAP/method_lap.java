package TEST_LAP;

public class method_lap {
	
	public String[]testloop_arrayInput;
	private String testloop_text ="";
	private int testloop_count = 0;
	
	method_lap(String[]LoopArr,int Count,String Text){
		this.testloop_arrayInput = LoopArr;
		this.testloop_count = Count;
		this.testloop_text = Text;
	}
	method_lap(String[]LoopArr){
		this.testloop_arrayInput = LoopArr;
	}
	method_lap(String Text,int Count){
		this.testloop_text =Text;
		this.testloop_count = Count;
	}
	public int getloop() {
		return testloop_arrayInput.length+testloop_text.length()+testloop_count ;

	}
	
	public boolean checkInputWord() {
		if(testloop_text.length()<1) {
			return true;
		}
			return false;
	}
	
	public void showloopByArray () {
		System.out.println("******show loop by array.");
		try {
			for(int i = 0 ; i < testloop_arrayInput.length;i++){
				for(int j = 0; j < i+1;j++) {
					System.out.print(testloop_arrayInput[j]);
					
				}
				System.out.println("");
			}
		}catch(Exception e ) {
			
		}
	}
	
	
	public void showloopBytext(){
		int temp = testloop_count;
		for(int i=0;i<testloop_count;i++) {
			for (int sp =1;sp <= temp;sp++) {
				System.out.print(" ");
			}
			temp--;
			for(int j =0 ; j<=i;j++) {
				System.out.print(testloop_text);
				System.out.print(j);
			}
			System.out.println("");
		}
		
	}
}
