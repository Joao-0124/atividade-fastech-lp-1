cont = 0
contO = 0
contB = 0
contR = 0
contP = 0
idade_maior = 0
idade_menor = 1000
idade_menor_resp = ''
idade_maior_resp = ''
while True:
    idade = int(input("Qual Sua Idade? "))
    atendimento = input("Seu Atendimento foi (OTIMO, BOM, REGULAR, PESSIMO)? ")
    cont += 1
    if (atendimento == "OTIMO"):
        contO += 1
    if (atendimento == "BOM"):
        contB += 1
    if (atendimento == "REGULAR"):
        contR += 1
    if (atendimento == "PESSIMO"):
        contP += 1
    if (idade > idade_maior):
        idade_maior = idade
        idade_maior_resp = atendimento
    if (idade < idade_menor):
        idade_menor = idade
        idade_menor_resp = atendimento
    if (input("Deseja Continuar? (S, N)" )) != "S":
        break
print("Total de pessoas que responderam", cont)
print("A quantidade de pessoas que receberam otimo foi:\n" , contO)
print("A quantidade de pessoas que receberam bom foi:\n" , contB)
print("A quantidade de pessoas que receberam regular foi:\n" , contR)
print("A quantidade de pessoas que receberam pessimo foi:\n" , contP)
print("O mais Novo tem" , idade_menor, "anos, e sua resposta foi" , idade_menor_resp) 
print("O mais Velho tem" , idade_maior, "anos e sua resposta foi" , idade_maior_resp)