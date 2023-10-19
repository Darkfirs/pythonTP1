import math as m

def float_numbers(coefficient):
    try:
        float(coefficient)
        return True
    except ValueError:
        return False


def select_formula(a, b, c):
    if a != 0:
        return tuple(sorted(solution_quadratic(a, b, c)))
    elif b != 0:
        return solution_linear(b, c)
    return solve_constant_equation(c)


def solution_quadratic(a, b, c):
    d = b**2 - 4 * a * c
    if d == 0:
        return (-b / (2 * a), )
    elif d > 0:
        return [(-b + m.sqrt(d)) / (2 * a), (-b - m.sqrt(d)) / (2 * a)]
    raise ArithmeticError("Discriminant must be non-negative")


def solution_linear(b, c):
    return (-c / b, )


def solve_constant_equation(c):
    if c != 0:
        raise ArithmeticError("No solutions")
    raise ArithmeticError("Infinitely many solutions")


def checking_arguments(numbers):
    numbers = numbers.split()
    if len(numbers) != 3:
        raise ValueError("Not 3 arguments were entered")
    elif any(not float_numbers(i) for i in numbers):
        raise ValueError("Enter a float number")
    return tuple((float(i) for i in numbers))


def main():
    arguments = input("Enter three float numbers a, b, c: ")
    try:
        arguments = checking_arguments(arguments)
        print(f"Solution:", *select_formula(*arguments))
    except ValueError as e:
        print(str(e))
    except ArithmeticError as e:
        print(str(e))


if __name__ == "__main__":
    main()
