lista = []
acumulador = 0
nomeAtleta = input("Atleta: ")
for i in range(7):
    nota = float(input(f"{i + 1}° Nota: "))
    lista.append(nota)
    acumulador+=nota
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
        
    media = acumulador - (maior + menor)
    mediaFinal = media/5
       
print(f"Resultado final:\nMelhor nota: {maior}\nPior nota: {menor}\nMédia {round(mediaFinal, 2)} ")