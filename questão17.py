resulta = 1
n = int(input("Digite um número inteiro entre 1 e 10 para calcular a tabuada: "))
for i in range(n):
    resulta = n * (i + 1)
    print(f"{n} * {i + 1}  = {resulta}")