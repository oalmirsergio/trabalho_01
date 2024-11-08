# Jogo da Velha.

Este é um simples jogo da velha (ou "tic-tac-toe") implementado em Python. O jogo pode ser jogado entre um jogador humano e um computador, ou entre dois jogadores humanos.

## Estrutura do Código

O código é composto pelas seguintes classes:

- `Tabuleiro`: Representa o tabuleiro do jogo.
- `Jogador`: Classe base abstrata para os jogadores.
- `JogadorHumano`: Implementação da classe `Jogador` para jogadores humanos.
- `JogadorComputador`: Implementação da classe `Jogador` para jogadores controlados por computador.
- `JogoVelha`: Gerencia a lógica do jogo e a interação entre os jogadores.

## Instalação

Para executar este código, você precisa ter o Python instalado em sua máquina.

```bash
No seu terminal, digite o código:

python -m pip install --upgrade pip setuptools wheel

- Depois digite :
 
python setup.py install
```
## Exemplo de Uso

Para jogar, você deve importar as classes, instanciar os jogadores e iniciar o jogo da seguinte forma:

```python
from jogovelha import Jogador, JogadorHumano, JogadorComputador, JogoVelha, Tabuleiro

jogador1 = JogadorHumano(simbolo='X', nome='Jogador1')
jogador2 = JogadorComputador(simbolo='O', nome='IA')
jogo = JogoVelha(jogador1, jogador2)
jogo.jogar()
```
## Classes e Métodos

### Classe Tabuleiro

A classe `Tabuleiro` representa o tabuleiro do jogo da velha. Ela gerencia o estado das casas do jogo e fornece métodos para marcar jogadas e exibir o tabuleiro.

#### Métodos

- `__init__(self)`: Inicializa um tabuleiro vazio de 3x3.
- `pegar_tabuleiro(self)`: Retorna o estado atual do tabuleiro como uma lista bidimensional.
- `marcar_casa(self, linha, coluna, simbolo)`: Marca uma casa específica com o símbolo do jogador, se a casa estiver disponível.
- `imprimir_tabuleiro(self)`: Exibe o tabuleiro no console em um formato organizado.

#### Código

```python
class Tabuleiro:
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
        """
        Imprime o tabuleiro formatado na tela, com cabeçalhos de linha e coluna.
        """
        header = ['   0', '   1', '   2']
        print("    " + " ".join(header))
        for i, linha in enumerate(self.casas):
            print(f"{i} | " + " | ".join(casa if casa != '' else ' ' for casa in linha) + " |")
            print("    " + "----" * 3)

```
### Classe Jogador

A classe `Jogador` é uma classe abstrata que serve de base para os jogadores no jogo da velha. Ela define um jogador por meio de um símbolo (por exemplo, 'X' ou 'O') e um nome.

#### Métodos

- `__init__(self, simbolo, nome)`: Inicializa o jogador com o símbolo e o nome.
- `fazer_jogada(self, tabuleiro)`: Método abstrato que deve ser implementado pelas subclasses, para que o jogador faça uma jogada no tabuleiro.

```python
class Jogador(ABC):
    def __init__(self, simbolo, nome):
        """Inicializa um jogador com um símbolo e nome."""
        self.simbolo = simbolo
        self.jogador = nome

    @abstractmethod
    def fazer_jogada(self, tabuleiro: Tabuleiro):
        """Método abstrato para fazer uma jogada."""
        pass
```
### Classe JogadorHumano

A classe `JogadorHumano` herda da classe abstrata `Jogador` e representa um jogador humano que interage diretamente com o jogo, escolhendo a posição onde deseja jogar.

#### Métodos

- `__init__(self, simbolo, nome)`: Inicializa o jogador humano com um símbolo (ex: 'X' ou 'O') e um nome.
- `fazer_jogada(self, tabuleiro)`: Solicita ao jogador humano para escolher uma posição válida no tabuleiro e marca a jogada.

#### Código

```python
class JogadorHumano(Jogador):
    def __init__(self, simbolo, nome):
        """Inicializa o jogador humano com o símbolo e o nome."""
        super().__init__(simbolo, nome)

    def fazer_jogada(self, tabuleiro: Tabuleiro):
        """Pede ao jogador humano para fazer uma jogada no tabuleiro.

        Args:
            tabuleiro (Tabuleiro): O tabuleiro onde a jogada será feita.

        Returns:
            tuple: A linha e coluna escolhidas pelo jogador.
        """
        while True:
            try:
                posicao = input(f'A vez de jogar é do {self.jogador} ({self.simbolo}). Informe a posição (linha,coluna): ')
                posicao = posicao.replace(" ", "")
                linha, coluna = map(int, posicao.split(','))

                if linha < 0 ou linha > 2 ou coluna < 0 ou coluna > 2:
                    print("Posição inválida! Por favor, insira uma linha e coluna entre 0 e 2.")
                    continue

                tabuleiro.marcar_casa(linha, coluna, self.simbolo)
                return (linha, coluna)

            except ValueError as e:
                print(e)
                print("Por favor, escolha uma casa válida no formato 'linha,coluna'.")
            except IndexError:
                print("Posição inválida! Por favor, insira uma linha e coluna entre 0 e 2.")
```
### Classe JogadorComputador

A classe `JogadorComputador` herda da classe abstrata `Jogador` e representa um jogador controlado pelo computador. O comportamento do computador é baseado em uma estratégia, como jogadas aleatórias.

#### Métodos

- `__init__(self, simbolo, nome, estrategia='aleatoria')`: Inicializa o jogador computador com um símbolo, nome e uma estratégia de jogo. A estratégia padrão é aleatória.
- `fazer_jogada(self, tabuleiro)`: Executa uma jogada baseada na estratégia definida.
- `jogada_aleatoria(self, tabuleiro)`: Realiza uma jogada aleatória em uma das casas vazias do tabuleiro.

#### Código

```python
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
        estado_tabuleiro = tabuleiro.pegar_tabuleiro()

        posicoes_disponiveis = []
        for i in range(len(estado_tabuleiro)):
            for j in range(len(estado_tabuleiro[i])):
                if estado_tabuleiro[i][j] == '':
                    posicoes_disponiveis.append((i, j))

        if posicoes_disponiveis:
            linha, coluna = random.choice(posicoes_disponiveis)
            tabuleiro.marcar_casa(linha, coluna, self.simbolo)
            return (linha, coluna)
        else:
            return None
```
### Classe JogoVelha

A classe `JogoVelha` gerencia o jogo da velha, coordenando os jogadores, o tabuleiro e verificando as condições de vitória ou empate.

#### Métodos

- `__init__(self, jogador1, jogador2)`: Inicializa o jogo com dois jogadores e um tabuleiro.
- `jogador_atual(self)`: Retorna o jogador que está atualmente jogando.
- `alternar_turno(self)`: Alterna o turno entre os dois jogadores.
- `verificar_vitoria(self, simbolo)`: Verifica se o jogador com o símbolo especificado venceu o jogo.
- `tabuleiro_cheio(self)`: Verifica se o tabuleiro está completamente preenchido.
- `jogar(self)`: Inicia o loop principal do jogo, alternando turnos e verificando o resultado da partida.

#### Código

```python
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
```
# Licença MIT

Copyright (c) [2024] [Almir Sérgio Ramos dos Santos Filho]

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados (o "Software"), para lidar com o Software sem restrição, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e permitir às pessoas a quem o Software é fornecido que o façam, sujeitas às seguintes condições:

O aviso de copyright acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM NENHUM CASO OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSABILIZADOS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRAS RESPONSABILIDADES, SEJA EM UMA AÇÃO CONTRATUAL, DELITO OU OUTRA FORMA, DECORRENTE DE, FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.

---

Para mais informações sobre a licença MIT, consulte o seguinte link: [MIT License](https://opensource.org/licenses/MIT).

# Agradecimentos

Gostaríamos de expressar nossa gratidão a todos que contribuíram para o desenvolvimento deste projeto:

- **[Almir Sérgio Ramos dos Santos]** - Criador e desenvolvedor principal do jogo da velha.

- **[Pedro Henrique Neves]** - Obrigado pelo suporte na documentação e testes do jogo.

Além disso, agradecemos à comunidade de desenvolvedores e às seguintes bibliotecas e recursos:

- **Python** - Para ser uma linguagem acessível e poderosa.
- **Biblioteca Random** - Para fornecer funcionalidades de geração aleatória que melhoram a experiência de jogo.
- **Tabulate** - Para facilitar a formatação e apresentação do tabuleiro.
- **Sys** - Para oferecer acesso a funcionalidades que ajudam na manipulação do sistema.
- **OS** - Para fornecer uma maneira de interagir com o sistema operacional.

Agradecemos a todos pelo apoio e incentivo! Se você tiver alguma sugestão ou feedback, sinta-se à vontade para entrar em contato.

Email para contato: almirsergio.a@gmail.com