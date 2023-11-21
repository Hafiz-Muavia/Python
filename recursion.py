def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def fibo(n):
    if n==0:
        print(0)
    elif n==1:
        print(0,1)
    else:
        print(0,",",1,end=" , ")
        j=0
        k=1
        l=j+k
        while l<=n:
            l=j+k
            print(l,end=" , ")
            j=k
            k=l
fibo(10)
# def fibo_recursive(n, a=0, b=1):
#     if n > 0:
#         print(a, end=" , ")
#         fibo_recursive(n - 1, b, a + b)


# fibo_recursive(10)

        
