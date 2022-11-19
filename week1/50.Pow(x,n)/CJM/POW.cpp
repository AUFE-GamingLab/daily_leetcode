class Solution {
public:
    double myPow(double x, int n) {
        double num=1;
        if(n==0 || x==num || (x==-1.0&&n%2==0))
            return num;
        else if(n<0)
            x = num/x;
        while(n&&num!=0.0)
        {
           if(n&1) 
               num*=x;
           x*=x;
           n/=2;
        }
        return num;
    }
};
