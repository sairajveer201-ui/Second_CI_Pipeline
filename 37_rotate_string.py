"""Program 37: Rotate a string right by k positions."""


def rotate_string(text, k):
    if not text:
        return text

    k = k % len(text)
    return text[-k:] + text[:-k] if k else text


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation positions: "))
    print("Rotated string:", rotate_string(text, k))