#include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[5][5];
    int column=0,row=0;
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            int x;
            cin>>x;
            if(x==1){
                row=i;
                column = j;
            }
        }
    }
    
    column=abs(column-2);
    row=abs(row-2);
    cout<<column+row;
}
