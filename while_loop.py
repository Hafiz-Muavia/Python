i=0
while(i<3):
    print(i)
    i=i+1
colors=["yellow","pink","purple","grey"]
j=0
while(j<len(colors)):
    print(colors[j])
    k=0
    for k in colors[j]:
        print(k, end=', ')
    print(" ")   
    j=j+1
i=3
while(i!=0):
    print("While Loop")
    i=i-1
else:
    print("else")