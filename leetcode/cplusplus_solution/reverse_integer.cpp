class Solution {
public:
    int reverse(int x) {
        long long y;
        long long sum=0;
        long long z=x;
        if(z<0){
            z=z*(-1);
        while(z>0){
        y=z%10;
        sum=(sum*10)+y;
        z=z/10;
        }
        sum=sum*(-1);
        if(sum<(pow(-2,31)) || sum>(pow(2,31)-1)){sum = 0;}
        return sum;
        }
        else{
         while(z>0){
        y=z%10;
        sum=(sum*10)+y;
        z=z/10;
         }
        if(sum<(pow(-2,31)) || sum>(pow(2,31)-1)){sum = 0;}
        return sum;
        }
    }

};
