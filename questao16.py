# 16. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
# fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores
# que 16.
def numeroInt(msn):
    ok = False
    valor = 0
    while True:
        n = str(input(msn))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("DIGITE UM NÚMERO INTEIRO!")
        if ok:
            break
    return valor


fatorial = 1
while True:
    n = numeroInt("Digite um número inteiro para calcular o fatorial: ")
    
    if (n >= 16):
        print("DIGITE NÚMEROS INTEIRO MENORES QUE 16!")
        
    

    elif (n < 16):
        for i in range(n):
            fatorial = fatorial * n
            n-=1
        print(f"O FATORIAL DO NÚMERO {i + 1} É = {fatorial}")
            