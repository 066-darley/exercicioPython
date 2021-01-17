# Verifica até números reais

while True: 
    n = float(input("\nDigite um número: "))
    if (n % 2 == 0) and n != 0:
        print(f"\n{n} é um número par")
        
    elif (n % 2 != 0):
        print(f"\n{n} é um número impar")
    
    if (n == 0):
        print("Programa encerrado! ")
        break
        