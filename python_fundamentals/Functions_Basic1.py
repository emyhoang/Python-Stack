def a():
    return 5
print(a())  
#output: 5

def a():
    return 5
print(a()+a())  
#output: 10


def a():
    return 5
    return 10
print(a())   
#output: 5


def a():
    return 5
    print(10)
print(a())  
#output: 5


def a():
    print(5)

x = a()
print(x)  
#output: it prints the number 5 to the console but returns None.


def a(b,c):
    print(b+c)

print(a(1,2) + a(2,3))   
#output: it prints 3,5, but the method raise error TypeError. 


def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#output: return "25"


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7

print(a())  
#output: prints 100, returns 10


def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))  
#output: 7,14,21


def a(b,c):
    return b+c
    return 10

print(a(3,5))     
b = 500
print(b)
output: Line 76 prints 8, and line 78 prints 500.


def a():
    b = 300
    print(b)

print(b) # variable b is not defined
a() # call method and print 300
print(b) # variable b is not defined
b = 500 
print(b) # print 500


def a():
    b = 300
    print(b)
    return b

print(b) #b not defined
a() # call method print 300 and return 300 
print(b) #b not defined
b = 500 
print(b) #print 500


def a():
    b = 300
    print(b)
    return b

print(b) # b not defined
b=a() # call method a() , print 300, return 300 set the result to b
print(b) # b prints 300


def a():
  print(1)
  b()
  print(2)
output: It does nothing because method a() is not called yet.


def b():
    print(3)
a()
output: It does nothing because a() is not defined.


def a():
    print(1)
    x = b()
    print(x)
    return 10
output: It does nothing because method a() is not called yet.


def b():
    print(3)
    return 5

y = a() # It raises error because a() is not defined.
print(y) # It raises error becase y is not defined.
#output: 
