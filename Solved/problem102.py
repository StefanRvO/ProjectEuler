#!/usr/bin/python3

def GetTriangle(line):
  numbers=[]
  number = ""
  for i in line:
    if(i == ","):
      numbers.append(int(number))
      number = ""
    else:
      number+=i
  numbers.append(int(number[:-1]))
  return [[numbers[0],numbers[1]],[numbers[2],numbers[3]],[numbers[4],numbers[5]]]
  
def isInside(Triangle, Point):
  alpha1_n = (Triangle[1][1] - Triangle[2][1]) * (Point[0] - Triangle[2][0])
  alpha2_n = (Triangle[2][0] - Triangle[1][0]) * (Point[1] - Triangle[2][1])
  alpha1_d = (Triangle[1][1] - Triangle[2][1]) * (Triangle[0][0] - Triangle[2][0])
  alpha2_d = (Triangle[2][0] - Triangle[1][0]) * (Triangle[0][1] - Triangle[2][1])
  alpha = (alpha1_n + alpha2_n) / (alpha1_d + alpha2_d)
  
  beta1_n = (Triangle[2][1] - Triangle[0][1]) * (Point[0] - Triangle[2][0])
  beta2_n = (Triangle[0][0] - Triangle[2][0]) * (Point[1] - Triangle[2][1])
  beta1_d = (Triangle[1][1] - Triangle[2][1]) * (Triangle[0][0] - Triangle[2][0])
  beta2_d = (Triangle[2][0] - Triangle[1][0]) * (Triangle[0][1] - Triangle[2][1])
  beta = (beta1_n + beta2_n) / (beta1_d + beta2_d)
  
  gamma = 1. - alpha - beta
  
  return (alpha > 0 and beta > 0 and gamma > 0)
  
f = open("p102_triangles.txt")

number = 0
count = 0
for i in f:
  number+=1
  origoInside = isInside(GetTriangle(i),[0,0])
  if origoInside:
    count+=1
  print (str(origoInside), number)
print(count)
