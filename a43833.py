


'''

AUTOR: Orlando Freitas 
'''
import sys
def carregaListaMarcas():
    mLista = []
    f = open("viaturas.txt", "r")
    for line in f:
        line = line.replace('\n', '')
        carLista = line.split(';')
        if carLista[0] != 'MARCA' :
            if not carLista[0] in mLista:
                mLista.append(carLista[0])
    f.close()
    return mLista

def carregaListaModelos(marca):
    mLista = []
    f = open("viaturas.txt", "r")
    for line in f:
        line = line.replace('\n', '')
        carLista = line.split(';')
        if carLista[0] == marca :
            if not carLista[1] in mLista :
                mLista.append(carLista[1])
    f.close()
    return mLista

def menuEscolha(lista):
    y = 1
    for i in lista:
        print(y,'- >',i)
        y += 1
    print(y,'- > sair')
    escolha = int(input('Escolha um da lista '))
    if escolha < -1 or escolha > y:
        print('Valor invalido ')
        menuEscolha(lista)
        escolha = 0
    if escolha == y:
        print('Sair!!')
        sys.exit(0)
    else:
        return lista[escolha-1]

def introduzirViatura(key):
    combLista = ['gasolina','diesel']
    caixLista = ['manual','automatica']
    for k in key:
        if k != 'MARCA' and k !='MODELO' and k !='PREÇO':
            if k == 'COMBUSTIVEL':
                car.update({k : menuEscolha(combLista)})
            elif k == 'CAIXA':
                car.update({k : menuEscolha(caixLista)})
            else :
                print('Indique ',k, end = ' ')
                car[k] = input()
    return car

def compararViaturas(car, carArquivo):
    # ano-> 0.5 km-> 0.25 comb-> 0.2 caix-> 0.05
    comp = 0
    difAno = (int(car.get('ANO')) - int(carArquivo.get('ANO'))) / int(car.get('ANO'))
    comp += 0.5 + difAno
    # ex: (2005 - 2010)/ 2005 = -0,00249 valor que vai ser retirado 0,5 que foi atribuido ao ano
    difKm = (int(carArquivo.get('KM')) - int(car.get('KM'))) / int(carArquivo.get('KM'))
    comp += 0.25 + difKm/10
    if car.get('COMBUSTIVEL') == carArquivo.get('COMBUSTIVEL'):
        comp += 0.2
    elif car.get('COMBUSTIVEL') == 'diesel' :
        comp += 0.2 + 0.05
    else:
        comp += 0.2 - 0.05
    if car.get('CAIXA') == carArquivo.get('CAIXA'):
        comp += 0.05
    elif car.get('CAIXA') == 'automatica' :
        comp += 0.05 + 0.005
    else:
        comp += 0.05 - 0.005
    return comp  

def procuraViatura(car, key):
    f = open("viaturas.txt", "r")
    carAux = {}
    for line in f:
        line = line.replace('\n', '')
        carLista = line.split(';')
        i = 0
        # Fazer uma procura só nas viaturas com a marca e o modelo correspondente
        if carLista[0] == car.get('MARCA') and carLista[1] == car.get('MODELO'): 
            for k in key:
                carAux[k] = carLista[i]
                i += 1
            comp = compararViaturas(car, carAux)

    preco = int(int(carAux.get('PREÇO'))*comp)
    car['PREÇO'] = str(preco)

def carregarKey():
    f = open("viaturas.txt", "r")   # abrir o arquivo de texto para leitura 'r'
    linha = f.readline()# ler a 1º linha do arquivo com as carateristicas das viaturas
    linha = linha.replace('\n', '')
    key = linha.split(";")          # copiar para uma lista as carateristicas separadas 
    f.close()
    return key

def novaViatura(key):
    carNovo = ''
    for k in key:
        print(k,'->',)
        carNovo += input() + '\n'
    carNovo = carNovo.replace('\n', ';',6)
    f = open("viaturas.txt", "a")   # abrir o arquivo de texto para acrescentar 'a'
    f.write(carNovo)
    f.close()
    
def gravarViatura(car):
    nLinha = ''
    for v in car.values():
        nLinha = nLinha + v + '\n'
    nLinha = nLinha.replace('\n', ';',6)
    f = open("viaturas.txt", "a")   # abrir o arquivo de texto para acrescentar 'a'
    f.write(nLinha)
    f.close()
    
def menuInicial():
    inicio = ['Consultar listagem do arquivo', 'Inserir uma viatura nova no arquivo']
    esc = menuEscolha(inicio)
    key = carregarKey()
    if esc == 'Inserir uma viatura nova no arquivo':
        novaViatura(key)
    else:
        car = {}
        marcasLista = carregaListaMarcas()
        esc = menuEscolha(marcasLista)
        car[key[0]] = esc
        modelosLista = carregaListaModelos(esc)
        car[key[1]] = menuEscolha(modelosLista)
        car = introduzirViatura(key)
        procuraViatura(car,key)
        gravarViatura(car)
        print(car)
    menuInicial()

menuInicial()    

