"""
for i in range(1,4):
    for j in range(1,4):
        if i==1 or i==3 or j==1 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
"""


"""
row=int(input("enter row="))
column=(int(input("enter column=")))
for i in range(1,row+1):
    for j in range(1,column+1):
        if i==1 or i==row or j==1 or j==column:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""

"""
row=int(input("enter row="))
count=0
for i in range(1,row+1):
    for j in range(1,row+1):
            if i%2==0:
                print(count,end=" ")
                count-=1
            else:
                count+=1
                print(count,end=" ")
    count+=row
    print()
"""
"""n=int(input("enter fibbo range="))
row=int(input("enter row="))
a=0
b=1
for i in range(1,row+1):
    for j in range(1,row+1):

        if i==1 and j==1:
             print(a,end=" ")
        elif i==1 and j==2:
             print(b,end=" ")
        else:
             c=a+b
             print(c,end=" ")
             a=b
             b=c
    print()
"""

























