#include<iostream>
#include<math.h>
#include <primesieve.hpp>
#include <stdlib.h>
#include <algorithm>
#include <givaro/givintfactor.h>
#include <vector>
#include <fstream>
#include <algorithm>
//#include <cassert>
using namespace std;
using namespace Givaro;
std::ofstream nullStream;
IntFactorDom<> IP;

bool paircompare(pair<long,long> i,pair<long,long> j) {
    if  (i.first==j.first) return (i.second<j.second);
    return (i.first<j.first);
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
    int limit=100000;
    int goal=10000;
    vector<pair<long,long> > radicals;
    for(int i=1;i<=limit;i++) radicals.push_back(make_pair(rad(i),i));
    sort(radicals.begin(),radicals.end(),paircompare);
   /* for(int i=0;i<radicals.size();i++) {
        cout << radicals[i].second << "\t" << radicals[i].first << "\t" << i << endl;
        }*/
    cout << radicals[goal-1].second << endl;
    }
        
