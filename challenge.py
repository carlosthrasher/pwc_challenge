#Desafio 1

phrase_1 = "Hello, World! OpenAI is amazing"
words = phrase_1.split()
words.reverse()
inverted_phrase = " ".join(words)
print(inverted_phrase)



#Desafio 2 

from collections import OrderedDict 

phrase_2 = "Hello, World!"
removed_duplicated_chars = "".join(OrderedDict.fromkeys(phrase_2))

print(removed_duplicated_chars) 