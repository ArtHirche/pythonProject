#Exercício 1
"""
velocidadeMaxima = 80

velocidadeInserida = int(input("Qual a velocidade do veículo?"))

multa = float((velocidadeInserida - velocidadeMaxima) * 7)

if velocidadeMaxima > velocidadeInserida:
    print("Muito bem!")
elif velocidadeMaxima == velocidadeInserida:
    print("No limite, tome cuidado!")
else:
    print(f"\nInfelizmente será mutado\nPagará:R$ {multa}\nPor excesso de velocidade. Velocidade máxima: {velocidadeMaxima}")
"""
#Exercício 2

numeroInserido = int(input("Digite um número: "))

resto = numeroInserido % 2

if resto == 0:
    print("Seu número é par.")
else:
    print("Seu número é impar.")
