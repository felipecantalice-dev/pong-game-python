# Jogo Pong

Pong é um dos primeiros jogos eletrônicos de arcade, criado por Allan Alcorn e lançado pela Atari em 1972. O jogo simula uma partida de tênis de mesa, onde dois jogadores controlam paletas para rebater uma bola de um lado para o outro da tela.
![](images\ingame.png)

A simplicidade do jogo e sua jogabilidade viciante ajudaram a popularizar os videogames e a estabelecer a indústria de jogos eletrônicos.


## Regras

Cada jogador controla uma paleta verticalmente ao longo da borda da tela. O objetivo é rebater a bola para o lado do adversário, tentando fazer com que ele não consiga devolvê-la. Cada vez que um jogador falha em rebater a bola, o adversário marca um ponto. O jogo continua até que um dos jogadores alcance a pontuação máxima definida.

## Ferramentas

Este projeto é uma recriação do clássico Pong usando a linguagem de programação Python e a biblioteca Turtle. O jogo inclui funcionalidades como controle de velocidade da bola, detecção de colisão com as paletas e as bordas da tela, e um placar para acompanhar a pontuação dos jogadores. Divirta-se jogando e revivendo a nostalgia dos primeiros dias dos videogames!


## Desenvolvimento

Jogo contem propriedades
* 800x600
* Cada paleta possui 5x1
* As paletas estao a uma distancia |x| de 350 do centro (0,0)

![](images\game_config.png)


A bola não pode exceder a tela em x e y 

* Caso a posicao da bola em y for maior (300 - 20) = 280(300 equivale a metade de tela em y menos a bolinha com 20, evitando que fuja da tela)
* Caso a posicao da bola em |x| for (400-20) = 380(400 equivale a metade de tela em x menos a bolinha com 20, evitando que fuja da tela)

![](images\ingame_screen_rules.png)