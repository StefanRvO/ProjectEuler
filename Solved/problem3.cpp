#include<iostream>
#include<math.h>
#define checknumber 600851475143

bool isPrime(long num) {
    if (num<1) {
        return false;
        }
    if (num==1 or num==2) {
        return true;
        }
    if (num%2==0) {
        return false;
        }
    bool prime=true;
    for(int i=3;i<=sqrt(num);i+=2) {
        if (num%i==0) {
            prime=!prime;
            break;
            }
        }
    if (prime==true) {
        return true;
        }
    else {
        return false;
        }
    }
long long gcd(long long x,long long y) {
    int k=0;
    int x_next=0;
    while(1) {
        x_next=y;
        y=x%y;
        x=x_next;
        k++;
        if(y==0) {
            return x;
        }
    }
}

using namespace std;
int main() {
long long maxfactor=0;
long long greatestcommon=0;
    for(int i=0;i<sqrt(checknumber)+1;i++) {
        if (isPrime(i)) {
            greatestcommon=gcd(checknumber,i);
            if (greatestcommon>maxfactor) {
                maxfactor=greatestcommon;
                }    
            }
        }
    cout << maxfactor << endl;
}
