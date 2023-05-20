import math
import os

def factorial(x):
    '''#1. ფაქტორიალის გამოთვლა'''
    if x == 1 or x == 0:
        return 1
    return x * factorial(x-1)


def minimum(x, y, z):
    '''#2. სამ რიცხვში უმცირესის პოვნა'''
    return min(x, y, z)


def toCelsius(temp):
    '''#3. F-C გადამყვანი'''
    return (5/9) * (temp - 32)

def toFahrenheit(temp):
    '''#3. C-F გადამყვანი'''
    return (temp * (9/5)) + 32


def isPrime(x):
    '''#4. მოცემულ დიაპაზონში (1..n) ყველა მარტივი რიცხვის პოვნა'''
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def allPrime(n):
    for i in range(2, n+1):
        if isPrime(i):
            print(i)


def sumAll(n):
    '''#5. 1-დან n-მდე ყველა რიცხვის ჯამი'''
    if n == 1:
        return 1
    return n + sumAll(n - 1)


def average(n):
    '''#6. 1-დან n-მდე ყველა რიცხვის საშუალო არითმეტიკული'''
    sum = 0
    count = 0
    for i in range(1, n+1):
        sum += i
        count += 1
    return sum / count

def squareSum(n):
    '''#7. 1-დან n-მდე ყველა რიცივის კვადრატების ჯამი'''
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum


def evenSum(n):
    '''#8. 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი'''
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum


def lcm(a, b):
    '''#9. ორი რიცხვის უმცირესი საერთო ჯერადი'''
    return abs(a * b) // math.gcd(a, b)


def allDivisors(n):
    '''#10. მოცემული რიცხვის ყველა გამყოფის პოვნა '''
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors




def main():
    menu = [
        ("ფაქტორიალის გამოთვლა", factorial),
        ("სამ რიცხვში უმცირესის პოვნა", minimum),
        ("ფარენგეიტიდან ცელსიუსზე გადაყვანა", toCelsius),
        ("ცელსიუსიდან ფარენგეიტზე გადაყვანა", toFahrenheit),
        ("1..n ყველა მარტივი რიცხვის პოვნა", allPrime),
        ("1..n ყველა რიცხვის ჯამი", sumAll),
        ("1..n ყველა რიცხვის საშ. არითმეტიკული", average),
        ("1..n ყველა რიცხვის კვადრატების ჯამი", squareSum),
        ("1..n ყველა ლუწი რიცხვის ჯამი", evenSum),
        ("ორი რიცხვის უსჯ", lcm),
        ("მოცემული რიცხვის ყველა გამყოფის პოვნა", allDivisors),
        ]
    
    actions = {
        "1": factorial,
        "2": minimum,
        "3": toCelsius,
        "4": toFahrenheit,
        "5": allPrime,
        "6": sumAll,
        "7": average,
        "8": squareSum,
        "9": evenSum,
        "10": lcm,
        "11": allDivisors,
    }

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("მენიუ:")
        for i,item in enumerate(menu):
            print(f"{i + 1}.{item[0]}")
        
        choice = input("აირჩიე მოქმედება:")
        action = actions[choice]
        result = 0

        if action is None:
            break
        

        if action == minimum:
            a = float(input("შეიყვანე პირველი რიცხვი"))
            b = float(input("შეიყვანე მეორე რიცხვი"))
            c = float(input("შეიყვანე მესამე რიცხვი"))
            result = action(a, b, c)
        elif action == lcm:
            a = float(input("შეიყვანე პირველი რიცხვი"))
            b = float(input("შეიყვანე მეორე რიცხვი"))
            result = action(a, b)
        else:
            a = float(input("შეიყვანე რიცხვი:"))
            result = action(a)
        
        print(f"შედეგი: {result}")

if __name__ == "__main__":
    main()