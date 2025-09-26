from random import randint
import os
import time
from shutil import get_terminal_size

# Variável do tamanho do terminal para centralizar o campo minado
largura_terminal = get_terminal_size().columns

#-------------------------------------------------------------------------------------
# Função que gera aviso personalizado
def aviso(mensagem, atraso):
    os.system('cls')
    print(mensagem, end="")
    for i in range(3):
        time.sleep(atraso)
        print(".", end="", flush=True)

    time.sleep(atraso)
    os.system('cls')

# Função para mostrar o campo atual
def mostrar_campo(campo):
    for linha in campo:

        linha_str = "".join(f"| {coordenada} " for coordenada in linha) + "|"
        print(linha_str.center(largura_terminal))

# Função que gera mensagem de derrota
def perdeu():
    time.sleep(2)
    os.system('cls')
    mensagem = r"""
    |--------------------------------------|
    | |¨¨¨¨\    /¨¨¨¨\  /¨¨¨¨\  |\      /| |
    | |     )  |      ||      | | \    / | |
    | |¨¨¨¨¨)  |      ||      | |  \  /  | |
    | |____/    \____/  \____/  |   \/   | |
    |--------------------------------------|

    """
    print(mensagem.center(largura_terminal))
    print("PERDEU")
    
    for i in range(40):
        time.sleep(0.1)
        print(".", end="", flush=True)

    os.system('cls')

# Função que gera mensagem de vitória
def venceu():
    time.sleep(2)
    os.system('cls')
    mensagem = r"""
    |----------------------------------------| 
    |  \      /\      /    0     |\   |   |  | 
    |   \    /  \    /     |     | \  |   |  | 
    |    \  /    \  /      |     |  \ |   |  | 
    |     \/      \/       |     |   \|   0  | 
    |----------------------------------------|
    """
    print(mensagem.center(largura_terminal))
    print("VENCEU")
    
    for i in range(40):
        time.sleep(0.1)
        print(".", end="", flush=True)

    os.system('cls')

# Função de entrada de dados Tamanho do campo e número de minas
def input_dados():
    os.system('cls')
    while(True):
        try: 
            tamanho = int(input("Insira o tamanho do campo minado: (2 a 10) "))
        except:
            aviso("Insira um número inteiro", 0.5)
            continue
        
        # Caso o tamanho não seja válido
        if(not (2 <= tamanho <= 10)):
            aviso("Insira um tamanho entre 2 e 10", 0.7)
            continue

        while(True):
            try:
                n_minas = int(input(f"Insira o número de minas contidas no campo (Min: 1|Max: {int((tamanho**2)/2)}) "))
                if(n_minas > ((tamanho ** 2) / 2) or n_minas < 1):
                    aviso("Digite uma quantidade válida", 0.5)
                    continue
            
            except:
                aviso("Insira um número inteiro", 0.5)
                continue
            break
        break

    return tamanho, n_minas

# Função para gerar o campo minado aleatóriamente, com minas posicionadas aleatóriamente
def gerar_campo(tamanho, n_minas):
    campo = [["*" for i in range(tamanho)] for i in range(tamanho)]
    coordenadas_minas = []
    while(n_minas > 0):
        coordenada = (randint(0, tamanho - 1), randint(0, tamanho - 1))
        if(not (coordenada in coordenadas_minas)):
            coordenadas_minas.append(coordenada)
            n_minas -= 1
            
    return campo, coordenadas_minas

# Função que atualiza o campo pra mostrar todas as minas
def mostrar_minas(campo, coordenadas_minas):
    for coordenada in coordenadas_minas:
        campo[coordenada[0]][coordenada[1]] = "X"
    return campo

# Função para leitura e tratamento da entrada de dados das coordenadas
def ler_coordenadas(campo, tamanho, mensagem):
    while(True):
        try:
            coordenadas_str = str(input(mensagem))
            if "," in coordenadas_str:
                linha, coluna = coordenadas_str.split(",")
                linha = int(linha.strip()) - 1
                coluna = int(coluna.strip()) - 1
                if linha > tamanho - 1 or coluna > tamanho - 1:
                    aviso("Insira uma coordenada dentro do campo", 0.5)
                    continue
                print(f"{linha}, {coluna}")
                return (linha, coluna)
                
            else:
                aviso("Insira uma coordenada válida, Ex: 5, 6", 0.5)
        except:
            aviso("Insira uma coordenada válida, Ex: 5, 6", 0.5)

def contar_minas_vizinhas(posicao, coordenadas_minas, raio):
    linha_posicao = posicao[0]
    coluna_posicao = posicao[1]
    n_minas = 0
    raio = 1

    # Verificando arredores
    for dlinha in [-raio, 0, raio]:
        for dcoluna in [-raio, 0, raio]:
            # Posição aberta não conta
            if dlinha == 0 and dcoluna == 0:
                continue
            if (linha_posicao + dlinha, coluna_posicao + dcoluna) in coordenadas_minas:
                n_minas += 1
                
    return n_minas

# Função para verificar e marcar o redor da coordenada aberta pelo jogador
def atualizar_campo(campo, posicao, n_minas):
    # Conta quantas minas vizinhas existem

    # Define a quantidade de minas vizinhas na posição escolhida pelo usuário
    campo[posicao[0]][posicao[1]] = n_minas
    return campo

# Função que verifica se todas as minas estão marcadas
def verificar_posicoes_minas(campo, coordenadas_minas):
    for coordenada in coordenadas_minas:
        if campo[coordenada[0]][coordenada[1]] != "M":
            return False
    else:
        return True

# Função que inicia e executa o jogo
def jogar(campo, coordenadas_minas):
    aviso("INICIANDO CAMPO MINADO", 0.7)

    while(True):
        os.system('cls')
        mostrar_campo(campo)
        opcao = input("->[1]Marcar uma mina\n->[2]Abrir uma posição\n")
        
        if opcao == "1":
            coordenada = ler_coordenadas(campo, len(campo), "Digite a coordenada onde você vai marcar(Ex: 1, 2): ")
            campo[coordenada[0]][coordenada[1]] = "M"

        elif opcao == "2":
            coordenada = ler_coordenadas(campo, len(campo), "Digite a coordenada onde você vai marcar(Ex: 1, 2): ")

            # Escolheu a posição da mina
            if(coordenada in coordenadas_minas):
                campo = mostrar_minas(campo, coordenadas_minas)
                mostrar_campo(campo)
                return False
            # Próxima rodada
            else:
                n_minas = contar_minas_vizinhas(coordenada, coordenadas_minas, 1)
                campo = atualizar_campo(campo, coordenada, n_minas)
        else:
            aviso("Escolha uma das opções", 0,7)

        if verificar_posicoes_minas(campo, coordenadas_minas):
            return True
           
#-------------------------------------------------------------------------------------
