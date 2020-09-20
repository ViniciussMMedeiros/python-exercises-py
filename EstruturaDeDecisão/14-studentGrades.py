print("\t\tPrograma para calcular a média de um aluno a partir de duas notas e devolver o conceito atingido")

notaUm = float(input("\nDigite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))

media = (notaUm + notaDois) / 2

print(f"\n\nAs notas obtidas pelo aluno foram: Nota 1 = {notaUm} e Nota 2 = {notaDois}")
print("A média obtida foi = ", media)

if media >= 9.0 and media <= 10.0:
    print("O conceito obtido foi A e o aluno foi APROVADO!")
elif media >= 7.5 and media < 9.0:
    print("O conceito obtido foi B e o aluno foi APROVADO!")
elif media >= 6.0 and media < 7.5:
    print("O conceito obtido foi C e o aluno foi APROVADO!")
elif media >= 4.0 and media < 6.0:
    print("O conceito obtido foi D e o aluno foi REPROVADO!")
elif media >= 0 and media < 4.0:
    print("O conceito obtido foi E e o aluno foi REPROVADO!")
