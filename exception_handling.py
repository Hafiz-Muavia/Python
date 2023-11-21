a=(input("Enter a number: "))
print(f"Table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except Exception as e:
    print(e)
a=input("Enter numerator: ")
b=input("Enter denominator: ")
try:
    print(int(a)/int(b))
except:
    print("Invalid")