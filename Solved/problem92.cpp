#include<iostream>
using namespace std;
int GetSquareSum(int n);
int GetChainEnd(int n) {
    while(n!=1 and n!=89) n=GetSquareSum(n);
    return n;
    }
int GetSquareSum(int n) {
    int ns[10];
    int size=0;
    ns[size]=n;
    do {
        size++;
        ns[size]=ns[size-1]/10;
        ns[size-1]%=10;
        }
    while(ns[size]>0);
    int summe=0;
    for (int i=0;i<size;i++) summe+=ns[i]*ns[i];
    return summe;
    }
int main() {
    int summe=0;
    for (int i=1;i<10000000;i++) {
        if(GetChainEnd(i)==89) summe++;
        }
    cout << summe << endl;
    }
        
