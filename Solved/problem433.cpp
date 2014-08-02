#include<iostream>
#include <thread>
#include <future>
//#include "gcd.h"
#define limit 5000000
//#define debug
//This will take a VERY long time



int gcdk(int x,int y) {
    int k=0;
    int x_next=0;
    while(1) {
        x_next=y;
        y=x%y;
        x=x_next;
        k++;
        if(y==0) {
            return k;
        }
    }
}

long long getKofRow(int x) {
    long long summe=0;
    for (int y=1;y<=limit;y++) {
        if (x==y) {
           summe+=1;
           }
        else if(x>y){
            summe+=gcdk(x,y)*2+1;
            }
        else {
           break;
           }
        }
    return summe;
    }
    
using namespace std;
int main() {
    long long summe=0;
    for (int x=1;x<=limit;x+=2) {
        #ifdef debug
        if(x%(limit/1000)==0) {
            cout << x/float(limit)*100 << "\tpercent done!" << endl;
            } 
        #endif
        if(x>limit-2) {
            while(x<=limit) {
                summe+=getKofRow(x);
                x++;
                }
            break;
            }
        
                
        auto future1=async(std::launch::async,getKofRow,x);
        auto future2=async(std::launch::async,getKofRow,x+1);
        summe+=future1.get();
        summe+=future2.get();
          

        }
    cout << summe << endl;        
    }

