"""Program 35: Move all zeros to the end."""


def move_zeros(numbers):
    non_zeros = [number for number in numbers if number != 0]
    zeros = [number for number in numbers if number == 0]
    return non_zeros + zeros


if __name__ == "__main__":
    numbers = list(map(
        int, input("Enter numbers separated by spaces: ").split()
    ))
    print("Result:", move_zeros(numbers))