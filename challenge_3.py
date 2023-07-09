phrase_3 = "babad"
palindrome_long_word_in_string = ""

for i in range(len(phrase_3)): #percorre a string 
    left, right = i, i # inicializa 2 ponteiros para percorrer a string 
    while left >= 0 and right < len(phrase_3) and phrase_3[left] == phrase_3[right]: # esse laço percorre a string até o centro, utilizei o debug, e monta uma string
        left -= 1
        right += 1
    if len(phrase_3[left + 1:right]) > len(palindrome_long_word_in_string):
        palindrome_long_word_in_string = phrase_3[left + 1:right]

    left, right = i, i + 1
    while left >= 0 and right < len(phrase_3) and phrase_3[left] == phrase_3[right]:  # esse laço é usado para encontrar palindromos comparando com o primeiro laço
        left -= 1
        right += 1
    if len(phrase_3[left + 1:right]) > len(palindrome_long_word_in_string):
        palindrome_long_word_in_string = phrase_3[left + 1:right]

print(palindrome_long_word_in_string)
