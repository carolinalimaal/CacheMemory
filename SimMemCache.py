# Definindo a MP
numBlocos = 16
numCelulas = 32
mp = ['00000000' for _ in range(numCelulas)] 

# Definindo a CACHE 
numLinhas = 4
numCelulaLinha = 2
cacheTAG = [[None, None] for _ in range(numLinhas)]
cacheDADO = [[None, None] for _ in range(numLinhas)]

#Função para 'quebrar' o endereço 
def cacheController(endereco):
    if 0 <= int(endereco, 2) <= numCelulas:
        bloco = int(endereco[:4], 2)
        linha = int(endereco[2:4], 2)
        celula = int(endereco[4:], 2)
        endereco = int(endereco, 2)
        return linha, celula, endereco
    else:
        print('ENDERECO INVÁLIDO!')

#Função para escrever na MP
def writeMp():
    while True:
        print('='*20)
        print('  ESCREVENDO NA MP ')
        print('='*20)
        endereco = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2)
        if 0 <= endereco <= numCelulas:
            dado = input('DADO DE 8 bits: ').zfill(8)[:8]
            mp[endereco] = dado
            print()
            opcao = input('Deseja continuar? [S]/[N]: ')
            if opcao in 'Nn':
                break
        else:
            print('ENDEREÇO INVÁLIDO.')
    print('='*20)
    print('    ESTADO DA MP')
    print('='*20)
    for _ in range(numCelulas):
        print(mp[_])

#Função para escrever na Cache, caso dê 'CACHE MISS'
def writeCache(linha, celula, endereco):
    cacheTAG[linha][celula] = endereco
    cacheDADO[linha][celula] = mp[endereco]
    if celula == 0: #Condição para levar o bloco todo, verificando se é a célula 0 ou 1
        cacheTAG[linha][celula+1] = endereco+1
        cacheDADO[linha][celula+1] = mp[endereco+1]
    else:
        cacheTAG[linha][celula-1] = endereco-1
        cacheDADO[linha][celula-1] = mp[endereco-1]

#Função para ler na Cache
def readCache(linha, celula, endereco):
    if cacheTAG[linha][celula] == endereco:
        print(f'CACHE HIT. Conteúdo da célula {bin(endereco)[2:].zfill(5)} -> {cacheDADO[linha][celula]}\n')
    else:
        print('CACHE MISS. Buscando na MP.....')
        writeCache(linha, celula, endereco)
        print(f'Conteúdo da célula {bin(endereco)[2:].zfill(5)} -> {cacheDADO[linha][celula]}\n')

#Função que roda todo o sistema
def runSimulation():
    while True:
        print('='*20)
        print('   LENDO NA CACHE   ')
        print('='*20)
        endereco = (input('ENDEREÇO DE 5 bits: ').zfill(5))
        linha, celula, endereco = cacheController(endereco)
        readCache(linha, celula, endereco)
        print('='*24)
        print('     ESTADO DA CACHE')
        print('='*24)
        for l in range(numLinhas):
                print(cacheDADO[l])
        print()
        opcao = input('Deseja continuar? [S]/[N]: ')
        if opcao in 'Nn':
            break

writeMp() #Para preencher a MP
runSimulation() #Para ler na Cache
