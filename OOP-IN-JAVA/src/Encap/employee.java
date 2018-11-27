package Encap;

public class employee {
	public int employee_Ot;
	private int employee_Salary;
	 //Encapsulation
		//Method setter
		public void setSalary(int salary) {
			if(salary <= 20000) {
				this.employee_Salary = salary ;
			}else {
				System.out.println("ERROR !!! OVER Salary .");
			}
		}
		//Method getter
		public int getSalary() {
			return this.employee_Salary;
		}
	public int calculateSalary() {
		return this.employee_Ot+this.employee_Salary;
	}
}
