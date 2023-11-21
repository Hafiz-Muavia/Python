dic={"name":"Muavia","age":21}
print(dic)
print(dic["name"])
roll={
    1:"Mavi",
    9:"Moin",
    45:"zain"
}
print(roll[9])
print(roll.get(9))
print(roll.get(2))#roll[2] get error
print(roll.keys())
print(roll.values())
for i in roll.keys():
    print(roll[i])
for i in roll.keys():
    print(f"The value corresponds to {i} is {roll[i]}")
print(roll.items())
for i,j in roll.items():
    print(f"The value corresponds to {i} is {j}")