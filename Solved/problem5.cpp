#include<iostream>
int main() {
    long i=0;
    bool divisable=false;
    while(1) {
        i++;
        divisable=true;
        for (int j=1;j<=20;j++) {
            if (i%j!=0) {
                divisable=!divisable;
                break;
                }
            }
        if (divisable) {
            break;
            }
        }
    std::cout << i << std::endl;
}
            
