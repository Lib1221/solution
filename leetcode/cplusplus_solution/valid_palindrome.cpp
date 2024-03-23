class Solution {
public:
    bool isPalindrome(string s) {
        string d="";
        transform(s.begin(),s.end(),s.begin(),::tolower);
        for(int i=0;i<s.length();i++){
       if (s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9'){
          d+=s[i];
        }
    }
        string f="";
        f=d;
        reverse(d.begin(),d.end());
        if(d==f){
            return 1;
        }
        else return 0;}
};
