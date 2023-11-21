s={2,3,4,9,9}
print(s)
mavi={}
print(mavi)
print(type(mavi))
mavi=set()
print(mavi)
print(type(mavi))
for i in s:
    print(i)
for i in mavi:
    print(i)
j={"Muavia",19,4}
print(s.union(j))
print(s,j)
s.update(j)
print(s,j)
# difference is, in updation, s changes but in union it doesnt chng
print(s.intersection(j))
s.intersection_update(j)
print(s,j)
s={2,3,4,9,9}
print(s.symmetric_difference(j))
print(s.difference(j))
s.symmetric_difference_update(j)
print(s,j)
s={2,3,4,9,9}
print(s.isdisjoint(j))
print(s.issuperset(j))
k={2,3}
print(s.issuperset(k))
print(s.issubset(k))
print(k.issubset(s))
k.add("Hui")
print(k)
k.remove("Hui")
print(k)
k.discard(1)
print(k)
m=s.pop()
print(s,m)
k.clear()
print(k)
del k
if "Muavia" in j:
    print("hello")