contA = 0
contB = 0
contC = 0

contM = 0
contV = 0
contN = 0

lista = []
lista_elevador = []
lista_periodo = []

while True:
    elevador = input("Qual o Elevador que você Utilizou: (A, B ou C)" )
    periodo = input("Qual o Período Utilizado \n Para Matutino Informe M \n Para Vespertino informe V \n Para Noturno informe N \n " )
    
    if(elevador == "A"):
        contA += 1
    elif(elevador == "B"):
        contB += 1
    elif(elevador == "C"):
        contC += 1

    if(periodo == "M"):
        contM += 1
    elif(periodo == "V"):
        contV += 1
    elif(periodo == "N"):
        contN += 1
    if(input("Deseja Continuar? (S, N)" )) != "S":
        break

lista_elevador.extend([contA,contB,contC])
lista_periodo.extend([contM,contV,contN])

elevadores = {'A': contA, 'B': contB, 'C': contC}
periodos = {'M': contM, 'V': contV, 'N': contN}

max_lista_elevador = max(elevadores, key=elevadores.get)
max_lista_periodo = max(periodos, key=periodos.get)
min_lista_periodo = min(periodos, key=periodos.get)

lista.append([max_lista_elevador, max_lista_periodo])

print(f"O Elevador mais Utilizado foi o {max_lista_elevador} e o Período com mais fluxo foi o {max_lista_periodo}")
print("O Período em que os Elevadores foram mais Utilizados foi:" , max_lista_periodo)
print("O Período em que os Elevadores foram menos Utilizados foi:" , min_lista_periodo)