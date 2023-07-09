#Desafio 1

phrase_1 = "Hello, World! OpenAI is amazing"
words_1 = phrase_1.split() #dividi a frase em palavras pelo espaço criando uma lista
words_1.reverse() #inverte as palavras da lista
inverted_phrase = " ".join(words_1) # cria uma nova string com as palavras invertidas 
print(inverted_phrase)
