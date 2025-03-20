import random

pontuacao_usuario = 0
pontuacao_computador = 0

opcoes = ["r", "p", "t"]

while True:
    escolha_usuario = input("\n Escolha uma opção: \n (R)Pedra \n (P)Papel \n (T)Tesoura ou Q para sair. \n Resposta: ").lower()

    if escolha_usuario == "q":
        break

    if escolha_usuario not in opcoes:
        continue
        

    escolha_computador = random.randint(0,2)
    # 0 = Pedra, 1 = Papel, 2 = Tesoura
    escolha_computador = opcoes[escolha_computador]

    print(f"O computador escolheu: {escolha_computador}")

    if escolha_computador == escolha_usuario:
        print(f"Empate!, os dois escolheram {escolha_usuario}")
    elif escolha_usuario == "r" and  escolha_computador == "t":
        print("Você ganhou!")
        pontuacao_usuario = pontuacao_usuario + 1
    elif escolha_usuario == "p" and escolha_computador == "r":
        print("Você ganhou!")
        pontuacao_usuario = pontuacao_usuario + 1
    elif escolha_usuario == "t" and escolha_computador == "p":
        print("Você ganhou!")
        pontuacao_usuario = pontuacao_usuario + 1
    else:
        print("O computador ganhou!")
        pontuacao_computador = pontuacao_computador + 1

print("----------------------JOGO FINALIZADO-------------------\n")
print(f"Sua pontuação: {pontuacao_usuario} ")
print(f"Pontuação do computador: {pontuacao_computador}")

if pontuacao_computador > pontuacao_usuario:
    print("Que pena!! Você perdeu!!")
elif pontuacao_usuario == pontuacao_computador:
    print("Deu empate!")
else: print("Parabéns!! Você ganhou!!")


    
print("Até breve!")