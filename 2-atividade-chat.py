contA = 0
contB = 0
contC = 0

contM = 0
contV = 0
contN = 0

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
periodos = {'Matutino': contM, 'Vespertino': contV, 'Noturno': contN}

max_quantidade_elevador = max(elevadores.values())
elevadores_max = [elevador for elevador, quantidade in elevadores.items() if quantidade == max_quantidade_elevador]

max_quantidade_periodo = max(periodos.values())
periodos_max = [periodo for periodo, quantidade in periodos.items() if quantidade == max_quantidade_periodo]

min_quantidade_periodo = min(periodos.values())
periodos_min = [periodo for periodo, quantidade in periodos.items() if quantidade == min_quantidade_periodo]

if len(elevadores_max) == 1:
    print(f"O Elevador mais Utilizado foi o {elevadores_max[0]} e o Período com mais fluxo foi o {', '.join(periodos_max)}")
else:
    print(f"Os Elevadores mais Utilizados foram: {', '.join(elevadores_max)} e o Período com mais fluxo foi o {', '.join(periodos_max)}")

if len(periodos_max) == 1:
    print("O Período mais utilizado foi:", periodos_max[0])
else:
    print("Os Períodos mais utilizados foram:", ', '.join(periodos_max))

if len(periodos_min) == 1:
    print("O Período menos utilizado foi:", periodos_min[0])
else:
    print("Os Períodos menos utilizados foram:", ', '.join(periodos_min))