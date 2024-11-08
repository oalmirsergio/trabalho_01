from jogovelha import Jogador, JogadorComputador, JogadorHumano, JogoVelha, Tabuleiro

jogador1 = JogadorHumano('X','CidadãoNessiano')
jogador2 = JogadorComputador('O','Computador')
jogo = JogoVelha(jogador1,jogador2)
jogo.jogar()