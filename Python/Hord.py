import math
#Хорд

def f(x):
    return (x-5)**2-math.sin(x-5)
def f1(x):
    return math.sin(x-5)+2


a = 4.85
b = 5.2
e = 0.1


if(f(a) * f1(a) > 0):
    c=a
else:
    c=b
if(f(a) * f1(a) < 0):
    x=a
else:
    x=b
while True:
    dx = f(x) * (x - c) / (f(x) - f(c))
    x = x - dx

    if (math.fabs(dx)<e):
        break

print(x);