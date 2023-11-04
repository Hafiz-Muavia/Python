def MyFunc(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)
def greater(a,b):
    if a>b:
        print(a,"is greater than",b)
    else:
        print(b,"is greater than",a)
def smaller(a,b):
    pass
a=9
b=8
MyFunc(a,b)
greater(a,b)
smaller(a,b)
c=8
d=7
MyFunc(c,d)
greater(c,d)
smaller(c,d)
def smaller(a,b):
    if a<b:
        print(a,"is smaller than",b)
    else:
        print(b,"is smaller than",a)
