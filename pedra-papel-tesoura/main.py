from distutils.command.clean import clean
from optparse import Option
import random
from turtle import clear

user_win=0
computer_win=0
draw=0

options = ["pedra", "papel","tesoura"]
options[0]

while True:
    user_input = input("Type pedra/papel/tesoura or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in ["pedra", "papel","tesoura"]:
        continue    

    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("O computador escolheu",computer_pick + ".")

    if user_input == "pedra" and computer_pick == "tesoura":
        print("Você Ganhou")
        user_win += 1
    elif user_input == "papel" and computer_pick == "pedra":
        print("Você Ganhou")
        user_win += 1
    elif user_input == "tesoura" and computer_pick == "papel":
        print("Você Ganhou")
        user_win += 1
    else:
        if user_input == "pedra" and computer_pick == "pedra":
            print("Empate")
            draw += 1
        else:
            if user_input == "papel" and computer_pick == "papel":
                print("Empate")
                draw += 1
            else:
                if user_input == "tesoura" and computer_pick == "tesoura":
                    print("Empate")
                    draw += 1
                else:
                    print("Você Perdeu")
                    computer_win += 1   

print("O jogador ganhou", user_win, "vezes")
print("O computador ganhou", computer_win, "vezes")
print("Houve ", draw, "empates")
print("Até Mais")
