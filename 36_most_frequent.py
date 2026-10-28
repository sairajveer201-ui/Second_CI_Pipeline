"""Program 36: Find the most frequent element in a list."""


def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return max(numbers, key=lambda number: counts[number])


if __name__ == "__main__":
    numbers = list(map(
        int, input("Enter numbers separated by spaces: ").split()
    ))
    print("Most frequent element:", most_frequent(numbers))