def increment_addition(numbers):
    print(tabulated_string(numbers[0]))
    final = numbers[0]
    for number in numbers[1:]:
        final = final + number
        display = tabulated_string(f"+{number} (={final})")
        print(display)
        last_lenght = len(display)
    end_bar = ""
    for i in range(last_lenght):
        end_bar += "-"
    print(tabulated_string(end_bar))
    print(f"total = {final} (addition)")


def increment_multiplication(numbers):
    print(tabulated_string(numbers[0]))
    final = numbers[0]
    for number in numbers[1:]:
        final = final * number
        display = tabulated_string(f"*{number} (={final})")
        print(display)
        last_lenght = len(display)
    end_bar = ""
    for i in range(last_lenght):
        end_bar += "-"
    print(tabulated_string(end_bar))
    print(f"total = {final} (multiplication)")

def output(numbers, operation):
    match operation:
        case "+":
            increment_addition(numbers)
        case "*":
            increment_multiplication(numbers)

def tabulated_string(string):
    return f"\t{string}"