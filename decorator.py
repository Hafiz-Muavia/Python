def hello(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx
@hello
def hi():
    print("Hello")
hi()