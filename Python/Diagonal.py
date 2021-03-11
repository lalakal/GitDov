import math
#Деления пополам

def f(x):
    return (x-5)**2-math.sin(x-5)

a = 4.85
b = 5.2
e = 0.01


while((math.fabs(b - a)) > 2*e):
    x = (a+b)/2
    if(f(a)*f(x) < 0): 
        b = x
    else:
        a = x
print(x);