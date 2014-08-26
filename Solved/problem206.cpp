#include<iostream>

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
    
bool IsConcealedSquare(__int128 n) {
    for (int i=9;i>=1;i--) {
        n/=100;
        if (not (n%10==i)) return false;
    }
    return true;

}
int main() {
__int128 i=30;
bool switche=true;;
for(;!IsConcealedSquare(i*i);){
    if (switche) i+=40;
    else i+=60;
    switche=!switche;
    }
cout << int128_tostring(i) << endl;

}
