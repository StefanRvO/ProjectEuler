

#include<iostream>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;
bool isPrime(int n) {
    if (n<=1) return false;
    if (n==2) return true;
    if (n%2==0) return false;
    for (int i=3;i<=sqrt(n);i+=2) if (n%i==0) return false;
    return true;
    }
vector<int> getPrimeDivisors(int n) {
    vector<int> pdivisors;
    int nsqrt=int(sqrt(n));
    if (n%2==1) {
        for(int i=3;i<=nsqrt;i+=2) {
            if (n%i==0) {
                if (isPrime(i)) pdivisors.push_back(i);
                if (isPrime(n/i)) pdivisors.push_back(n/i);
                }
            }
        }
    else {
        for(int i=2;i<=nsqrt;i++) {
            if (n%i==0) {
                if (isPrime(i)) pdivisors.push_back(i);
                if (isPrime(n/i)) pdivisors.push_back(n/i);
                }
            }
        }
    return pdivisors;
    }
int getPhi(int n) {
    auto div=getPrimeDivisors(n);
    float prod=n;
    for(int i=0;i<div.size();i++) prod*=(1-1./div[i]); 
    return (int)prod;
    }
vector <int> GetDigits(int n) {
    vector <int> digits;
    digits.push_back(n);
    do {
        digits.push_back(digits[digits.size()-1]/10);
        digits[digits.size()-2]%=10;
        }
    while(digits[digits.size()-1]>10);
    return digits;
    
    }
bool isPermutations(int n1,int n2) {
    auto digits1=GetDigits(n1);
    auto digits2=GetDigits(n2);
    if (digits1.size()!=digits2.size()) return false;
    sort(digits1.begin(),digits1.end());
    sort(digits2.begin(),digits2.end());
    for(int i=0;i<digits1.size();i++) if (digits1[i]!=digits2[i]) return false;
    return true;
    }
int main() {
    double minratio=99999999;
    int record;
    for (int i=1;i<10000000;i++) {
        auto totient=getPhi(i);
        if ((double)i/totient<minratio) {
            if( totient!=i and isPermutations(totient,i)) {
                minratio=((double)i/totient);
                record=i;
                cout << "New Record with ratio " << minratio << "\t" << record << endl;
                }
            }
        }
    }
