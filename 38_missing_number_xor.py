"""Program 38: Find the missing number using XOR."""


def missing_number(numbers):
    n = len(numbers) + 1
    result = 0

    for number in range(1, n + 1):
        result ^= number

    for number in numbers:
        result ^= number

    return result


if __name__ == "__main__":
    numbers = list(map(
        int, input("Enter numbers separated by spaces: ").split()
    ))
    print("Missing number:", missing_number(numbers))