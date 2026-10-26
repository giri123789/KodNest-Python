c = 30
def add():
    global a
    a=10
    b=20 
    print( a + b)
    print(c) 
add()
print(a)

x= 100
def display():
    print("Local x:",x)    
display()
print("Global x:",x)

x= 100
def display():
    print(x)
    print(x)
display()
x = 30
print(x)  

def add(a=20 , b=10 , c=0):
    return(a + b + c)
print(add(10)) 
print(add(10,20))
print(add(1,1,1))
print(add())

def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name')}" , end = "  ")
    print(f"Age is {kwargs.get('age')}" , end = "  ")
    print(f"Course is {kwargs.get('course')}")
stu_info(name = 'giri' , age = 22 , course = "python" )


def count(n):
    if n== 0:
        return
    print(n)
    count( n - 1)
count(5)

def fact(n):
    if n == 1:
        return 1
        return n * fact( n - 1)
print(fact(5))

def fib(n):
    if n == 0:
        return 0
    elif n==1:
       return 1        
    return fib(n - 1) + fib(n - 2)
print(fib(5))