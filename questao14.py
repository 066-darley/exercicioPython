# 14. Faça um programa que peça um número inteiro e determine se ele é ou não
# um número primo. Um número primo é aquele que é divisível somente por ele
# mesmo e por 1.

n = int(input("Digite um número INTEIRO: "))

primo = True

divisor = 2

while divisor < n and primo:
        if n % divisor == 0:
            primo = False
        divisor += 1
  
if primo and n != 1:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")