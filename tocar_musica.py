import pyfiglet 
titulo = pyfiglet.figlet_format("Quiz do indiano", font="slant")
print(titulo)
titulo_pequeno = pyfiglet.figlet_format("salve!", font="digital")
print(titulo_pequeno)

import random

from colorama import Back, init
init(autoreset=True)

from termcolor import colored


nome = input('Qual é o seu nome?:')
print(Back.GREEN   + f'Prazer em te conhecer, {nome}!')
resposta = input('Vamos jogar um Quiz? (responda com sim ou não) ')

if resposta.lower() == 'sim':
    print(Back.RED + 'Ótimo! Vamos começar.', "red")
    print(colored('Temos três temas:', 'red'))
    print(colored('1. volei\n2. musica\n3. anime', 'cyan'))
    tema_escolhido = input(colored('Escolha seu tema: ', 'green')).lower().strip()

    perguntas = []

    if tema_escolhido == 'volei':
        perguntas = [
            {'questão': 'Quantos jogadores por time entram em quadra em uma partida oficial de vôlei?', 'resposta': '6'},
            {'questão': 'Qual é a posição inicial do líbero na quadra?', 'resposta': '1'},
            {'questão': 'Quem é o melhor oposto atualmente no brasil?', 'resposta': 'Darlan'},
            {'questão': 'Quantos sets uma equipe precisa vencer para ganhar a partida?', 'resposta': '3'},
            {'questão': 'Quantos toques cada equipe pode dar na bola antes de passá-la por cima da rede?', 'resposta': '3'},
            {'questão': 'Quais são as principais posições da frente da rede? Levantador, Oposto e Ponteiro; Central, Líbero; Levantador, Oposto e Líbero', 'resposta': 'Levantador, Oposto, Ponteiro'}
        ]
    elif tema_escolhido == 'musica':
        perguntas = [
            {'questão': 'Quem canta a musica Jhonny Boy? kamaitachi ou basara', 'resposta': 'kamaitachi'},
            {'questão': 'Quem canta a musica hora de devaneio? kamaitachi, anirap ou ishida', 'resposta': 'ishida'},
            {'questão': 'Quem canta a musica Algum lugar? anirap, blaze rapper ou basara', 'resposta': 'blaze rapper'},
            {'questão': 'Quem canta a musica Perdas? anirap, ishida ou lexclash', 'resposta': 'anirap'},
            {'questão': 'Quem canta a musica Aluno e Mestre? lexclash, kamaitachi ou blaze rapper', 'resposta': 'lexclash'},
            {'questão': 'Quem canta a musica ainda mais esforço e menos sorte? basara, Enigma ou lexclash', 'resposta': 'basara'}
        ]
    elif tema_escolhido == 'anime':
        perguntas = [
            {'questão': 'Quem morreu mais vezes: Meliodas ou Subaru Natsuki?', 'resposta': 'subaru natsuki'},
            {'questão': 'Qual desses mangás foi mais lido em 2024? Vagabond, Berserk ou One-Punch Man', 'resposta': 'Vagabond'},
            {'questão': 'Quem é o criador de One Piece? Hayao Miyazaki, Eiichiro Oda ou Akira Toriyama', 'resposta': 'Eiichiro Oda'},
            {'questão': 'Qual o anime mais longo da história? One Piece, Sazae-san ou Yami Shibai', 'resposta': 'Sazae-san'},
            {'questão': 'Quem é o melhor amigo do Satoru Gojo? suguru geto, yuji itadori ou yuta okkotsu', 'resposta': 'suguru geto'},
            {'questão': 'Quem Megumi considerou como seu pai? toji, gojo, nanami ou haroraga', 'resposta': 'gojo'}
        ]
    else:
        print('voce digitou errado, seu analfabeto digita de novo mais certo dassa vez')

    if perguntas:
        random.shuffle(perguntas)
        pontos = 0
        for questao in perguntas:
            resposta_usuario = input(f"\n{questao['questão']}\nSua resposta: ").lower().strip()
            if resposta_usuario == questao['resposta'].lower().strip():
                print(Back.BLUE + 'acertou!')
                pontos += 1
            else:
                print(Back.RED + f'voce errou seu burro! A resposta correta era: {questao["resposta"]}')

        print(f'\n--- Fim do Quiz ---')
        print(f'Você fez {pontos} de {len(perguntas)} pontos.')

    elif resposta.lower() == 'nao':
        print('Ah, que pena. Fica para a próxima!')
    else:
        print('porra voce e burro??, não entendi sua resposta.')