# Programa para calcular a média de notas

# Quantas notas o usuário vai digitar
qtd = int(input("Quantas notas você quer calcular? "))

soma = 0

# Loop para pegar as notas
for i in range(1, qtd + 1):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

# Cálculo da média
media = soma / qtd

# Resultado
print(f"A média das {qtd} notas é: {media:.2f}")

# Situação (opcional)
if media >= 7:
    print("Situação: Aprovado ")
elif media >= 5:
    print("Situação: Recuperação ")
else:
    print("Situação: Reprovado ")
