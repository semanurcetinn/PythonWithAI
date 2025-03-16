from typing import Union, AnyStr
def calculator(number1, action, number2) -> Union[float, AnyStr]:
    """
    sema nur
    :param number1:
    :param action:
    :param number2:
    :return:
    """

    if action == "+":
        return number1 + number2
    elif action == "-":
        return number1 - number2
    elif action == "*":
        return number1 * number2
    elif action == "/":
        if number2 == 0:
            print("The second number for the division operation cannot be 0!")
        return number1 / number2
    else:
        return "Invalid transaction type!"

def isPalindrome(word):
    if word == word[::-1]:
        return "The entered word is a palindrome."
    else:
        return "The entered word is not a palindrome"

def yearCalculator(age):
    if age < 0:
        return "Age is not negative."
    elif age >= 100:
        return "Age is already 100 years old or older."

    year = 100 - age
    return f"You will reach the age of 100 in {year} years."

if __name__ == '__main__':
    print(calculator(4,"/",3))
    print(isPalindrome("madam"))
    print(yearCalculator(21))