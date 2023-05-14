def factorial(x):
    if x == 1 or x == 0:
        return 1
    
    return x * factorial(x-1)

def minimum(x,y,z):
    return min(x,y,z)

def toCelsius(temp):
    return (5/9)*(temp - 32)

def toFahrenheit(temp):
    return (temp * (9/5)) + 32

def isPrime(x):
    if x < 2:
        return False;
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            return False;
    return True

def allPrime(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i)

def sumall(n):
    if n == 1:
        return 1
    
    return n + sumall(n - 1)

def average(n):
    sum = 0
    count = 0
    for i in range(1, n+1):
        sum += i
        count += 1
    
    return sum / count

def squareSum(n):
    if n == 1:
        return 1
    return n**2 + squareSum(n-1)

print(squareSum(3))
