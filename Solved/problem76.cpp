#include<iostream>
#include<vector>
#include <string>

using namespace std;

string int128_tostring(__int128 n)
{
    string s="";
    if (n == 0) {
      s="0";
      return s;
    }
    while (n!=0) {
        s+=(n%10+0x30);
        n/=10;
        }
    s=string(s.rbegin(),s.rend());
    return s;
}
__int128 p(int n, vector<__int128> partvector) {
    if (n<0) return 0;
    if (n<=1) return 1;
    if (partvector.size()>n) return partvector[n];
    __int128 summe=0;
    for (int k=1;k<=n;k++) {
        if (k%2==0) summe-=(p(n-k*(3*k-1)/2,partvector)+p(n-k*(3*k+1)/2,partvector));
        else summe+=(p(n-k*(3*k-1)/2,partvector)+p(n-k*(3*k+1)/2,partvector));
        }
    return summe;
    }
int main() {
    int target=100;
    vector<__int128> partitions;
    for (int i=0;i<=target;i++) partitions.push_back(p(i,partitions));
    cout << int128_tostring(p(target,partitions)-1) << endl;
    
    }
