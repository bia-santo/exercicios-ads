tempAtraso = float(input("Digite o tempo de atraso: "))

if tempAtraso <= 10:
    print("Nenhum crédito")
elif tempAtraso <= 25:
    print("R$ 5,00 de crédito")
elif tempAtraso <= 45:
    print("R$ 10,00 de crédito")
else:
    print("R$ 20,00 de crédito")
