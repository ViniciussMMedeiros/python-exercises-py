print("\t\tPrograma para verificar a existência de um triângulo e indicar o tipo dele")

ladoUm = float(input("\nDigite o primeiro lado do triângulo: "))
ladoDois = float(input("Digite o segundo lado do triângulo: "))
ladoTres = float(input("Digite o terceiro lado do triângulo: "))

if ladoUm + ladoDois > ladoTres and ladoDois + ladoTres > ladoUm and ladoUm + ladoTres > ladoDois:
  if ladoUm == ladoDois and ladoDois == ladoTres:
    print("Os lados foram um triângulo equilátero!")
  elif ladoUm == ladoDois or ladoDois == ladoTres or ladoUm == ladoTres:
    print("Os lados formam um triângulo isósceles!")
  else:
    print("Os lados formam um triângulo escaleno!")
else:
  print("Os lados não formam um triângulo")
