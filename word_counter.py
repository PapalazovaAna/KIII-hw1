def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    return len(text.replace(" ", ""))


if __name__ == "__main__":
    user_text = input("Внеси некој текст: ")

    word_count = count_words(user_text)
    print(f"Текстот содржи {word_count} зборови.")

    letter_count = count_letters(user_text)
    print(f"Текстот содржи {letter_count} букви.")