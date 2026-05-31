# TicTacToe

O projeto consiste em ser um **jogo da velha** no qual o jogador pode jogar contra outro jogador ou contra a AI (roubada).

## Tecnologias

- Python
- Tkinter
- C

## Como Rodar?

1. Baixe as dependencias `pip install .`
1. Entre na pasta `src/`
1. Compile a *engine* do jogo da velha `gcc -fPIC -shared -o tictactoe.so ./engine/tictactoe.c`
1. Execute a aplicação `python run main.py`

## Inteligência Artificial

A "IA" do jogo funciona através do algoritmo *MiniMax* para tomar sempre a decisão com menos probabilidade de perda.

## Engine

O a lógica do jogo é implementada na linguagem C.

## UI

A interface gráfica é gerenciada pelo Python com *tkinter*.
