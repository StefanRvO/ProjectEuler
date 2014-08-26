#include <string>
#include <sstream>
#include <iostream>
#include<stdio.h>
#include<math.h>


using namespace std;

class fibio {
    bool switche=true;
    public:
    unsigned long long F1=0;
    unsigned long long F2=0;
    int generation=0;
    fibio (int fibionum=1,int gen=1) {
        F1=fibionum;
        generation=gen;
    }
    unsigned long long next() {
        switche=!switche;
        generation++;
        if (switche) {F2+=F1; return F2;}
        else {F1+=F2; return F1;};
        }

    unsigned long long cur() {
        if (switche) {return F2;}
        else { return F1;};
        }
    };
    
class FibionaciWord {
    
    bool switche=true;
    public:
    string String1,String2;
    FibionaciWord (string a,string b) {
        String1=a;
        String2=b;
        }
    unsigned long long LenOfItteration(int n) {
        int Stringsize=String1.length(); //We assume same lenght for both given strings
        fibio fib;
        for (int i=0;i<n;i++) fib.next();
        return fib.cur()*Stringsize;
        }
    char GetCharAtIndex(unsigned long long index) {
        int Stringsize=String1.length(); //We assume same lenght for both given strings
        fibio fib;
        while(fib.cur()<index) fib.next();
        int gen=fib.generation;
        
        while(index>=2*Stringsize) {
            if (index>LenOfItteration(gen-2)) {
                index-=LenOfItteration(gen-2);
                }
            else {
                index+=LenOfItteration(gen-1)-LenOfItteration(gen-2);
                gen--;
                }
            }
        if (index<Stringsize) return String1[index-1];
        else return String2[index-Stringsize-1];
        }
            
    };

int main() {
    FibionaciWord fibi("82148086513282306647093844609550582231725359408128 ","48111745028410270193852110555964462294895493038196");
    for (int i=0;i<=17;i++) {
        printf("%c\t%d\n",fibi.GetCharAtIndex((127+19*i)*pow(7,i)),i);
    }
        

}
