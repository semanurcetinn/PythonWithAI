number = int(input("Enter a number:"))

if number%2 == 0:
    print("The number you entered is even.")
else:
    print("the number you entered is odd.")

print("***********************")

grade = int(input("Enter your grade:"))

if 90 <= grade <= 100:
    print("Your grade: A")
elif 80 <= grade <= 89:
    print("Your grade: B")
elif 70 <= grade <= 79:
    print("Your grade: C")
elif 60 <= grade <= 69:
    print("Your grade: D")
else:
    print("Your grade: F")

print("***********************")

age = int(input("Enter your age:"))

if age > 60:
    print("You are old.")
elif 20 <= age <= 59:
    print("You are adult.")
elif 13 <= age <= 19:
    print("You are young.")
else:
    print("You are child.")