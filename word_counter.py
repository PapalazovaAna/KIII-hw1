def count_words(text):
    words = text.split()
    return len(words)


if __name__ == "__main__":
    user_text = input("Внеси некој текст: ")

    word_count = count_words(user_text)
    print(f"Текстот содржи {word_count} зборови.")