a=int(input("Enter your age: "))
print("Your age is: ",a)
#condition operators as print(a>18) etc it will return boolean datatype
if(a>18):
    print("You can drive")
elif a<0:
    print("Wrong input")
else:
    print("You cannot drive")