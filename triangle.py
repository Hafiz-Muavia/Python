i=0
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print(" ")
k=5
for i in range(6):
    for j in range(k):
        print("%",end=" ")
    k=k-1
    print(" ")
l=5
for i in range(6):
    for j in range(i):
        print(" ",end=" ")
    for k in range(l):
        print("*",end=" ")
    l=l-1
    print(" ")
l=5
for i in range(6):
    for j in range(l):
        print(" ",end=" ")
    l=l-1
    for k in range(i):
        print("%",end=" ")
    print(" ")
l=5
for i in range(1,6):
    for j in range(l):
        print(" ",end=" ")
    l=l-1
    for k in range(i):
        print(" * ",end=" ")
    print(" ")
m=1
l=5
for i in range(1,6):
    for j in range(l):
        print(" ",end=" ")
    l=l-1
    for k in range(m):
        print("*",end=" ")
    print(" ")
    m=m+2