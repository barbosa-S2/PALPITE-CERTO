# Jogo de Adivinhação
# Descrição
Este é um simples jogo de adivinhação onde o jogador tenta adivinhar um número secreto gerado aleatoriamente pelo computador. O jogo oferece três níveis de dificuldade, cada um com um número diferente de tentativas permitidas.

# Estrutura do Código
Importação de Biblioteca
python
Copy code
import random as rd
Importa a biblioteca random e a renomeia para rd, que será utilizada para gerar números aleatórios.

# Funções
# boasVindas()
python

def boasVindas():
    print('\n_____________________________________________')
    print('\n|---SEJA BEM VINDO AO JOGO DE ADIVINHAÇÃO----|')
    print('|---DEFINA A DIFICULDADE QUE DESEJA JOGAR---|')
    print('|---------------1 FÁCIL---------------------|')
    print('|---------------2 MÉDIO---------------------|')
    print('|---------------3 DIFICIL-------------------|')
Exibe uma mensagem de boas-vindas e apresenta as opções de dificuldade ao jogador.

# dificuldade()
python

def dificuldade():
    boasVindas()
    while True:
        opcao = int(input('\nQual é a sua escolha, campeão: '))
        if opcao == 1:
            max_tentativas = 10
            print('\nÓtima opção para iniciantes! Vamos começar!')
            return max_tentativas
        elif opcao == 2:
            max_tentativas = 5
            print('\nPor que não tentar algo mais difícil? Vamos começar!')
            return max_tentativas
        elif opcao == 3:
            max_tentativas = 3
            print('\nSão apenas 3 tentativas, tenho medo de você! Vamos ver se é realmente bom!')
            return max_tentativas
        else:
            print('\nOpção inválida. Por favor, escolha uma dificuldade válida.')
Chama a função boasVindas() para mostrar as opções de dificuldade.
Solicita que o jogador escolha um nível de dificuldade.
Define o número máximo de tentativas com base na escolha do jogador:
Fácil: 10 tentativas.
Médio: 5 tentativas.
Difícil: 3 tentativas.
Garante que uma escolha válida seja feita através de um loop.
# jogo_adivinhacao()
python

def jogo_adivinhacao():
    numero_secreto = rd.randint(1, 100)
    tentativas = 0
    max_tentativas = dificuldade()

    while tentativas < max_tentativas:
        palpite = int(input('\nTente a sorte: '))
        
        if palpite == numero_secreto:
            print('\nParabéns! Você é um campeão!')
            break
        elif palpite > numero_secreto:
            print('\nTENTE UM NÚMERO MENOR!')
        else:
            print('\nTENTE UM NÚMERO MAIOR!')

        tentativas += 1

    if tentativas >= max_tentativas:
        print(f'Fim de jogo! O número era {numero_secreto}.')
    
    opcao = int(input('\nPara jogar novamente digite (1), para sair digite qualquer outra tecla: '))
    if opcao == 1:
        jogo_adivinhacao()
    else:
        print('\nObrigado por jogar, volte sempre!')
Gera um número secreto aleatório entre 1 e 100.
Chama a função dificuldade() para definir o número máximo de tentativas.
Permite ao jogador fazer palpites até atingir o número máximo de tentativas.
Informa se o palpite deve ser maior ou menor.
Parabeniza o jogador se ele adivinhar o número secreto.
Se o jogador não adivinhar o número dentro do limite de tentativas, informa o número secreto.
Pergunta se o jogador deseja jogar novamente. Se sim, reinicia o jogo; caso contrário, encerra.

# Execução do Jogo
python
Copy code
jogo_adivinhacao()
Chama a função jogo_adivinhacao() para iniciar o jogo.

# Como Executar
Certifique-se de ter o Python instalado em seu sistema.
Salve o código em um arquivo, por exemplo, adivinhacao.py.
Execute o arquivo com o comando:
Copy code
python adivinhacao.py

# Funcionalidades
Escolha de dificuldade: Três níveis de dificuldade (Fácil, Médio, Difícil) que determinam o número de tentativas permitidas.
Palpites com dicas: Dicas são fornecidas para ajudar o jogador a ajustar seus palpites (maior ou menor).
Reinício do jogo: Opção para jogar novamente após cada rodada.

# Contribuição
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Envie suas sugestões ou faça um pull request no repositório.