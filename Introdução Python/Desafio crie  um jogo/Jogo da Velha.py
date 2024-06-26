def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    print("  1  2  3")
    for i, linha in enumerate(tabuleiro):
        print(f"{i+1} {' | '.join(linha)}")
        if i < 2:
            print("  " + "--+---+---")

def obter_movimento():
    while True:
        try:
            linha = int(input("Escolha uma entre as linhas 1, 2 e 3: ")) - 1
            coluna = int(input("Escolha uma entre as colunas 1, 2 e 3: ")) - 1
            if linha not in range(3) or coluna not in range(3):
                print("Valores inválidos, tente novamente")
                continue
            return linha, coluna
        except ValueError:
            print("Entrada inválida")

def validar_movimento(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == " "

def movimentacao(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return True
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] ==jogador and tabuleiro[2][0] == jogador:
            return True
    return False

def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogo_da_velha():
     tabuleiro = criar_tabuleiro()
     jogador_atual = "X"

     while True:
         exibir_tabuleiro(tabuleiro)

         linha, coluna = obter_movimento()
         if not validar_movimento(tabuleiro, linha, coluna):
            print("Espaço já marcado, tente novamente")
            continue

         movimentacao(tabuleiro, linha, coluna, jogador_atual)

         if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu o jogo!")
            break

         if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo deu Velha!")
            break

         jogador_atual = "O" if jogador_atual == "X" else "X"

jogo_da_velha()
