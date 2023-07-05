#Desafio 1

phrase_1 = "Hello, World! OpenAI is amazing"
words = phrase_1.split() #dividi a frase em palavras pelo espaço criando uma lista
words.reverse() #inverte as palavras da lista
inverted_phrase = " ".join(words) # cria uma nova string com as palavras invertidas 
print(inverted_phrase)



#Desafio 2 

from collections import OrderedDict 

phrase_2 = "Hello, World!"
removed_duplicated_chars = "".join(OrderedDict.fromkeys(phrase_2)) # é criado um dictionary atraves do metodo fromkeys() removendo as duplicatas e refeita a string atraves do .join()

print(removed_duplicated_chars) 

#desafio 5

phrase_5 = "racecar"
inverted_phrase_5 = phrase_5[::-1] #inverte a string

if phrase_5 == inverted_phrase_5:
    print(True)
else:
    print(False)