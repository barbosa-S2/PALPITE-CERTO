#biblioteca de numeros aleatorios
import random as rd

#obas vindas e escolha de dificuldade do jogador
def boasVindas():
    print('\n_____________________________________________')
    print('\n|---SEJA BEM VINDO AO PALPITE CERTO-------|')
    print('|---DEFINA A DIFICULDADE QUE DESEJA JOGAR---|')
    print('|---------------1 FÁCIL---------------------|')
    print('|---------------1 MÉDIO---------------------|')
    print('|---------------3 DIFICIL-------------------|')

#mecanica de dificuldade
def dificuldade():
    boasVindas()
    opcao = int(input('\nQual á sua escolha campeão: '))

    if opcao == 1:
        max_tentativas = 10
        print('\nOtima opção para iniciantes! vamos começar!')
        return max_tentativas

    if opcao == 2:
        max_tentativas = 5
        print('\nPor que não tentar algo mais dificil? vamos começar!')
        return max_tentativas

    if opcao == 3:
        max_tentativas = 3
        print('\nSão apenas 3 tentativas, tenho medo de você! vamos ver se é realmente bom!')
        return max_tentativas
    
#criando nosso jogo de adivinhação
def jogo_adivinhacao():
    numero_secreto = rd.randint(1,100)
    tentativas = 0
    max_tentativas = dificuldade()

    while tentativas < max_tentativas:
        palpite = int(input('\nTente á sorte: '))
        
        if palpite == numero_secreto:
            print('\nParabéns! Você é um campeão!')
            opcao = int(input('\nPara jogar novamente digite (1): '))
            if opcao == 1:
                jogo_adivinhacao()
            else:
                print('\nObrigado por jogar, volte sempre!')
                break
        elif palpite > numero_secreto:
            print('\nTENTE UM NUMERO MENOR!')
        else:
            print('\nTENTE UM NUMERO MAIOR!')

        tentativas += 1

    if tentativas >= max_tentativas:
        print(f'fim de Jogo! O numero era {numero_secreto}.')
        opcao = int(input('\nPara jogar novamente digite (1): '))
        if opcao == 1:
            jogo_adivinhacao()
        else:
            print('\nObrigado por jogar, volte sempre!')
            

#jogo pronto para ser executado, divirta-se!!! 
jogo_adivinhacao()




