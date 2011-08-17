s = "parabens!"
l = list(s) # cria lista com cada caracter da string s
print l
l2 = [ord(x) for x in l] # cria uma lista com o código numérico de cada caracter da list l
print l2
l3 = [chr(x) for x in l2] # cria uma lista com a caracter de cada código numérico da lista l2 
print l3
s2 = "".join(l3) # transforma a lista l3 em uma string
print s2
