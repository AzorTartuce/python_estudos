# Receber Nota de um Aluno e verificar se ele foi aprovado ou reprovado
print("1 - Verificar a nota de um aluno")
print("2 - Verificar se um número é par ou ímpar")
print("3 - Verificar se um número é positivo ou negativo")
print("4 - Identificar se uma letra é vogal ou consoante")
print("5 - Verificar se um número é positivo, negativo ou zero")
print("6 - Exibir um número no formato de horas")
print("7 - Exibir o maior número ou indicar se são iguais")
print("8 - Exibir o menor número ou indicar se são iguais")
print("9 - Verificar o tipo de triângulo a partir de três valores")
print("10 - Calcular salário fixo com comissões por venda")
opcao = int(input('Escolha uma das opção acima: '))

print('----------------------------------------------------')

def verificarNota():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    calcularNota = (nota1 + nota2 + nota3) / 3

    if calcularNota >= 6:
        print('Aprovado na escola! ')
    else:
        print('reprovado! ')

    return calcularNota

def numeroParImpar():
    num1 = int(input('Digite um número: '))

    if num1 % 2 == 0:
        print('Número é Par')
    else:
        print('Número Impar')

def numeroPositivoNegativo():
    numero = int(input('Digite um valor qualquer: '))

    if numero < 0:
        numero *= -1 

    print(numero)

def vogalConsoante():
    digiteLetra = input('Digite uma letra: ')

    if digiteLetra == "a" or "e" or "i" or "o" or "u":
        print(f'A letra digitada é uma consoante {digiteLetra}')
    else:
        print(f'A letra escolida {digiteLetra}')

def numeroTipo():
    receberNumero = int(input('Digite um número: '))

    if receberNumero == 0:
        print('Você digitou o número 0')
    elif receberNumero < 0:
        print('O número que você digitou é negativo')
        print(f'Número digitado foi {receberNumero}')
    elif receberNumero >= 1:
        print('Você digitou um número positivo')
        print(f'Número digitado foi {receberNumero}')

def receberHora():
    numeroHora = int(input('Digite um número inteiro: '))
    numeroMin = int(input('Digite outro número inteiro: '))

    if numeroHora >= 0 and numeroMin <= 59:
        print(f'Agora são {numeroHora} : {numeroMin}')
    else:
        print('Digite um número valido! ')

def numeroMaior():
    receberNum1 = float(input('Digite um valor: '))
    receberNum2 = float(input('Digite outro valor: '))

    if receberNum1 > receberNum2:
        print(f'O {receberNum1} é maior que {receberNum2}')
    elif receberNum2 > receberNum1:
        print(f'O número {receberNum2} é maior que {receberNum1}')
    elif receberNum1 == receberNum2:
        print('Os números digitados são iguais! ')
    else:
        print('Digite um valor valido! ')

def menorNumeroTela():
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    numero3 = float(input('Digite outro valor: '))

    if numero1 == numero2 == numero3:
        print('Todos os números são iguais! ')
    else:
        menor = min(numero1, numero2, numero3)
        print(f'O menor número é {menor}')

def ladosTriangulo():
    a = float(input('Digite o primeiro lado do triângulo: '))
    b = float(input('Digite o segundo lado do triângulo: '))
    c = float(input('Digite o terceiro lado do triângulo: '))

    if a == b == c:
        print('O triângulo é equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo isóceles')
    else:
        print('Triângulo escaleno')

def calcular_salario():
    vendedor = input("Digite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo do vendedor: "))
    valor_vendas = float(input(f"Digite o total de vendas do {vendedor}: "))

    # Comissão de 3% sobre as vendas
    comissao = (3 / 100) * valor_vendas

    # Se as vendas ultrapassam R$1500, aplica um bônus extra de 5% sobre o total de vendas
    if valor_vendas > 1500:
        bonus = (5 / 100) * valor_vendas
    else:
        bonus = 0

    salario_final = salario_fixo + comissao + bonus

    print(f"\nResumo do pagamento do vendedor {vendedor}:")
    print(f"Salário fixo: R${salario_fixo:.2f}")
    print(f"Comissão (3% sobre vendas): R${comissao:.2f}")
    print(f"Bônus adicional (5% sobre vendas acima de R$1500): R${bonus:.2f}")
    print(f"Salário final: R${salario_final:.2f}")        

if opcao == 1:
    print(verificarNota()) # Chama a função
elif opcao == 2:
    print(numeroParImpar())
elif opcao == 3:
    print(numeroParImpar())
elif opcao == 4:
    print(vogalConsoante())
elif opcao == 5:
    print(numeroTipo())
elif opcao == 6:
    print(receberHora())
elif opcao == 7:
    print(numeroMaior())
elif opcao == 8:
    print(menorNumeroTela())
elif opcao == 9:
    print(ladosTriangulo())
elif opcao == 10:
    print(calcular_salario())