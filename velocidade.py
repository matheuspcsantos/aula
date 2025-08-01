# Entrada dos dados
distancia = float(input("Digite a distância (em km): "))
velocidade = float(input("Digite a velocidade média (em km/h): "))

# Cálculo do tempo
tempo = distancia / velocidade

# Saída
print(f"Tempo estimado de viagem: {tempo:.1f} horas")
