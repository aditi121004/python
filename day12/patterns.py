"""row=int(input("enter row="))
for i in range(1,row+1):
    for j in range(i):
        print("*",end=" ")
    print()"""

"""row=int(input("enter row="))
for i in range(row,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()"""


"""row=int(input("enter row="))
for i in range(1,row+1):
    for j in range(i):
        print(i,end=" ")
    print()"""

"""row=int(input("enter row="))
for i in range(row,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()"""


"""
row=int(input("enter row="))
count=0
for i in range(1,row+1):
    for j in range(i):
        count+=1
        print(count,end=" ")
    print()
"""

row=int(input("enter row="))
count=1
for i in range(1,row+1):
    i=count
    for j in range(i):
        print(i,end=" ")
        i=row-1
    count+=1
    print()







































