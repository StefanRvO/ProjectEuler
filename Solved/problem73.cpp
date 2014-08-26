#include<iostream>

int gcd(int x,int y) {
    int k=0;
    int x_next=0;
    while(1) {
        x_next=y;
        y=x%y;
        x=x_next;
        if(y==0) {
            return x;
        }
    }
}

using namespace std;
int main() {
    int s1=1;
    int s2=1;
    int r1=2;
    int r2=3;
    int counter=0;
    for(int q=2;q<=12000;q++) {
        for (int p=(s2*q+1)/r2;p<=(s1*q-1)/r1;p++) {
            if (gcd(p,q)==1) {
                counter++;
                }
            }
        }
    cout << counter << endl;
    }
