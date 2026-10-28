"""Program 34: Check whether a list is sorted."""


def is_sorted(numbers):
    return all(
        numbers[i] <= numbers[i + 1]
        for i in range(len(numbers) - 1)
    )


if __name__ == "__main__":
    numbers = list(map(
        int, input("Enter numbers separated by spaces: ").split()
    ))

    if is_sorted(numbers):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")