class Solution {
    public double myPow(double x, int n) {
    double res=1;
    if(x==1){
         return 1; 
    }else if(x==0){
        return 0;
    }else{
    if(n>0){
        for(int i=0;i<n;i++){
        res*=x;
    }
    return res;
    }else if (n==0)  {
        return 1;
    }else if(n<0){
        n=-n;
        for(int i=0;i<n;i++){
        res*=1/x; 
    }
    return res;
    }
    }
   

    return 0;
}
}
