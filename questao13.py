soma = 0
for i in range(5):
    numeros = float(input(f"Digite o {i + 1}° número: "))
    soma+=numeros
    media = soma/5
print(f"A soma dos números digitaos é {soma}\nA média dos números somados é {media}") 