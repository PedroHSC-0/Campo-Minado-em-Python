->Trabalho de Programação em Python

->Pedro Henrique Silva Costa

->INSTRUÇÕES PARA JOGAR O CAMPO MINADO

->Inserir o tamanho do campo minado: (2x2 até 10x10)

->Inserir a quantidade de minas colocadas no campo: (Entre 1 e a metade do total de posições)

Após isso, o jogo inicia

-> Escolher se quer [1]marcar ou [2]abrir uma posição no campo.

em ambas as opções será solicitado a coordenada para a ação

->Cada rodada, o jogador precisa inserir coordenadas no modelo: (x, y)
de 0 ao tamanho do campo, por exemplo:
tamanho do campo = 10
exemplo de coordenadas esperadas: (8,9)
indo de (0, 0) até (9, 9)
a coordenada será usada ambas as ações

-> Símbolos no campo mostrado:
"*" é uma posição fechada,
"0" é uma posição aberta, o número indica a quantidade de minas vizinhas
"M" é uma posição que foi marcada pelo usuário onde ele acha estar uma mina
"X" é uma posição onde a mina está (Só é mostrada quando o jogador abre uma posição onde tem uma mina, nesse momento todas as posições de mina são reveladas)


-> Ao abrir uma posição, caso a posição tenha uma mina, o jogo acaba, caso não haja mina, a posição mostrará a quantidade de minas na distância de uma casa da posição escolhida.

->O jogo acaba quando todas as minas forem marcadas

->O jogador receberá mensagens de vitória ou de derrota para cada final que obtiver
Após uma sessão de jogo, terá a opção de escolher se quer recomeçar o jogo novamente

->INTERFACE

-De início são mostrados campos de input de dados para tamanho e quantidade de minas, com avisos para diversos erros que o usuário pode cometer na inserção dos dados

->Após inserir os dados do tamanho e quantidade de minas, o campo será mostrado, a cada rodada, o campo será atualizado, mostrando os simbolos descritos acima.

->O usuário deve escolher se quer marcar uma mina ou abrir uma posição, em ambas uma coordenada é pedida

-Quando o jogo acaba, e a mensagem de derrota ou vitoria aparece, o jogador é questionado se quer reiniciar o jogo, ou se quer finalizar o programa

-CONCLUSÃO

-Tentei limitar o máximo de erros possiveis na entrada de dados pelo usuários restringindo o tipo e os valores possiveis de cada input

-No campo minado original, a área que não tem minas é aberta, mas nessa versão não tem essa função, apenas é aberto a posição que o usuário escolheu

-O jogo, por ser no terminal, é metódico, demora muito para jogar, pedindo entradas de dados invés de cliques na tela
