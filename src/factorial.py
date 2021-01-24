import math
from timeit import timeit


def fact(x: int):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print("3! is {}".format(fact(3)))

# but actaully what's tje point if math module exists?
# also you won't be able to go for fact(1000) because RecursionError
builtin_time = timeit(lambda: math.factorial(900), number=1000)
custom_time = timeit(lambda: fact(900), number=1000)

print("==== Running built-in vs handwritten function ===")
print(f"+{'-' * 14}+{'-' * 12}+")
print("| {:^12} | {:^10} |".format("built-in", "{:.4f} ms".format(builtin_time)))
print("| {:^12} | {:^10} |".format("handwritten", "{:.4f} ms".format(custom_time)))
print(f"+{'-' * 14}+{'-' * 12}+")
