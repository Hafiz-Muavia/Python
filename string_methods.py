age=21
z="I am Muavia and I am {} years old"
print(z.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
a="I am muavia"
# strings are immutable
a="!!I am Muavia Ansari...!!!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #cant strip starter ones
print(a.replace("Muavia","SAM"))
print(a.split(" "))
b=a.split(" ")#list
print(b)
c="i am hui hui"
print(a.capitalize())
print(c.capitalize())
print(c.center(50))
print(len(c))
print(len(c.center(50)))
d=c.center(50)
print(d)
print(len(d))
e="I am Muavia. Muavia is a good boy. Muavia is nice"
print(e.count("Muavia"))
print("Muavia" in e)
print("Mavi" not in e)
print(e.endswith("!"))
print(e.endswith("e"))
print(e.endswith("i",4,10))
print(e.find("is"))#for first occurrence
print(e.find("ishh"))#returns -1
print(e.index("is"))#error if not in string
print(e.isalnum())
f="IamMuavia1"
print(f.isalnum())#true when using A-Z,a-z,0-9
print(f.isalpha())
g="IamMuavia"
print(g.isalpha())#for A-Z,a-z
print(g.islower())
h="muavia ansari_huihui321"
print(h.islower())
print(h.isprintable())
i="hi\n"
print(i.isprintable())
print(i.isspace())
j=" "
print(j.isspace())
k="                         "
print(k.isspace())
l="Muavia Is Cute"
print(a.istitle())
print(l.istitle())#every first char is Uppercase
m="I AM A BOY12345"
print(m.isupper())
print(m.startswith("I"))
print(m.swapcase())
print(m.title())
n="   Hello   12    "
print(n.strip())