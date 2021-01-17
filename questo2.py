# Questão 02 com menos linha de código

lista = []
for i in range(3):
    n = int(input(f"Digite o {i + 1}° número: "))
    lista.append(n)
    maior = lista[0]
    menor = lista[0]


menor = lista[0]
for i in lista:
    if i < menor:
        menor = i
        
maior = lista[0]
for i in lista:
    if i > maior:
        maior = i
        
print(f"O maior número é {maior} e o menor é {menor}")
        

