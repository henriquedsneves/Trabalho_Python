# Conversor de Dólar para Real

# Entrada da cotação
cotacao = float(input("Digite a cotação atual do dólar: "))

# Entrada do valor em dólares
dolar = float(input("Digite o valor em dólares: "))

# Conversão
real = dolar * cotacao

# Saída formatada
print(f"US$ {dolar:.2f} equivale a R$ {real:.2f}")
