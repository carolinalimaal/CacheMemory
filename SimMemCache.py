#Definição MP
num_celulas_mp = 32
celulas_por_bloco = 2
mp = ['00000000' for c in range(num_celulas_mp)]

#Definição Cache
num_linhas = 4
blocos_por_linha = 4 
cache = [[-1, -1] for l in range(num_linhas)] # Dado inválido é -1

#Função de escrever na MP
def write_mp(): 
    print('='*26)
    print('  ESCREVENDO DADOS NA MP ')
    print('='*26)
    while True:
        address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2)
        if 0 <= address < num_celulas_mp:
            data = input('INFORMAÇÃO DE 8 bits: ').zfill(8)[:8] #O [:8] serve para deixar o dado com o tamanho de 8bits, retirando, caso ultrapasse, os menos significantes.
            mp[address] = data 
            print()
            opcao = input('Deseja continuar? [S]/[N]: ')
            if opcao in 'Nn':
                break
        else:
            print('ENDEREÇO INVÁLIDO.')

#Função para quebrar o endereço
def cachecontroller():
    address = (input('ENDEREÇO DE 5 bits: ').zfill(5))
    if 0 <= len(address) < num_celulas_mp:
        linha = int((address[2:4]), 2)
        celula = int((address[4:]), 2)
        address = int(address, 2)
        return linha, celula, address
    
#Função de escrever na CACHE
def write_cache():
    linha, celula, address = cachecontroller() 
    cache[linha][celula] = mp[address]

#Função de ler na CACHE
def read_cache():
    print('='*26)
    print('  LEITURA NA CACHE  ')
    print('='*26)
    linha, celula, address = cachecontroller()
    if cache[linha][celula] != -1:
        print(f'HIT. Conteúdo da célula {bin(address)[2:].zfill(5)} -> {cache[linha][celula]}')
    else:
        print('MISS. Bloco não encontrado. Buscando na MP...')
        write_cache()
        print(f'Conteúdo da célula {bin(address)[2:].zfill(5)} -> {cache[linha][celula]}')

def runSimulation():
    while True:
        read_cache()
        opcao = input('Deseja continuar? [S]/[N]: ')
        if opcao in 'Nn':
            break

write_mp() #Primeiramente, para preencher a MP com dados
runSimulation() #Simulação da interação CACHE-MP

