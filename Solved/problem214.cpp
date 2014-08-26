#include<iostream>
#include<math.h>
#include <primesieve.hpp>
#include <stdlib.h>
#include <algorithm>
#include <givaro/givintfactor.h>
#include <vector>
#include <fstream>

using namespace std;
using namespace Givaro;
std::ofstream nullStream;
IntFactorDom<> IP;
vector <int> ChainLenght;

vector <int> GetFactors(int n) {

    Integer m=n;
    vector<int> factors;
    IP.write(nullStream,factors,m);
    return factors;
    }

int EToitent(int n) {
    auto factors=GetFactors(n);
    int prod=n;
    for (int i=0;i<factors.size();i++) prod*=(1-1./factors[i]);
    
    return (int) prod;
    }
int GetChainLenght(int n) {
    if (n==0) return 0;
    if (ChainLenght.size()>n) return ChainLenght[n];
    return 1+GetChainLenght(EToitent(n));
    
    }
int main(){
Integer j;
ChainLenght.reserve(500000);
for(int i=0;i<=500000;i++) {
    ChainLenght.push_back(GetChainLenght(i));
    }
    
long summe=0;
for(int i=2;i<40000000;i=IP.nextprime(j,i)) if(GetChainLenght(i)==25) summe+=i;
cout << summe << endl;
}
