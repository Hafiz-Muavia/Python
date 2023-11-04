l=[3,4,5,"Muavia"]
c=l[3]
print(l,type(l))
print(len(l[3]))
print(l[1],len(l))
l[1]=2
l[3]=4
print(l)
print(l[-3])
l[3]=c
if "Muavia" in l:
    print("Yes Muavia is in list")
else:
    print("Muavia is not in list")
if "M" in c:
    print("yes")
print(l[1:3])
print(l[1:4:2])
#list comprehension
lst=[i+1 for i in range(45)]
print(lst)
lst2=[i for i in range(100) if i%2==0]
print(lst2)
print(lst2[:50:5])