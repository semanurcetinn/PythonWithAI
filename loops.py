numbers = []
for i in range(1,101):
    numbers.append(i)
print(f"numbers: {numbers}")

print("***********************")
evenNumbers = []
for i in range(1,101):
    if i % 2 == 0:
        evenNumbers.append(i)
print(f"even numbers: {evenNumbers}")

print("***********************")

primeNumbers = []
for i in range(2, 101):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primeNumbers.append(i)
print(f"prime numbers: {primeNumbers}")

print("***********************")

number = int(input("Enter a number:"))
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(number))
