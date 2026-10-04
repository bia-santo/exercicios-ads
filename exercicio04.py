situacao = input("Digite a situação da candidatura: ").lower()

if situacao == "deferida":
    print("Candidatura aprovada")
elif situacao == "pendente":
    print("Candidatura aguardando análise")
elif situacao == "indeferida":
    print("Candidatura não aprovada")
else:
    print("Situação inválida")
