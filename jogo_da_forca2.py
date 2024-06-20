import random
import os
import time


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def escolher_palavra(possiveis_palavras):
    return random.choice(possiveis_palavras)

def atualizar_palavra_formatada(palavra_secreta, letras_acertadas):
    return "".join([letra if letra in letras_acertadas else '_' for letra in palavra_secreta])

def jogo_da_forca():
    limpar_tela()
    
    possiveis_palavras = ['banana', 'segredo', 'cebola', 'lactose']
    palavra_secreta = escolher_palavra(possiveis_palavras)
    palavra_formatada = "_" * len(palavra_secreta)
    letras_acertadas = set()
    letras_erradas = set()
    tentativas = len(palavra_secreta)
    
    while tentativas > 0 and palavra_formatada != palavra_secreta:
        limpar_tela()
        print(f"Você tem {tentativas} tentativas.")
        print(f"Palavra: {palavra_formatada}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        palpite = input("Digite uma letra ou seu palpite da palavra completa: ").lower()
        
        if not palpite.isalpha() or len(palpite) == 0:
            print("====DIGITE APENAS LETRAS!====")
            time.sleep(1)
            continue
        
        if palpite == palavra_secreta:
            palavra_formatada = palavra_secreta
            break
        
        if palpite == 'sair':
            print("Encerrando o programa!")
            break
        
        if palpite in letras_acertadas or palpite in letras_erradas:
            print("Você já digitou essa letra!")
            time.sleep(.7)
            continue
        
        if len(palpite) > 1:
            if palpite != palavra_secreta:
                print("Seu palpite está errado!")
                tentativas -= 1
                time.sleep(.7)
                continue
        
        tentativas -= 1
        
        if palpite in palavra_secreta:
            print(f"Muito bem, a palavra tem a letra '{palpite}'")
            letras_acertadas.add(palpite)
            time.sleep(.7)
        else:
            print(f"A palavra não tem a letra '{palpite}'")
            letras_erradas.add(palpite)
            time.sleep(.7)
        
        palavra_formatada = atualizar_palavra_formatada(palavra_secreta, letras_acertadas)
    
    limpar_tela()
    if palavra_formatada == palavra_secreta:
        print(palavra_formatada)
        print("Parabéns, você adivinhou a palavra secreta.")
    else:
        print(f"Não foi dessa vez. A palavra secreta era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_da_forca()
