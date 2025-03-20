# Atividade 1:
nome = input('Digite seu nome: ')
print(f"Olá {nome}")

# Atividade 2:
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite outro valor: '))

soma = numero1 + numero2
multiplicar = numero1 * numero2

print(f'A soma dos valores {numero1} + {numero2} é igual a {soma}')
print(f'A multiplicação dos valores {numero1} x {numero2} é igual a {multiplicar}')

# Atividade 3: Nota de alunos
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua outra nota: '))
nota3 = float(input('Digite sua última nota: '))

def somarCalcular(nota1, nota2, nota3):
    somarNota = nota1 + nota2 + nota3
    dividirNota = somarNota / 3
    return dividirNota

mostrarNotaTela = somarCalcular(nota1, nota2, nota3)
print(mostrarNotaTela)

# Atividade 4: Temperatura
c = float(input('Digite a temperatura em graus Celsius: '))
print("A temperatura em Celsius vai ser convertida em Fahrenheit")
f = c * 1.8 + 32
print(f)

# Atividade 5: Calculadora IMC
print('Calculadora IMC!')
digitePeso = float(input('Digite seu peso (kg): '))
digiteAltura = float(input('Digite sua altura (m): '))
calcularIMC = digitePeso / (digiteAltura ** 2)
print(calcularIMC)

# Atividade 6: Triângulo
print('Calcular a área de um triângulo! ')
baseTriangulo = float(input('Escreva a base de um triângulo: '))
alturaTriangulo = float(input('Escreva a altura de um triângulo: '))
area = (baseTriangulo * alturaTriangulo) / 2
print(area)

# Atividade 7: Desconto de 10%
valorProduto = float(input('Digite o valor do produto: '))
descontoProduto = valorProduto * 0.10
print(f'O desconto foi de {descontoProduto}')

# Atividade 8: Salário com aumento
""""

200 reais por carro vendido 
2% do total das vendas de carro 

"""
salario = 2500
comisao = 200


nomeVendedor = input('Qual o nome do vendedor: ')
qtCarrosVendidos = int(input('Quantidades de carros vendidos: '))
valorVendasTotal = float(input('Qual o valor total das vendas: '))

comissaoCalcular = qtCarrosVendidos * comisao
# Comissão + salario
comissaoVendas = valorVendasTotal * 0.2

# Adicionar os 2% das vendas gerais de carro
salarioFinal = salario + comissaoCalcular + comissaoVendas

print(salarioFinal)

# Atividade 9: A e B
valorA = float(input("Digite um valor qualquer: "))
valorB = float(input("Digite um valor qualquer: "))

valorC = valorA
valorD = valorB
valorA = valorD
valorB = valorC


print(f"Valor A = {valorA}")
print(f"Valor B = {valorB}")

# Atividade 10: Inverter o Número digitado 
valor1 = int(input("Digite um valor qualquer: ")) 
valor2 = int(input("Digite um valor qualquer: ")) 
valor3 = int(input("Digite um valor qualquer: "))

numeros = [valor1, valor2, valor3]

print("Números na ordem inversa: ", numeros[::-1])