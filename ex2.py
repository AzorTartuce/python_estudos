# Atividade 1: Valor do produto com desconto:
valorProduto = float(input('Digite o valor do produto: '))
valorDesconto = valorProduto * (12 / 100)
print(valorDesconto)

# Atividade 2: Transformar o valor em minuto / segundos / horas
receberValor = int(input('Digite o valor em Segundos! '))

valorMinutos = receberValor // 60
valorHora = receberValor // 3600
print(f"Valor em minutos {valorMinutos:.2f}")
print(f"Valor em horas {valorHora:.1f}")

# Atividade 3: Atividade da Granja
qtDeFrango = int(input('Quantida de frango na fazenda: '))
calcularFrango = qtDeFrango * 1.1
print(f"O valor dos frangos na fazenda é igual a {calcularFrango}")

# Atividade 4: Conversor de Dolar
valorConverter = float(input('Qual valor você gostaria de converter em dolar: '))
valorDolar = 5.6

conversor = valorConverter * valorDolar
print(f"R$ {conversor} em dolar fica {valorConverter}")

# Atividade 5: Escrever um algoritimo de numeros de votos
numerosBrancos = int(input('Qual o número de votos em brancos nas eleições: '))
numeroNulo = int(input('Qual o número de votos nulos nas eleições: '))
numeroValido = int(input('Qual o número de votos validos nas eleições: '))

valorTotal = numeroNulo  + numerosBrancos + numeroValido

print(f'Quantidade total de votos {valorTotal}')

porcentagemBrancons = (numerosBrancos / valorTotal) * 100
porcentagemNNulo = (numeroNulo / valorTotal) * 100
porcentagemValido = (numeroValido / valorTotal) * 100

print(f'A porcentagem de votos em Brancos foi {porcentagemBrancons} % de votos Nulos {porcentagemNNulo} % em votos validos for {porcentagemValido} %')

# Atividade 6: Calcular o valor com a formula pi
pi = 3.1415
valorRaio = float(input('Qual o valor do raio: '))
calcularRaio = pi * (valorRaio ** 2)
print(f'Valor do raio igual a {calcularRaio}')

# Atividade 7: Custo ao consumidor
custoFabrica = float(input('Qual o valor de fabrica do veiculo: '))
distribuidor = 28 / 100
impostos = 45 / 100

valorFinalConsumidor = custoFabrica * (distribuidor + impostos)

print(f'O custo final do carro para o consumidor ficou igual a {valorFinalConsumidor}')
