import random
import tabulate
from abc import ABC, abstractmethod

# Definindo classes

class Tabuleiro():
    def __init__(self):
        """Inicializa um tabuleiro 3x3 vazio."""
        self.casas = [['' for _ in range(3)] for _ in range(3)]

    def pegar_tabuleiro(self):
        """
        Retorna o estado atual do tabuleiro.

        Returns:
            list: Uma lista 2D representando o tabuleiro.
        """
        return self.casas

    def marcar_casa(self, linha, coluna, simbolo):
        """
        Marca uma casa no tabuleiro com o símbolo do jogador.

        Args:
            linha (int): A linha onde a casa será marcada.
            coluna (int): A coluna onde a casa será marcada.
            simbolo (str): O símbolo do jogador que está fazendo a jogada.

        Raises:
            ValueError: Se a casa já estiver ocupada.
        """
        if self.casas[linha][coluna] == '':
            self.casas[linha][coluna] = simbolo
        else:
            raise ValueError("A casa já está ocupada.")

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro formatado na tela, com cabeçalhos de linha e coluna."""
        header = ['0', '  1', '  2']
        print("    " + " ".join(header))
        for i, linha in enumerate(self.casas):
            print(f"{i} | " + " | ".join(casa if casa != '' else ' ' for casa in linha) + " |")
            print("    " + "----" * 3)

class Jogador(ABC):
    def __init__(self, simbolo, nome):
        """Inicializa um jogador com um símbolo e nome.

        Args:
            simbolo (str): O símbolo do jogador.
            nome (str): O nome do jogador.
        """
        self.simbolo = simbolo
        self.jogador = nome

    @abstractmethod
    def fazer_jogada(self, tabuleiro: Tabuleiro):
        """Método a ser implementado pelas subclasses para fazer uma jogada."""
        pass

class JogadorHumano(Jogador):
    def fazer_jogada(self, tabuleiro: Tabuleiro):
        """Pede ao jogador humano para fazer uma jogada no tabuleiro.

        Args:
            tabuleiro (Tabuleiro): O tabuleiro onde a jogada será feita.

        Returns:
            tuple: A linha e coluna escolhidas pelo jogador.
        """
        while True:
            try:
                # Pedindo ao usuário para fazer uma jogada e verificando sua validade.
                posicao = input(f'A vez de jogar é do {self.jogador} ({self.simbolo}). Informe a posição (linha,coluna): ')
                posicao = posicao.replace(" ", "")
                linha, coluna = map(int, posicao.split(','))

                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print("Posição inválida! Por favor, insira uma linha e coluna entre 0 e 2.")
                    continue

                tabuleiro.marcar_casa(linha, coluna, self.simbolo)
                return (linha, coluna)

            except ValueError as e:
                print(e)
                print("Por favor, escolha uma casa válida no formato 'linha,coluna'.")
            except IndexError:
                print("Posição inválida! Por favor, insira uma linha e coluna entre 0 e 2.")

class JogadorComputador(Jogador):

    def __init__(self, simbolo, nome, estrategia='aleatoria'):
        """Inicializa um jogador computador com um símbolo, nome e estratégia.

        Args:
            simbolo (str): O símbolo do jogador.
            nome (str): O nome do jogador.
            estrategia (str): A estratégia do jogador computador (default é 'aleatoria').
        """
        super().__init__(simbolo, nome)
        self.estrategia = estrategia

    def fazer_jogada(self, tabuleiro: Tabuleiro):
        """Faz uma jogada no tabuleiro baseado na estratégia definida.

        Args:
            tabuleiro (Tabuleiro): O tabuleiro onde a jogada será feita.

        Returns:
            tuple: A linha e coluna escolhidas pelo jogador.
        """
        if self.estrategia == 'aleatoria':
            return self.jogada_aleatoria(tabuleiro)

    def jogada_aleatoria(self, tabuleiro: Tabuleiro):
        """Realiza uma jogada aleatória no tabuleiro.

        Args:
            tabuleiro (Tabuleiro): O tabuleiro onde a jogada será feita.

        Returns:
            tuple: A linha e coluna escolhidas aleatoriamente.
        """
        # verifica as casas disponíveis para realizar a jogada aleatória da máquina
        estado_tabuleiro = tabuleiro.pegar_tabuleiro()

        posicoes_disponiveis = []
        for i in range(len(estado_tabuleiro)):
            for j in range(len(estado_tabuleiro[i])):
                if estado_tabuleiro[i][j] == '':
                    posicoes_disponiveis.append((i, j))
        # Se a posição está disponível
        if posicoes_disponiveis:
            linha, coluna = random.choice(posicoes_disponiveis)
            tabuleiro.marcar_casa(linha, coluna, self.simbolo)
            return (linha, coluna)
        # caso o contrário
        else:
            return None

class JogoVelha:
    def __init__(self, jogador1, jogador2):
        """Inicializa o jogo da velha com dois jogadores.

        Args:
            jogador1 (Jogador): O primeiro jogador.
            jogador2 (Jogador): O segundo jogador.
        """
        self.jogadores = [jogador1, jogador2]
        self.tabuleiro = Tabuleiro()
        self.turno = 0

    def jogador_atual(self):
        """Retorna o jogador que está atualmente jogando.

        Returns:
            Jogador: O jogador atual.
        """
        return self.jogadores[self.turno]

    def alternar_turno(self):
        """Alterna o turno entre os jogadores."""
        self.turno = 1 - self.turno

    def verificar_vitoria(self, simbolo):
        """Verifica se o jogador com o símbolo especificado venceu.

        Args:
            simbolo (str): O símbolo do jogador que está sendo verificado.

        Returns:
            bool: True se o jogador venceu, False caso contrário.
        """
        # verificando se houve alguma vitória, se houve vitória, o jogo será encerrado.
        for linha in self.tabuleiro.pegar_tabuleiro():
            if all(casa == simbolo for casa in linha):
                return True

        for coluna in range(3):
            if all(self.tabuleiro.pegar_tabuleiro()[linha][coluna] == simbolo for linha in range(3)):
                return True

        if all(self.tabuleiro.pegar_tabuleiro()[i][i] == simbolo for i in range(3)) or \
           all(self.tabuleiro.pegar_tabuleiro()[i][2 - i] == simbolo for i in range(3)):
            return True

        return False

    def tabuleiro_cheio(self):
        """Verifica se o tabuleiro está cheio.

        Returns:
            bool: True se o tabuleiro está cheio, False caso contrário.
        """
        return all(casa != '' for linha in self.tabuleiro.pegar_tabuleiro() for casa in linha)

    def jogar(self):
        """Inicia o loop principal do jogo, alternando turnos e verificando vitórias."""
        print("Iniciando o jogo!")
        self.tabuleiro.imprimir_tabuleiro()
        while True:
            jogador = self.jogador_atual()
            print(f"Turno de {jogador.jogador} ({jogador.simbolo})")
            linha, coluna = jogador.fazer_jogada(self.tabuleiro)

            self.tabuleiro.imprimir_tabuleiro()

            if self.verificar_vitoria(jogador.simbolo):
                print(f"{jogador.jogador} venceu!")
                break
            if self.tabuleiro_cheio():
                print("O jogo empatou!")
                break

            self.alternar_turno()