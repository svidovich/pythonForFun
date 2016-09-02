#!/usr/bin/Python

##This program is a machine to calculate the dot product between two vectors.
##It takes two 3D vectors and then spits out the numerical value equal
##to their product.

print("Welcome to 3D Dot product. Let your first vector be u, and your second \
v. Put them in the form ai + bj + ck. Answer the following:")

u1 = input("The first term of u (or 'a'): ")
u2 = input("The second term of u (or 'b'): ")
u3 = input("The third term of u (or 'c'): ")
v1 = input("The first term of v (or 'a'): ")
v2 = input("The second term of v (or 'b'): ")
v3 = input("The third term of v (or 'c'): ")

s = u1*v1 + u2*v2 + u3*v3
print("The dot product of your vectors is " + str(s) + ".")
