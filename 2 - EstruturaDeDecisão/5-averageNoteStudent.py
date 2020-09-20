# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

note1 = float(input("Enter the first note: "))
note2 = float(input("Enter the second note: "))

average = (note1 + note2) / 2.0

print(f"Average = {average:0.2f}")

if average >= 7.0:
    print("Passed!")
elif average < 7.0:
    print("Failed!")
elif average == 10:
    print("Passed with distinction!")
else:
    print("Error.")
