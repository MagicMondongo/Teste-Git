import random # Trazemos a biblioteca de aleatoriedade do Python

def iniciar_jogo():
    print("====================================")
    print("Bem-vindo ao Jogo de Adivinhação! 🎮")
    print("====================================")
    
    # O computador escolhe um número entre 1 e 50
    numero_secreto = random.randint(1, 50)
    tentativas = 0
    acertou = False
    
    print("Eu pensei em um número entre 1 e 50. Consegue adivinhar qual é?")

    # O "Game Loop" - O jogo continua rodando enquanto você não acertar
    while not acertou:
        # Pede para o jogador digitar um número
        chute_str = input("Digite o seu palpite: ")
        
        # Converte o texto que o jogador digitou para um número inteiro
        chute = int(chute_str)
        tentativas += 1 # Adiciona 1 ao contador de tentativas
        
        # O jogo verifica se você acertou, chutou alto ou chutou baixo
        if chute == numero_secreto:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            acertou = True # Isso quebra o loop e encerra o jogo
        elif chute > numero_secreto:
            print("👇 Muito alto! Tente um número menor.")
        else:
            print("👆 Muito baixo! Tente um número maior.")

    print("Fim de jogo. Obrigado por jogar!")

# Essa linha faz o jogo rodar quando executamos o arquivo
if __name__ == "__main__":
    iniciar_jogo()
