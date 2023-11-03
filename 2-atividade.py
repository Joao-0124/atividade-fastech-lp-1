#Elevadores A, B, C
#Períodos Matutino, Vespertino, Noturno
#Elevador mais utilizado e seu período com mais fluxo
#Qual Período mais utilizado
#Qual Período menos utilizado
cont = 0
contA = 0
contB = 0
contC = 0
contM = 0
contV = 0
contN = 0
while True:
    elevador = input("Qual o Elevador que você Utilizou: (A, B ou C)" )
    periodo = input("Qual o Período Utilizado \n Para Matutino Informe M \n Para Vespertino informe V \n Para Noturno informe N \n " )
    cont += 1
    if(elevador == "A"):
        contA += 1
    if(elevador == "B"):
        contB += 1
    if(elevador == "C"):
        contC += 1
    if(periodo == "M"):
        contM += 1
    if(periodo == "V"):
        contV += 1
    if(periodo == "N"):
        contN += 1
    if(input("Deseja Continuar? (S, N)" )) != "S":
        break


lista_elevador = [contA, contB, contC]
elevador_mais_utilizado = max(lista_elevador)
if elevador_mais_utilizado == contA:
    elevador_mais_utilizado = 'A'
elif elevador_mais_utilizado == contB:
    elevador_mais_utilizado = 'B'
else:
    elevador_mais_utilizado = 'C'

lista_periodo = [contM, contV, contN]
periodo_de_maior_fluxo = max(lista_periodo)
if(periodo_de_maior_fluxo == contM):
    contM = 'Matutino'
elif(periodo_de_maior_fluxo == contV):
    contV = 'Vespertino'
else:
    contN = 'Noturno'
periodo_de_menor_fluxo = min(lista_periodo)
if(periodo_de_menor_fluxo == contM):
    contM = 'Matutino'
elif(periodo_de_menor_fluxo == contV):
    contV = 'Vespertino'
else:
    contN = 'Noturno'
print(f"O Elevador mais Utilizado foi: {elevador_mais_utilizado} no Período {periodo}")
print("O Período em que os Elevadores foram mais Utilizados foi:" , periodo_de_maior_fluxo)
print("O Período em que os Elevadores foram mais Utilizados foi:" , periodo_de_menor_fluxo)