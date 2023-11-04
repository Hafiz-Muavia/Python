l=[i for i in range(5)]
print(l)

l.append(9)
print(l)

m=[3,1,-3,22,-89,3]
print(m)

print(m.index(3))

m.reverse()
print(m)

m.sort()
print(m)

m.sort(reverse=True)
print(m)

print(m.index(3))

print(m.count(3))

o=m
o[0]=1000
print(m,o)

n=m.copy()
n[0]="Muavia"
print(m,n)

m.insert(2,899)
print(m)

m.extend(n)#k=m +n
print(m)
print(n)
# print(k)

color=["Yellow","royal blue","Z ish pink"]
color.sort()
print(color)