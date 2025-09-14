# Programa para calcular o IMC

# Entrada de dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado
print(f"\nSeu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3 (mórbida)")
