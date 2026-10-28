"""Program 32: Count words in a sentence."""


def count_words(sentence):
    return len(sentence.split())


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Number of words:", count_words(text))