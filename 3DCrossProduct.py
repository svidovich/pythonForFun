#!/usr/bin/Python
##This program is a matrix cross product machine for
##three dimensional vectors
##It takes two vector arguments and returns
##Their cross-product


print("Welcome to 3D cross product. Let your first vector be u, your second v. Put them in the form ai + bj + ck. Answer these:")
##The following lines take the values of the vectors to be produced
u1 = input("First entry of u (or 'a'): ")
u2 = input("Second entry of u (or 'b': ")
u3 = input("Third entry of u (or 'c': ")
v1 = input("First entry of v (or 'a': ")
v2 = input("Second entry of v (or 'b'): ")
v3 = input("Third entry of v (or 'c'): ")

##The special case
if u1 == u2 == u3 and v1 == v2 == v3:
	print("The solution is 0i + 0j + 0k.")
##
si = (u2*v3 - u3*v2)
sj = (-1)*(u1*v3 - u3*v1)
sk = (u1*v2 - u2*v1)
##These three lines are the solutions for each direction individually

if sj < 0 and sk < 0:
	print("The solution is:  {0}i {1}j {2}k".format(si, sj, sk))
if sj < 0 and sk > 0:
	print("The solution is: {0}i {1}j + {2}k".format(si, sj, sk))
if sj > 0 and sk < 0:
	print("The solution is: {0}i + {1}j {2}k".format(si, sj, sk))
if sj > 0 and sk > 0:
	print("The solution is: {0}i + {1}j + {2}k".format(si, sj, sk))
##These conditions are just here to make the output look nicer

