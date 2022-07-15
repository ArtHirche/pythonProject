""""
Variaveis são espaços de alocamento na memória

int

float

str

bool

"""

nome = "Arthur"
idade = 17
sexo = "M"

#Exemplos:
# print("Olá, meu nome é", nome, "minha idade é", idade)
#print("Olá, meu nome é {}\n Eu tenho {} anos".format(nome, idade))
#print(f"Olá, meu nome é {nome}\nEu tenho {idade} anos e meu sexo é {sexo}")

"""pi = 3.14
parte_inteira = int(pi)"""
#Exemplos:
#print(f"O valor de pi é {pi}\n A parte inteira de pi é {parte_inteira}")

pi = 3.14

print(f"Pi antes valia : {pi}\nE seu tipo é {type(pi)}")
pi = int(pi)

print(f"Agora pi vale : {pi}\nE seu tipo é {type(pi)}")

pi = str(pi)

print(f"Pi agora é uma string, e seu tipo é {type(pi)}y")