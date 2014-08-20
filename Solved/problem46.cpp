#include<vector>
#include<iostream>
#include<math.h>
#define MAXVAL 10000
using namespace std;
bool isPrime(int n) {
    if (n<=1) return false;
    if (n==2) return true;
    if (n%2==0) return false;
    for (int i=3;i<=sqrt(n);i+=2) if (n%i==0) return false;
    return true;
    }

int createSquare(int n) {return n*n;}

bool checkConjecture(int n, vector<int> dsquares, vector<int>primes) {
    for (int i=0;i<dsquares.size();i++) {
        if (dsquares[i]>n) break;
        for (int j=0;j<primes.size();j++) {
            if (dsquares[i]+primes[j]>n) break;
            if (dsquares[i]+primes[j]==n) return true;
            }    
        }
    return false;
    }
    

int main() {
    //create the first 1000 sqaures, multiply with two and put into a vector
    vector<int> doublesquares;
    for (int i=1;i<=sqrt(MAXVAL);i++) doublesquares.push_back(2*createSquare(i));
    //create primes up to 10^6 and put into a vector
    vector<int> primes;
    primes.push_back(2);
    for (int i=3;i<=MAXVAL;i++) if (isPrime(i)) primes.push_back(i);
    
    for (int i=3;i<MAXVAL;i+=2) {
        if (not (checkConjecture(i,doublesquares,primes))) {
            if (not isPrime(i)) cout << i << endl;
            }
        }
    }
    
