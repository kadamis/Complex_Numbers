import math
import random

class Complex:
    
    def __init__(self,a,b):

        self.a=a
        self.b=b

    def get_real_number(self):

        return self.a
    
    def get_imaginary_number(self):
        
        return self.b

    def get_norm(self):

        return math.sqrt(self.a**2 + self.b**2)

    def get_angle(self):

        if self.a!=0:
            return math.atan(self.b/self.a)
        else:
            return 1.5625

    def AddComplex(x,y,z,w):

        a = x + y
        b = z + w

        return (a+1j*b)
    
    def SubComplex(x,y,z,w):

        a = x - y
        b = z - w

        return (a+1j*b)

c1 = Complex(random.randint(1,6),random.randint(1,6))
c2 = Complex(random.randint(1,6),random.randint(1,6))

print("c1=",c1.get_real_number(),"+",c1.get_imaginary_number(),"j",sep="")
print("c2=",c2.get_real_number(),"+",c2.get_imaginary_number(),"j",sep="")

print("r,φ =",c1.get_norm(),c1.get_angle())
print("r,φ =",c2.get_norm(),c2.get_angle())

c3 = Complex.AddComplex(c1.get_real_number(),c2.get_real_number(),c1.get_imaginary_number(),c2.get_imaginary_number())
print("c3=",c3,sep="")

c4 = Complex.SubComplex(c1.get_real_number(),c2.get_real_number(),c1.get_imaginary_number(),c2.get_imaginary_number())
print("c4=",c4,sep="")

import matplotlib.pyplot as plt

plt.grid()
plt.plot(c1.get_real_number(),c1.get_imaginary_number(),"r*",c2.get_real_number(),c2.get_imaginary_number(),"b*")
plt.show()

L = [[c1.get_real_number(),c1.get_imaginary_number()],[c2.get_real_number(),c2.get_imaginary_number()]]
X = [L[0][0],L[1][0]]
Y = [L[0][1],L[1][1]]

if (L[0][0]==L[1][0]) and (L[0][1]==L[1][1]):
    plt.plot (L[0][0],L[0][1], "r*")
else:
    plt.plot(X,Y,"-.g")

plt.grid()
plt.show()
