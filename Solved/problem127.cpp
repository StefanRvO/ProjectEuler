#include<iostream>
#include<math.h>
#include <primesieve.hpp>
#include <stdlib.h>
#include <algorithm>
#include <givaro/givintfactor.h>
#include <vector>
#include <fstream>
//#include <cassert>
using namespace std;
using namespace Givaro;
std::ofstream nullStream;
IntFactorDom<> IP;

int gcd(int x,int y) {
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
bool isPrime(int n) {
    if (n<=1) return false;
    if (n==2) return true;
    if (n%2==0) return false;
    for (int i=3;i<=sqrt(n);i+=2) if (n%i==0) return false;
    return true;
    }
vector <int> GetFactors(int n) {

    Integer m=n;
    vector<int> factors;
    IP.write(nullStream,factors,m);
    return factors;
    }
    
int rad(int n) {
    vector<int> factors=GetFactors(n);
    int prod=1;
    for (int i=0;i<factors.size();i++) prod*= factors[i];
    return prod;
    }
int main() {
    int limit=120000;
    vector<long> radicals;
    for(int i=0;i<limit;i++) radicals.push_back(rad(i));
    int summe=0;
    int b;
    for(int c=2;c<limit;c++) {
        for (int a=1;a<c;a++) {
            b=c-a;
            if (a>=b) break;
            if (radicals[c]*radicals[a]*radicals[b]>=c) continue;
            if (gcd(a,b)!=1) continue;
            
            summe+=c;
            }
        }
    using namespace std;
    cout << summe << endl;
    }
        
