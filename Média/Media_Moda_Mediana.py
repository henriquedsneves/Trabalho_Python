import statistics

# Pergunta quantas notas serão digitadas
qtd = int(input("Quantas notas você quer calcular? "))

notas = []

# Coleta as notas
for i in range(1, qtd + 1):
    nota = float(input(f"Digite a {i}ª nota: "))
    # esse append adiciona a nota na lista
    notas.append(nota)

# Cálculos
media = statistics.mean(notas)
mediana = statistics.median(notas)

# A moda pode dar erro se não existir (exemplo: todas diferentes),
# por isso tratamos com try/except
try:
    moda = statistics.mode(notas)
except statistics.StatisticsError:
    moda = "Não existe moda (todos valores diferentes)"

# Resultados
print("\n--- Resultados ---")
print(f"Notas digitadas: {notas}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
