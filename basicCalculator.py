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

if __name__ == '__main__':
    print(calculator(4,"/",3))