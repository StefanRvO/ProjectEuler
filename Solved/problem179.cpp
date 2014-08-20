#include <iostream>
#include <vector>
#include<math.h>
using namespace std;
bool isSquare(int n) {
    return (sqrt(n)==int(sqrt(n)));
    }
int getDivisorsCount(int n) {
    int divisors=2;
    int nsqrt=int(sqrt(n));
    if (n==1) divisors=1;
    if (n%2==1) {
        for(int i=3;i<=nsqrt;i+=2) {
            if (n%i==0) {
                divisors+=2;
                }
            }
        }
    else {
        for(int i=2;i<=nsqrt;i++) {
            if (n%i==0) {
                divisors+=2;
                }
            }
        }
    if (isSquare(n)) divisors--;
    return divisors;
    }

int main() {
    int counter=0;
    int lastdivisors=0;
    int thisdivisors=0;
    for(int i=2;i<10000000;i++) {
        lastdivisors=thisdivisors;
        thisdivisors=getDivisorsCount(i);
        if (lastdivisors==thisdivisors) counter++;

        }
    cout << counter << endl;
    
    
    }
    
