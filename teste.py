valorPao = 0,38 
valorBroa = 4,50

qtPaoDia = int(input('Quantos pães francesses são vendidos no dia: '))
qtBroaDia = int(input('Quantas broa são vendidas em um dia :'))
somaVendas = qtPaoDia + qtBroaDia
print(f"O valor total vendido em um dia foi de {somaVendas}")

reserva = somaVendas * 0.10
print(f"Ele precisa reservar {reserva} do valor das vendas! ")