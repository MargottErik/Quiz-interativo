import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
)

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz do Indiano")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_instrucao = QLabel("Digite seu nome:")
        self.input_nome = QLineEdit()
        self.botao_iniciar = QPushButton("Começar o Quiz")
        self.botao_iniciar.clicked.connect(self.iniciar_quiz)

        self.layout.addWidget(self.label_instrucao)
        self.layout.addWidget(self.input_nome)
        self.layout.addWidget(self.botao_iniciar)

        self.nome = ""
        self.tema = ""
        self.perguntas = []
        self.pontos = 0
        self.pergunta_atual = 0

    def iniciar_quiz(self):
        self.nome = self.input_nome.text()
        if not self.nome:
            self.label_instrucao.setText("Digite seu nome antes de continuar!")
            return

        self.label_instrucao.setText(f"Olá, {self.nome}! Escolha o tema do quiz:")
        self.input_nome.hide()
        self.botao_iniciar.hide()

        self.botao_volei = QPushButton("🏐 Vôlei")
        self.botao_musica = QPushButton("🎵 Música")
        self.botao_anime = QPushButton("🎌 Anime")

        self.botao_volei.clicked.connect(lambda: self.comecar_quiz("volei"))
        self.botao_musica.clicked.connect(lambda: self.comecar_quiz("musica"))
        self.botao_anime.clicked.connect(lambda: self.comecar_quiz("anime"))

        self.layout.addWidget(self.botao_volei)
        self.layout.addWidget(self.botao_musica)
        self.layout.addWidget(self.botao_anime)

    def comecar_quiz(self, tema):
        self.tema = tema
        self.pontos = 0
        self.pergunta_atual = 0

        self.botao_volei.hide()
        self.botao_musica.hide()
        self.botao_anime.hide()

        if tema == "volei":
            self.perguntas = [
                {'questão': 'Quantos jogadores por time entram em quadra em uma partida oficial de vôlei?', 'resposta': '6'},
                {'questão': 'Qual é a posição inicial do líbero na quadra?', 'resposta': '1'},
                {'questão': 'Quem é o melhor oposto atualmente no brasil?', 'resposta': 'Darlan'},
                {'questão': 'Quantos sets uma equipe precisa vencer para ganhar a partida?', 'resposta': '3'},
                {'questão': 'Quantos toques cada equipe pode dar na bola antes de passá-la por cima da rede?', 'resposta': '3'},
                {'questão': 'Quais são as principais posições da frente da rede? Levantador, Oposto e Ponteiro; Central, Líbero; Levantador, Oposto e Líbero', 'resposta': 'Levantador, Oposto, Ponteiro'}
            ]
        elif tema == "musica":
            self.perguntas = [
                {'questão': 'Quem canta a musica Jhonny Boy? kamaitachi ou basara', 'resposta': 'kamaitachi'},
                {'questão': 'Quem canta a musica hora de devaneio? kamaitachi, anirap ou ishida', 'resposta': 'ishida'},
                {'questão': 'Quem canta a musica Algum lugar? anirap, blaze rapper ou basara', 'resposta': 'blaze rapper'},
                {'questão': 'Quem canta a musica Perdas? anirap, ishida ou lexclash', 'resposta': 'anirap'},
                {'questão': 'Quem canta a musica Aluno e Mestre? lexclash, kamaitachi ou blaze rapper', 'resposta': 'lexclash'},
                {'questão': 'Quem canta a musica ainda mais esforço e menos sorte? basara, Enigma ou lexclash', 'resposta': 'basara'}
            ]
        elif tema == "anime":
            self.perguntas = [
                {'questão': 'Quem morreu mais vezes: Meliodas ou Subaru Natsuki?', 'resposta': 'subaru natsuki'},
                {'questão': 'Qual desses mangás foi mais lido em 2024? Vagabond, Berserk ou One-Punch Man', 'resposta': 'Vagabond'},
                {'questão': 'Quem é o criador de One Piece? Hayao Miyazaki, Eiichiro Oda ou Akira Toriyama', 'resposta': 'Eiichiro Oda'},
                {'questão': 'Qual o anime mais longo da história? One Piece, Sazae-san ou Yami Shibai', 'resposta': 'Sazae-san'},
                {'questão': 'Quem é o melhor amigo do Satoru Gojo? suguru geto, yuji itadori ou yuta okkotsu', 'resposta': 'suguru geto'},
                {'questão': 'Quem Megumi considerou como seu pai? toji, gojo, nanami ou haroraga', 'resposta': 'gojo'}
            ]
        random.shuffle(self.perguntas)

        self.label_pergunta = QLabel("")
        self.input_resposta = QLineEdit()
        self.botao_responder = QPushButton("Responder")
        self.botao_responder.clicked.connect(self.verificar_resposta)

        self.layout.addWidget(self.label_pergunta)
        self.layout.addWidget(self.input_resposta)
        self.layout.addWidget(self.botao_responder)

        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        if self.pergunta_atual < len(self.perguntas):
            self.label_pergunta.setText(self.perguntas[self.pergunta_atual]["questão"])
            self.input_resposta.setText("")
        else:
            self.finalizar_quiz()

    def verificar_resposta(self):
        resposta_usuario = self.input_resposta.text().lower().strip()
        resposta_correta = self.perguntas[self.pergunta_atual]["resposta"].lower().strip()
        if resposta_usuario == resposta_correta:
            self.label_pergunta.setText("Acertou!")
            self.pontos += 1
        else:
            self.label_pergunta.setText(f"Errou! Resposta certa: {self.perguntas[self.pergunta_atual]['resposta']}")

        self.pergunta_atual += 1
        QTimer.singleShot(1500, self.mostrar_pergunta)  # Espera 1.5s e mostra a próxima

    def finalizar_quiz(self):
        self.label_pergunta.setText(f"Fim do Quiz, {self.nome}! Você acertou {self.pontos} de {len(self.perguntas)}.")
        self.input_resposta.hide()
        self.botao_responder.hide()

if __name__ == "__main__":
    from PySide6.QtCore import QTimer
    app = QApplication(sys.argv)
    quiz = QuizApp()
    quiz.show()
    sys.exit(app.exec())