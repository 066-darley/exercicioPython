lista = []

while True:
    n = float(input("\n(1) - Para adicionar números ao conjunto:\n(2) - Mostrar conjunto de número e sua soma\n(3) - para encerrar o programa: "))
    if n == 1:
        n1 = float(input("\nDigite Número para adicionar no conjunto: "))
        lista.append(n1)
    elif n == 2:
        soma = sum(lista)
        print(f"\nO conjunto de número é {lista}. e a soma dos elementos do conjunto N é {soma} ")
        
    elif n == 3:
        print("Programa encerrado!")
        break
    
   