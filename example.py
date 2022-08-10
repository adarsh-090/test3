import math


class Complex(): 
  def add(self,z1,z2):
    return z1+z2 
  def subtract(self,z1,z2):
    return z1-z2   
  def product(self,z1,z2):
    return z1*z2 

print("Real and imaginery part of 1st comlex number")  
a=float(input("Enter real part-:")) 
b=float(input("Enter imagenary part-:"))  
print("Real and imaginery part of 2nd complex number")
a1=float(input("Enter real part-:")) 
b1=float(input("Enter imaginery part-:")) 
z1=complex(a,b) 
z2=complex(a1,b1)  
c=Complex()
print("Addition of complex number--:  ",c.add(z1,z2))
print("Substraction of complex numbers--:  ",c.subtract(z1,z2))
print("Product of complex numbers--:  ",c.product(z1,z2))




















"""def subComplex( z1, z2):
    return z1-z2
 
# driver program
z1 = complex(2, 3)
z2 = complex(1, 2)
print( "Subtraction is : ", subComplex(z1, z2))"""


