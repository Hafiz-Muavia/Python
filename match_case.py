x=int(input("Enter a value: "))
match x:
    case 0:
        print("x is zero")
    case 4 if x%2==0:
        print(x,"is obviously 4")
    case 4:
        print("x is four")
    case _ if x<0:
        print("x is negative as it is",x)
    case _ if x!=90:
        print(x,"is not 90")
    case _:
        print(x)