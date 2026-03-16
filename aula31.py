placa_veiculo = input('Digite a placa do veiculo: ')
velocidade_veiculo = input('Digite a velocidade o veiculo:') #velocidade do veiculo em km/h
velocidade_veiculo = int(velocidade_veiculo)
posicao_veiculo = 101 #posição do veiculo ao passar no radar

VEL_RADAR_1 = 50 #velocidade máxima permitida no radar em km/h
POSICAO_RADAR1 = 100 #posição do radar instalado
RANGE_RADAR_1 = 1 #distancia onde o radar detecta o veiculo

velocidade_nao_permitida = velocidade_veiculo > VEL_RADAR_1
carro_passa_pelo_radar = posicao_veiculo > (POSICAO_RADAR1 - RANGE_RADAR_1) or \
    posicao_veiculo <= (POSICAO_RADAR1 - RANGE_RADAR_1)
carro_multado = velocidade_nao_permitida and carro_passa_pelo_radar

print()
if carro_multado:
    print(f'Velocidade máxima permitida no radar: {VEL_RADAR_1} km/h')
    print(f'Placa do veiculo: {placa_veiculo}')
    print(f'Velocidade do veiculo detectada: {velocidade_veiculo} km/h')
    print('O veiculo foi multado.')
else:
    print(f'Velocidade máxima permitida no radar: {VEL_RADAR_1} km/h')
    print(f'Placa do veiculo: {placa_veiculo}')
    print(f'Velocidade do veiculo detectada: {velocidade_veiculo} km/h')
    print('O veiculo NÃO foi multado.')
