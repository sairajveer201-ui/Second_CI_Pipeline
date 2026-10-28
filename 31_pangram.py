"""Program 31: Check whether a sentence is a pangram."""


def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(sentence.lower())
    return alphabet.issubset(letters)


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    if is_pangram(text):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")