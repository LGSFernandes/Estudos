km = float(input('Quantos Km foram rodados? '))
dias = int(input('Quantos dias foram alugados? '))

valorTotal = (60 * dias) + (km * 0.15)

print(f'O valor pago foi de R${valorTotal:.2f}')