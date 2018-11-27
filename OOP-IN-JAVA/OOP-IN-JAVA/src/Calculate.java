
public class Calculate {
	public String  HRZone ;
	public int Age;
	public int MaxHrZone ,MinHrZone;
	public int MaxHr ; 
	

	public Calculate(String hrZone , int age ) {
		// TODO Auto-generated constructor stub
		this.HRZone = hrZone ;
		this.Age = age ;
	}
	
	public int CalculateHr() {
		// TODO Auto-generated method stub
		 this.MaxHr  = 220- this.Age ;
		
		int minZone,maxZone ;
		
		if (HRZone.equalsIgnoreCase("maximium")) {
			minZone = 90 ;
			maxZone = 100 ;
		}else if (HRZone.equalsIgnoreCase("hard")) {
			minZone = 80 ;
			maxZone = 90 ;
		}else if (HRZone.equalsIgnoreCase("moderate")) {
			minZone = 70 ;
			maxZone = 80 ;
		}else if (HRZone.equalsIgnoreCase("light")) {
			minZone = 60 ;
			maxZone = 70 ;
			
		}else {
			minZone = 50 ;
			maxZone = 60 ;
		}
		
		this.MaxHrZone = (int) (MaxHr * maxZone)/100;
		this.MinHrZone = (int) (MaxHr * minZone)/100;
		return  MaxHr ; 

	}
}
