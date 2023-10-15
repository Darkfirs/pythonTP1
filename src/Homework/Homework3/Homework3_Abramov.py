import sys


def curry_explicit(function, arity):
    def check(arguments):
        def curry_function(arg):
            return check([*arguments, arg])

        if arity == len(arguments):
            return function(*arguments)
        return curry_function

    if arity < 0:
        sys.exit("Отрицательная арность невозможна")
        return 0
    elif arity == 0:
        return function()
    arg_list = []
    return check(arg_list)


def uncurry_explicit(function, arity):
    if arity < 0:
        sys.exit("Отрицательная арность невозможна")

    def uncurry_function(*args):
        if len(args) == 1 or len(args) == 0:
            return function(*args)
        res = function(args[0])
        for i in range(1, arity):
            res = res(args[i])
        return res

    return uncurry_function


if __name__ == "__main__":
    f2 = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    print(f2(123)(456)(562))
    g2 = uncurry_explicit(f2, -3)
    print(g2(123, 456, 562))