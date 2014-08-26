#include<iostream>
#include<math.h>
#include<string>
using namespace std;
//We guess that the result is a square and try all found squares
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
int GetDigitSum(__int128 n) {
    __int128 ns[21];
    int size=0;
    ns[size]=n;
    do {
        size++;
        ns[size]=ns[size-1]/10;
        ns[size-1]%=10;
        }
    while(ns[size]>0);
    int summe=0;
    for (int i=0;i<size;i++) summe+=ns[i];
    return summe;
    }
bool isA(__int128 n) {
    int digitsum=GetDigitSum(n);
    if (digitsum<=1) return false;
    __int128 checker=0;
    int i=0;
    while(checker<n) {
        i++;
        checker=pow(digitsum,i);
        }
    if (checker==n) return true;
    else return false;
    }
int main() {
    int counter=0;
    for (__int128 i=10;i<1000000000;i++) {
        if (isA(i*i)) {
            counter++;
            cout << counter << "\t"<<int128_tostring(i*i) <<"\t" << sqrt(i*i) << endl ;
            }
        }
    
    }
    
