emp={
    1:100,
    2:69,
    45:45,
    9:21
}
emp2={
    3:20,
    4:29
}
print(emp,emp2)
emp.update(emp2)
print(emp,emp2)
emp2.clear()
print(emp2)
print(emp.pop(3))
emp.popitem()
print(emp)
del emp2
del emp[9]
print(emp)