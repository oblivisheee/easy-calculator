import os
import re
import time
settings = {
    'delay_calc': 10,
    'use_clr': True,
    'exit_delay': 3,
}
use_delay = None
while True:
    if settings['delay_calc'] == None:
        use_delay = False
    print("Expression like: 5 * 8 ")
    print('Write "Quit" for exiting.')
    expression = input("Write down your math expression: ").replace(" ", "")

    if expression.lower() == "quit":
        print("Exiting...")
        time.sleep(int(settings["exit_delay"]))
        break

    operator_multiply = "*" in expression
    operator_devide = "/" in expression
    operator_minus = "-" in expression
    operator_plus = "+" in expression

    if not any([operator_multiply, operator_devide, operator_minus, operator_plus]):
        raise Exception("Invalid expression")

    numbers = [float(num) if '.' in num else int(num) for num in re.findall(r'[-+]?\d*\.\d+|\d+', expression)]

    if len(numbers) < 2:
        raise Exception("Invalid expression: Not enough numbers found.")

    result = None

    if operator_multiply:
        result = numbers[0]
        for num in numbers[1:]:
            result *= num
    elif operator_devide:
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    elif operator_minus:
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif operator_plus:
        result = sum(numbers)

    if settings['use_clr']: os.system('clear')
    print("Answer of expression:", result)
    if not use_delay is False: time.sleep(int(settings["delay_calc"]))
    if settings['use_clr'] and not use_delay is False: os.system('clear')