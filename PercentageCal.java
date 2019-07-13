import java.util.*;

public class PercentageCal{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		while(1){
			float sum=0;
			System.out.print("Number of subject\t")
			int subjects=sc.nextInt();
			for(int i=0;i<subjects;i++){
				float marks=sc.nextFloat();
				marks:
				if(marks>100 || marks<0){
					System.out.println("Plz enter a valid marks");
					marks=sc.nextFloat();
					break marks;
				}
				sum+=marks;
			}
			float per=sum/subjects;
			if(per<33){
				System.out.println("Sorry, You were failed\nYour Percentage's "+per);
			}
			else if(per>=75){
				System.out.println("Congratulation's, You were passed with 1st Division\nYour Percentage's: "+per);
			}
			else{
				System.out.println("You were passed\nYour Percentage's: "+per);
			}
			System.out.println("1.Calculate Percentage\n0.Exit");
			int againOrNot=sc.nextInt();
			if(againOrNot==0){
				System.exit(0);
			}
			else if(againOrNot!=1){
				System.out.println("Invalid detected");
				System.exit(0);
			}
		}
	}
}