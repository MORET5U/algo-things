import random


def binary_search(arr: list[int], item: int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = arr[mid]

        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1

        else:
            low = mid + 1


data = sorted(range(100000000))

secret_number = random.choice(data)
print(f"The secret number is {secret_number}")

res = binary_search(data, secret_number)
print(f"Binary search result is {res}")
