public class problem_7{
    void problem_7(){
    }
    long inp=10001;
    boolean checkPrime(long ex){
	int i;
	for(i=3;i<=Math.sqrt(ex);i+=2){
	    if(ex%i == 0)
		return false;
	}
	return true;
    }
    static public void main(String args[]){
	problem_7 prob = new problem_7();
	long count=4,n=2, num=0;
	long prime=0;
	while(count<prob.inp){
	    num=6*n-1;
	    if(prob.checkPrime(num)){
		count++;
		prime = num;
	    }
	    num=6*n+1;
	    if(prob.checkPrime(num) && count<prob.inp){
		count++;
		prime = num;
	    }
	    //	    System.out.println(num + "\t" + count);
	    n++;
	}
      	System.out.println(prime);
    }
}
