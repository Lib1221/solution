class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> set;
        int sum, d;
        while(n != 1) {
            set.insert(n);
            sum = 0;
            while(n != 0) {
                d = n % 10;
                sum += d * d;
                n = n / 10;
            }
            if (set.count(sum)) {
                return false;
            }
            n = sum;
        }
        return true;
    }
};
