def print_upper_words (words_arr, must_start_with):
    uppercase_words = []
    for word in words_arr:
        uppercase_word = word.upper()
        starts_with = any(uppercase_word.startswith(letter) for letter in must_start_with)
    if starts_with:
        uppercase_words.append(uppercase_word)

    print(uppercase_words)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
