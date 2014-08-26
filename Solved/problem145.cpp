#include<iostream>
using namespace std;

int reverseint (int n) {
    int reversed=0;
    while(n>0) {
        reversed*=10;
        reversed+=n%10;
        n/=10;
        }
    return reversed;
    }
bool isOdd( int n) {
    while(n>0) {
        if (n%2==0) return false;
        n/=10;
    }
    return true;
    }   
bool isReversible(int n) {
    return isOdd(n+reverseint(n));
    }
int main() {
    int counter=0;
    for(int i=1;i<10000000;i++){
    if (i%10==0) continue;
        if(isReversible(i)) counter++;
        }
    cout << counter << endl;
}
