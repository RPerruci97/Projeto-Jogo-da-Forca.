import pygame
import random
from time import sleep
pygame.init() 
pygame.mixer.music.load("Stranger Things Theme Sound Effect.mp3")   
pygame.mixer.music.play(-1) 
pygame.event.wait()
corpo = ["""
            +------+
            |      |    
            |      
            | 
            | 
            |
            | 
            |
            ========= """, 
             """
             +------+
             |      | 
             |      O
             | 
             | 
             |
             | 
             |
             =========""", 
             """ 
             +------+
             |      | 
             |      O
             |      |
             | 
             |
             |
             |
             =========""", 
             """ 
             +------+
             |      | 
             |      O
             |     /|
             | 
             |
             |
             |
             =========""", 
             """ 
             +------+
             |      | 
             |      O
             |     /|\ 
             | 
             |
             |
             |
             =========""", 
             """ 
             +------+
             |      | 
             |      O
             |     /|\ 
             |     /
             |
             |
             |
             =========""", 
             """ 
             +------+
             |      | 
             |      O
             |     /|\ 
             |     / \ 
             |
             |
             |
             ========="""]

while True: 
    astrologia = ["mercurio", "venus", "terra", "marte", "jupiter","saturno","urano", "netuno", "aries", "touro","gemeos",    "cancer", "leao", "virgem", "libra", "escorpiao","sagitario", "capricornio", "aquario", "peixes" , "rato", "boi", "tigre", "coelho", "dragão", "cobra", "cavalo", "cabra", "macaco", "galo", "cachorro", "porco"] 
    palavra = random.choice(astrologia)

    tentativas = 0 
    chances = 7
    lacunas = ["_"] * len(palavra)
    letras_escolhidas = []


    print("+="*30)
    sleep(1)
    print("Vamos brincar de jogo da forca!".upper())
    sleep(1)
    print("+="*30)  
    sleep(1)
    print(f"Você terá {chances} tentativas para acertar a palavra!") 
    sleep(1)
    print("O tema desta forca é ASTROLOGIA! Boa sorte e divirta-se!")  
    sleep(1)

    while chances > 0 and "_" in lacunas:
        letra = input("\nDigite uma letra: ").lower()

        # Verificar se a letra já foi escolhida antes
        if letra in letras_escolhidas:
            print("Essa letra já foi escolhida. Tente novamente.")
            continue

        letras_escolhidas.append(letra)

        if letra in palavra:
            print("Você acertou uma letra!")

            # Atualizar o estado atual da palavra
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    lacunas[i] = letra

            print("Estado atual da palavra: ", " ".join(lacunas))
        else:
            print("Você errou uma letra!")
            tentativas += 1
            chances -= 1
            print(corpo[6 - chances])

        print(f"Tentativas restantes: {chances}")

        # Verificar se o jogador atingiu o limite máximo de tentativas
        if chances == 0:
            break

    # Verificar o resultado final do jogo
    if "_" not in lacunas:
        print("\nParabéns! Você venceu!")
    else:
        print("\nVocê perdeu! A palavra correta era:", palavra)

    opcao = str(input("Você deseja jogar novamente?[S/N]:")).upper() 
    if opcao == "S":
        continue 
    else:
        print("Foi ótimo jogar com você, até a próxima!")
        break 


    


