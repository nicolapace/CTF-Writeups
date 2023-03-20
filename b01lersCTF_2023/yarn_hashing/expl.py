#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes

ply=112
x=1892567312134508094174010761791081
y=4312970593268252669517093149707062

pos_in_quad=[0,0]
path=0

max_dim=2**ply
max_path=4**ply
n_twist=0

while ply>0:

    # let's check in which quadrants our number is
    # the quadrant position is: pos_in_quad [0/1, 0/1]

    if(x<((max_dim-1)/2) ):
        pos_in_quad[0]=0
    else:
        pos_in_quad[0]=1
        x=x-max_dim//2

    if(y<((max_dim-1)/2)):
        pos_in_quad[1]=0
    else:
        pos_in_quad[1]=1
        y=y-max_dim//2

    print("pos in quad = ", pos_in_quad)

    # let's sum based on the position in the quadrants
    # taking into account flips and twists

    if(pos_in_quad[0]==0 and pos_in_quad[1]==0): # we need a twist
        
        # twist
        cross = x
        x = y
        y = cross

    elif(pos_in_quad[0]==0 and pos_in_quad[1]==1):
        path += max_path//4

    elif(pos_in_quad[0]==1 and pos_in_quad[1]==1):
        path += 2*max_path//4

    elif(pos_in_quad[0]==1 and pos_in_quad[1]==0): # we need a twist and a flip
        path += 3*max_path//4

        # twist
        y=max_dim//2-y-1
        x=max_dim//2-x-1
        # flip
        cross = x
        x = y
        y = cross

    ply-=1
    max_dim=max_dim//2
    max_path=max_path//4

print("flag = ", long_to_bytes(path))