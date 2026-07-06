# Find quardrant and distance.
import math
def get_quardrant(x,y):
    if x>0 and y>0:
     return "1st Quardrant"
    elif x<0 and y>0:
     return "2nd Quardrant"
    elif x<0 and y<0:
     return "3rd Quardrant"
    elif x>0 and y<0:
     return "4rth Quardrant"
    elif x==0 and y!=0:
     return "on y_axis"
    elif x!=0 and y==0:
     return "on x_axis"
    else:
     return "on origin"
# To take input
x1,y1= map(int,input("Enter the points(x1,y1):").split(','))
print(get_quardrant (x1,y1))
x2,y2=map(int,input("Enter the points (x2,y2):").split(','))
print(get_quardrant(x2,y2))
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance between the points is:",distance)



