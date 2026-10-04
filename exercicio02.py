qtdDias = int(input("Quantos dias está aguardando a retirada? "))

if qtdDias >= 0 and 2 >= qtdDias:
    print("Retirada sem taxa")
elif qtdDias >= 3 and 5 >= qtdDias:
    print("Cobrar taxa de 5,00")
else:
    print("Retirada bloqueada")
