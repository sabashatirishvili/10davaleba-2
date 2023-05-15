import math

#1. ფაქტორიალის გამოთვლა
def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x-1)

#2. სამ რიცხვში უმცირესის პოვნა
def minimum(x, y, z):
    return min(x, y, z)

#3. ტემპერატურს შკალის კონვერტორი ცელსიუსიდან ფარენგეიტში და პირიქით
def toCelsius(temp):
    return (5/9) * (temp - 32)

def toFahrenheit(temp):
    return (temp * (9/5)) + 32

#4. მოცემულ დიაპაზონში (1..n) ყველა მარტივი რიცხვის პოვნა
def isPrime(x):
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

#5. 1-დან n-მდე ყველა რიცხვის ჯამი
def sumAll(n):
    if n == 1:
        return 1
    return n + sumAll(n - 1)

#6. 1-დან n-მდე ყველა რიცხვის საშუალო არითმეტიკული
def average(n):
    sum = 0
    count = 0
    for i in range(1, n+1):
        sum += i
        count += 1
    return sum / count

#7. 1-დან n-მდე ყველა რიცივის კვადრატების ჯამი
def squareSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

#8. 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი
def evenSum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum

#9. ორი რიცხვის უმცირესი საერთო ჯერადი
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

#10. მოცემული რიცხვის ყველა გამყოფის პოვნა 
def allDivisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

#11.
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