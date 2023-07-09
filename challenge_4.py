phrase_4 = "hello, how are you? i'm, fine, thank you."
words_capitalize = []

words_2 = phrase_4.split()

for new_words in words_2:
    word_capitalize = new_words.capitalize()
    words_capitalize.append(word_capitalize)

new_phrase_4 = " ".join(words_capitalize)
print(new_phrase_4)