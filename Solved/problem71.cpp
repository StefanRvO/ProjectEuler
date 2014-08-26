#include<iostream>

using namespace std;
int main() {
    int Rq;
    int Rp;
    double best=1.;
    double goalfrac=3./7;
    for(int q=3;q<=1000000;q++) {
        int p=(3.*q-1)/7.;
        if (goalfrac-(double)p/q<best) {
            best=goalfrac-(double)p/q;
            Rq=q;
            Rp=p;
            }
        }
        cout << Rp<< "/" << Rq << endl;
    }
