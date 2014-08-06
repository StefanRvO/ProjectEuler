#include<iostream>

int count=0;
int level1,level2,level3,level4,level5,level6;
int main() {
    for(int i=0;i<=200/1;i++) {
        for(int j=0;j<=200/2;j++) {
            level1=i+2*j;
            if (level1>200) break;
            for(int k=0;k<=200/5;k++) {
                level2=level1+k*5;
                if (level2>200) break;
                for(int l=0;l<=200/10;l++) {
                    level3=level2+l*10;
                    if (level3>200) break;
                    for(int m=0;m<=200/20;m++) {
                        level4=level3+m*20;
                        if (level4>200) break;
                        for(int n=0;n<=200/50;n++) {
                            level5=level4+n*50;
                            if (level5>200) break;
                            for(int o=0;o<=200/100;o++) {
                                level6=level5+o*100;
                                if (level6>200) break;
                                for(int p=0;p<=200/200;p++) {
                                    if (level6+p*200==200) count++;
                                
                                }
                            }
                        }
                    }
                }
            }                        
        }
    }
    std::cout << count << std::endl;
}
