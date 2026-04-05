excelente = 0
ruim = 0
bom = 0

for i in range(50):
    print(f"\nPessoa {i+1}:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite sua opinião (1-excelente, 2-bom, 3-ruim): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

print("\nResultado da pesquisa:")
print("Número de pessoas que responderam excelente:", excelente)
print("Número de pessoas que responderam bom:", bom)
print("Número de pessoas que responderam ruim:", ruim)