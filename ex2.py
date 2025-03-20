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

# Atividade 8: Salario com aumento de 25%
valorSalario = float(input('Qual o seu salario: '))
porcentagemAumento = 25/100
salarioFinal = valorSalario + (valorSalario * porcentagemAumento)
print(f'O valor do salario final com o aumento de 25% é igual a {salarioFinal})')

# Atividade 9: Dividir entre 3 ganhadores
a = 46 
b = 32
c = 22
importancia = 780000

print('A importância no valor de R$ 780.000,00, será dividida entre três ganhadores')

primeiroGanhador = importancia * (a / 100)
segundoGanhador = importancia * (b / 100)
terceiroGanhador = importancia * (c / 100)
print(f"O primeiro ganhador vai receber o valor de R$ {primeiroGanhador} - o Segundo ganhador {segundoGanhador} o Terceiro vai receber {terceiroGanhador}")

# Atividade 10: Contrata um serviço do encanador 
encanadorValor = 80
qtDias = int(input("Quantos dias o encanador trabalhou: "))
encanadorSalario = encanadorValor * qtDias
print(encanadorSalario)

imposto = (8 / 100) * encanadorSalario 
print(imposto)
salarioFinal = encanadorSalario - imposto
print(f"O valor final que o encanador vai receber, já descontando o imposto R${salarioFinal}")

# Atividade 11: Uma padaria 
valorPao = 0,38 
valorBroa = 4,50

qtPaoDia = int(input('Quantos pães francesses são vendidos no dia: '))
qtBroaDia = int(input('Quantas broa são vendidas em um dia :'))
somaVendas = qtPaoDia + qtBroaDia
print(f"O valor total vendido em um dia foi de {somaVendas}")

reserva = somaVendas * 0.10
print(f"Ele precisa reservar {reserva} do valor das vendas! ")