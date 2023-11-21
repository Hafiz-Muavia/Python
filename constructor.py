class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My name is {self.name} and i am {self.age} years old")
a=person("Mavi",21)#constructor always return None
a.info()
