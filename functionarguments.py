#required arguments
def avg(a,b):
    print("Average is: ",(a+b)/2)
avg(2,3)
#default arguments
def avg(a=5,b=1):
    print("Average is: ",(a+b)/2)
avg(2,3)
avg()
avg(b=25)

def name(fname,sname="Ansari",mname="Sahib"):
    print("Hello",fname,sname,mname)
    
name("Muavia", "hui")

#Keyword arguments
avg(b=23,a=21)

#arbitrary arguments
def avgg(*n):
    print(type(n))
    
    sum=0
    for i in n:
        sum=sum+i
    print(sum/len(n))
    return sum/len(n)
c=avgg(1,2,3)
print("avg c is: ",c)
#keyword arbitrary arguments
def name(**name):
    print(type(name))
    print("Hi",name["fname"],name["mname"],name["lname"])
name(fname="Hafiz",mname="Muavia",lname="Ansari")