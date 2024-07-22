import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

possiveis_palavras = ['segredo', 'banana', 'cebola', 'lactose']
palavra_secreta = "".join(random.choice(possiveis_palavras))
palavra_formatada = "_"*(len(palavra_secreta))
letras_acertadas = ""
letras_erradas = ""
chute_palavra = ""
tentativas = len(palavra_secreta) + int( len(palavra_secreta)/4)

while tentativas >= 1 and palavra_formatada != palavra_secreta:

    print(f"Você tem {tentativas} tentativas.")
    print(palavra_formatada)
    palpite = input("Digite uma letra ou seu palpite da palavra completa: ").lower()

    if not palpite.isalpha():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====DIGITE APENAS LETRAS!====")
        tentativas -= 1
        continue

    if palpite == palavra_secreta:
        palavra_formatada = palavra_secreta
        break

    if palpite == 'sair':
        print("Encerrando o programa!")
        break

  
    if palpite in letras_acertadas or palpite in letras_erradas: #Verifica se o usuario ja digitou esse palpite antes.
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Você ja digitou essa letra!")
        continue

    if len(palpite) > 1:
        if palpite != palavra_secreta:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Seu palpite está errado!")
            tentativas-=1
            continue

   
    tentativas -= 1
    
    palavra_usuario = "" #É essencial que essa variável seja transformada em uma string vazia em cada loop do while.


    if palpite in palavra_secreta: #Verifica se o palpite esta na palavra secreta.
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Muito bem, a palavra tem a letra '{palpite}'")
        letras_acertadas += palpite 
        for i in range(len(palavra_secreta)): #Esse for troca '_' pelo palpite ou deixa '_' caso não seja o palpite.
            if palavra_secreta[i] == palpite:
                palavra_usuario += palpite
            else:
                palavra_usuario += palavra_formatada[i]


    else: #O palpite não esta na palavra secreta!
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(palpite) == 1:
            print(f"A palavra não tem a letra '{palpite}'")
        palavra_usuario = palavra_formatada #Como não passou pelo for, atribuo o valor da palavra_formatada para o palavra_ usuario, pois posteriormente o valor de palavra_usuario deve ser passado para palavra_formatada para muda-la permanentemente. Tive que criar essa atribuição pois se o primeiro palpite não estiver na palavra_secreta a palavra_formatada ia receber um valor de string vazia. Caso o primeiro palpite esteja na palavra_secreta essa atribuição não é necessária pois o for irá atribuir um valor para a palavra-usuario.
        letras_erradas += palpite
        

    palavra_formatada = palavra_usuario #Muda permanentemante as mudanças feitas no for acima.


#Prints finais
if palavra_formatada == palavra_secreta:
    print(palavra_formatada)
    print("Parabéns, você adivinhou a palavra secreta.")
else:
    print(f"Não foi dessa vez. A palava secreta é: {palavra_secreta}")
