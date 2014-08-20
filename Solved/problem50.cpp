#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
bool isPrime(int n) {
    if (n<=1) return false;
    if (n==2) return true;
    if (n%2==0) return false;
    for (int i=3;i<=sqrt(n);i+=2) if (n%i==0) return false;
    return true;
    }
    
int main() {
    int maxsteps=0;
    vector<int> primevec;
    for(int i=0;i<50000;i++) if (isPrime(i)) primevec.push_back(i);
    for (int i=0;i<primevec.size();i++) {
        int sum=0;
        int sumprimes=0;
        for(int j=i;j<primevec.size();j++) {
            sum+=primevec[j];
            sumprimes++;
            if (sum>1000000) break;
            if (sumprimes>maxsteps) {
                if (isPrime(sum)) {
                    cout << "new record " << sum << " with " << sumprimes << " primes." << endl;
                    maxsteps=sumprimes;
                    }
                }
            }
        }
    }
