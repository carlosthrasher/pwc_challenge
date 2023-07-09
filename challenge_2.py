#Desafio 2 

from collections import OrderedDict 

phrase_2 = "Hello, World!"
removed_duplicated_chars = "".join(OrderedDict.fromkeys(phrase_2)) # é criado um dictionary atraves do metodo fromkeys() removendo as duplicatas e refeita a string atraves do "".join()

print(removed_duplicated_chars) 
