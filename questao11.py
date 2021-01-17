# Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
# conceitos obedece à tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E

nota = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota 2: "))

media = (nota + nota2)/2

if (media >= 9 and media <= 10 ):
    print("Média de Aproveitamento | Conceito\nEntre 9.0 e 10.0             A ")
    
elif (media >=7.5 and media < 9):
    print("Média de Aproveitamento | Conceito\nEntre 7.5 e 9.0             B ")

elif (media >=6.0 and media < 7.5 ):
    print("Média de Aproveitamento | Conceito\nEntre 6.0 e 7.5             C ")
    
elif (media >=4.0 and media < 6.0):
    print("Média de Aproveitamento | Conceito\nEntre 4.0 e 6.0             D ")

elif (media >= 0 and media < 4):
    print("Média de Aproveitamento | Conceito\nEntre 4.0 e Zero             E ")
    
    