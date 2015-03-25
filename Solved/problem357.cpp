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

bool isPrime(int n)
{
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

vector<int> GetAllFactors(int n)
{
  vector<int> Factors;
  vector<int> pFactors = GetFactors(n);
  for(auto i = 0; i < pFactors.size(); i++)
  {
    Factors.push_back(pFactors[i]);
    for(auto j = i + 1; j < pFactors.size(); j++)
    {
      Factors.push_back(pFactors[i]* pFactors[j]);
    }
  }
  Factors.push_back(1);
  Factors.push_back(n);

  return Factors;
}

bool valid(int n)
{
  for(auto i : GetAllFactors(n))
  {
    if(!isPrime(i+n/i)) return false;
  }
  return true;
}

int main()
{
  long sum = 0;
  for (size_t i = 1; i <= 100000000; i++) {
    if(i%10000 == 0)
      cout << i << endl;
    if(valid(i)) sum+=i;
  }
  cout << sum << endl;
}
