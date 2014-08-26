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
int main() {
    long summe=0;
    for (int i=2;i<=1000000;i++) summe+=EToitent(i);
    cout << summe << endl;
    }
