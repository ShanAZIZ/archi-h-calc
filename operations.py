def addition(number1, number2):
    return number1 + number2

def multiplication(number1, number2):
    return number1 * number2

operations = {
    "+": {
        "end_display": "addition",
        "op_function": addition,
    },
    "*": {
        "end_display": "mulitplication",
        "op_function": multiplication
    }
}

def operate(numbers, operation):
    output = ""
    output += tabulated_string(numbers[0])
    final = numbers[0]
    for number in numbers[1:]:
        final = operations[operation]["op_function"](final, number)
        display = operation_line_display(operation, number, final)
        output += display
    output += end_bar(len(display))
    output += f"total = {final} ({operations[operation]["end_display"]})"
    return output

def operation_line_display(operation, number, final):
    return tabulated_string(f"{operation}{number} (={final})")

def end_bar(lenght):
    end_bar = ""
    for i in range(lenght):
        end_bar += "-"
    return tabulated_string(end_bar)


def tabulated_string(string):
    return f"\t{string}\n"