import math


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



def menuCreator(n, items):
    keys = list(i for i in range(1, n+1))
    if len(keys) != len(items):
        return "მენიუ ვერ შეიქმნება"
    menu = dict(zip(keys,items))
    return menu

def main():
    while True:
        menu = menuCreator(11, [factorial, minimum, toCelsius, toFahrenheit, 
                            allPrime, sumAll, average,
                            squareSum, evenSum, lcm, allDivisors])
        print(" ")
        print("აირჩიეთ ერთ-ერთი:")
        print("1. რიცხვის ფაქტორიალის გამოთვლა")
        print("2. სამ რიცხვს შორის უმცირესის გამოთვლა")
        print("3. ტემპერატურის ფარენგეიტიდან ცელსიუსში გადაყვანა")
        print("4. ტემპერატურის ცელსიუსიდან ფარენგეიტში გადაყვანა")
        print("5. 1..n ყველა მარტივი რიცხვი")
        print("6. 1..n ყველა რიცხვის ჯამი")
        print("7. 1..n ყველა რიცხვის საშ. არითმეტიკული")
        print("8. 1..n ყველა რიცხვის კვადრატის ჯამი")
        print("9. 1..n ყველა ლუწი რიცხვის ჯამი")
        print("10. ორი რიცხვის უმცირესი საერთო ჯერადი")
        print("11. მოცემული რიცხვის ყველა გამყოფის პოვნა")
        print("0. პროგრამის შეჩერება")

        result = 0
        choice = int(input("აირჩიეთ ერთ-ერთი:"))
        if choice == 0:
            break
        
        selected_function = menu[choice]
    
        if choice == 10:
            num1 = int(input("პირველი რიცხვი:"))
            num2 = int(input("მეორე რიცხვი:"))
            result = lcm(num1 , num2)
        elif choice == 2:
            num1 = int(input("პირველი რიცხვი: "))
            num2 = int(input("მეორე რიცხვი: "))
            num3 = int(input("მესამე რიცხვი: "))
            result = minimum(num1, num2, num3)
        else:
            result = selected_function(int(input("შეიყვანეთ რიცხვი:")))
    
        print(f"შედეგი: {result}")
    

if __name__ == "__main__":
    main()