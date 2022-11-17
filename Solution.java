class Solution {
    public double myPow(double x, int n) {
        return n >= 0?power(x,n):1.0/power(x,n);
    }
    public double power(double x,int n){
        if(n == 0){
            return 1.0;
        }
        double y = power(x,n/2);
        return n % 2 == 0 ?y*y:y*y*x;
    }
}

