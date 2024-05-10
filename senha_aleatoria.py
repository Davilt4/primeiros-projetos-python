import random

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maisculas = letras_minusculas.upper()
numeros = "0123456789"

while True:
    tamanho = int(input("Digite o numéro de caracteres: "))    

    if tamanho>3:
        if tamanho % 3 == 0:
            tamanho_maisculo = (tamanho//3)
            tamanho_minusculo = (tamanho//3)
            tamanho_numeros = (tamanho//3)

        
        else:
            tamanho_maisculo = (tamanho//3)+(tamanho%3)
            tamanho_minusculo = (tamanho//3)
            tamanho_numeros = (tamanho//3)

        
        def gerar_senha():
            caractere_maiusculo ="".join(random.choices(letras_maisculas,k=(tamanho_maisculo)))
            dois_numeros = "".join(random.choices(numeros, k=(tamanho_minusculo)))
            cinco_letras_minusculas = "".join(random.choices(letras_minusculas,k=(tamanho_numeros)))
            senha = caractere_maiusculo + dois_numeros + cinco_letras_minusculas
            senha_embaralhada = "".join(random.sample(senha, len(senha)))
            print(len(senha_embaralhada))
            return senha_embaralhada
            
        print(f"A senha gerada é: {gerar_senha()}") 
        
    else:
        print("A senha deve ter pelo menos 3 caracteres")
    continuar = input("Deseja continuar(s/n)? ").lower()

    
    if continuar in "sS" or continuar[0] == "s":
        continue

    
    elif continuar in 'nN' or continuar[0] == "n":
        print("Programa encerrado.")
        break

    
