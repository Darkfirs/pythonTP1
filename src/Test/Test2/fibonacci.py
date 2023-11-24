def fibonacci(n):
    if n < 0 or n > 90:
        raise ValueError("n must be between 0 and 90")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def check_enter(n):
    if not n.isdigit():
        print("You must enter integer number")
        return False
    n = int(n)
    if not(0 <= n <= 90):
        print("You must enter number between 0 and 90")
        return False
    return True


def main():
    number = input("Enter number(between 0 and 90):")
    if check_enter(number):
        return print(fibonacci(int(number)))


if __name__ == "__main__":
    main()
