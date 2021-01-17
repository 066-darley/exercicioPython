lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    n = float(input("Digite uma nota entre 0 e 10: "))
    
    if n in lista:
        print(f"Nota informada = {n}")
        break
    
    elif n not in lista:
        print("Nota inválida")
            