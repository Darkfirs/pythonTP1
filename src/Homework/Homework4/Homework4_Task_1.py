def binary_representation(number):
    if number == 0:
        return [0, 0]
    elif number > 0:
        bit = []
        symbol = [0, 0]
    else:
        bit = []
        number = number * (-1)
        symbol = [1, 0]
    while number > 0:
        bit.append(number % 2)
        number = number // 2
    return symbol + bit[::-1]


def reverse_number_code(number):
    if number[0] == 0:
        return number
    else:
        for i in range(1, len(number)):
            if number[i] == 0:
                number[i] = 1
            elif number[i] == 1:
                number[i] = 0
        return number


def additional_number_code(number):
    if number[0] == 0:
        return number
    else:
        for i in range(len(number) - 1, 0, -1):
            if number[i] == 0:
                return number[:i] + [1] + [0] * (len(number) - i - 1)


def change_numbers(number1, number2, negative_number):
    n1 = number1
    n2 = number2
    ng = negative_number
    if len(n1) > len(n2):
        n2 = [n2[0]] + [0] * (len(n1) - len(n2)) + n2[1:]
        ng = [ng[0]] + [0] * (len(n1) - len(ng)) + ng[1:]
        return n1, n2, ng
    elif len(n2) > len(n1):
        n1 = [n1[0]] + [0] * (len(n2) - len(n1)) + n1[1:]
        return n1, n2, ng
    else:
        return n1, n2, ng


def creat_working_number(number1, number2):
    bin_code1 = binary_representation(number1)
    bin_code2 = binary_representation(number2)
    bin_negative_code = binary_representation(-number2)
    bin_code1, bin_code2, bin_negative_code = change_numbers(
        bin_code1, bin_code2, bin_negative_code
    )
    reverse_code1 = reverse_number_code(bin_code1)
    reverse_code2 = reverse_number_code(bin_code2)
    reverse_negative_code = reverse_number_code(bin_negative_code)
    additional_code1 = additional_number_code(reverse_code1)
    additional_code2 = additional_number_code(reverse_code2)
    additional_negative_code = additional_number_code(reverse_negative_code)
    return additional_code1, additional_code2, additional_negative_code


def calculate_sum(number1, number2):
    result = []
    count = 0
    for i in range(len(number1) - 1, -1, -1):
        if number1[i] + number2[i] + count == 0:
            count = 0
            result.append(0)
        elif number1[i] + number2[i] + count == 1:
            count = 0
            result.append(1)
        elif number1[i] + number2[i] + count == 2:
            count = 1
            result.append(0)
        else:
            count = 1
            result.append(1)
    result = result[::-1]
    return result


def speaker_to_output(bin_number1, bin_number2, bin_reverse, number1, number2):
    bin_number1_string = "".join(map(str, bin_number1))
    print("The first number in binary form:", bin_number1_string)
    bin_number2_string = "".join(map(str, bin_number2))
    print("The second number in binary form:", bin_number2_string)
    print("The sum in binary form:")
    bin_sum = "".join(map(str, calculate_sum(bin_number1, bin_number2)))
    print(f"{bin_number1_string} + {bin_number2_string} = {bin_sum}")
    print("The difference in binary form:")
    difference = "".join(map(str, calculate_sum(bin_number1, bin_reverse)))
    print(f"{bin_number1_string} - {bin_number2_string} = {difference}")
    print("The sum in decimal form:")
    print(f"{number1} + {number2} = {number1 + number2}")
    print("The difference in decimal form:")
    print(f"{number1} - {number2} = {number1 - number2}")


if __name__ == "__main__":
    first_number = int(input("First number:"))
    second_number = int(input("Second number:"))
    first_code, second_code, second_reverse_code = creat_working_number(
        first_number, second_number
    )
    speaker_to_output(
        first_code, second_code, second_reverse_code, first_number, second_number
    )
