#include<iostream>
using namespace std;
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

void ReduceFrac(int &numerator,int &denominator) {
    int gcdfrac=gcd(numerator,denominator);
    numerator/=gcdfrac;
    denominator/=gcdfrac;
    }
bool SameFrac(int n1,int d1,int n2,int d2) {
    if (((double)n1)/d1==((double)n2)/d2) return true;
    return false;
    }
int main() {
    int deno=1;
    int nume=1;
    
    for (int n=10;n<99;n++) {
        for(int d=n+1;d<99;d++) {
            if (n%10==0 and d%10==0) continue;
            if (SameFrac(n,d,n/10,d/10) and n%10==d%10) {nume*=n;deno*=d; cout << n << "/" << d << "=" << n/10 << "/" << d/10 << endl;}
            if (SameFrac(n,d,n%10,d/10) and n/10==d%10) {nume*=n;deno*=d; cout << n << "/" << d << "=" << n%10 << "/" << d/10 << endl;}
            if (SameFrac(n,d,n/10,d%10) and n%10==d/10) {nume*=n;deno*=d; cout << n << "/" << d << "=" << n/10 << "/" << d%10 << endl;}
            if (SameFrac(n,d,n%10,d%10) and n/10==d/10) {nume*=n;deno*=d; cout << n << "/" << d << "=" << n%10 << "/" << d%10 << endl;}
            }
        }
    ReduceFrac(nume,deno);
    cout << deno << endl;        
    }
