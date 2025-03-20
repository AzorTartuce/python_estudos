# Aqui vou criar um projeto que vai calcular a distancia entre dois pontos
# Vai calcular a velocidade que para percorrer a distancia 

# A = Valores de saida B = Valores de chegada

# Receber valores de saida
pontoAlati = float(input("Digite o valor da latitude do ponto A: "))
pontoBlati = float(input("Digite o valor da latitude do ponto B: "))
pontoAlon = float(input("Digite o valor da longitude do ponto A: "))
pontoBlon = float(input("Digite o valor da longitude do ponto B: "))

tempo = float(input("Digite o tempo que o veiculo levou para percorrer a distancia: "))

# Calcular distancia entre os pontos 

def calcular_distancia(pontoAlati, pontoBlati, pontoAlon, pontoBlon):
    return ((pontoAlati - pontoBlati)**2 + (pontoAlon - pontoBlon)**2)**0.5

distancia = calcular_distancia(pontoAlati, pontoBlati, pontoAlon, pontoBlon)
print(f"A distancia entre os pontos A e B é de {distancia} km ")

# Calcular a velocida 
# v = d/t | velocidade = distancia / tempo 

def calcular_velocidade(distancia, tempo):
    return distancia / tempo

velocidade = calcular_velocidade(distancia, tempo)
print(f"A velocidade que o veiculo estava é de {velocidade} km")