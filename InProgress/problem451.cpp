#include<iostream>
int gcd(int x,int y) {
    int k=0;
    int x_next=0;
    while(1) {
        x_next=y;
        y=x%y;
        x=x_next;
        k++;
        if(y==0) {
            return x;
        }
    }
}
int modinv(int a, int b)
{
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}
bool CoPrime(int a,int b) {
    for(;;) {
    if (!(a %= b)) return b == 1 ;
    if (!(b %= a)) return a == 1 ;
    }
}

int l(int n) {
        for (int m=n-2;m>n/2;m--) {
            if ( gcd(m,n)!=1) {
                continue;
            }
            if (modinv(m,n)==m) {
                return m;
                }
            }
        return 1;
    }
using namespace std;
int main() {
long long counter=0;
for (int i=3;i<=10000;i++) {
counter+=l(i);
}
cout << counter << endl;
}
