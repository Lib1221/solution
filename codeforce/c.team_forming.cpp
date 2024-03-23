#include<bits/stdc++.h>
using namespace std;
int main(){
    int x;
    cin>>x;
    int arr[x];
    for(int i=0;i<x;i++){
        int f;
        cin>>f;
        arr[i]=f;
    }
    sort(arr,arr+x);
    int sum = 0;
    for(int i=1;i<x;i+=2){
        sum=arr[i]-arr[i-1]+sum;

    }
    cout<<sum;

}
