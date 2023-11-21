for i in range(5):
    print(i)
else: 
    print("Hello")
for i in []:
    print(i)
else:
    print("No i")
for i in range(5):
    print(i)
    if(i==2):
        break
else: 
    print("Hello")
#else mean for is complete 
for i in range(5):
    print("iteration on {} in for loop".format(i+1))
else:
    print("else")
for i in range(5):
    print(f"iteration on {i} in for loop")