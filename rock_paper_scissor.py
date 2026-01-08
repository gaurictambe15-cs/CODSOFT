# Import library
import random
# Get ai choice
def get_ai_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)
# get player choice
def get_player_choice():
    choice=input("Enter your choice(rock,paper,scissors):").lower()
    while choice not in ["rock","paper","scissors"]:
        choice=input("Invalid choice").lower()
    return choice
# Determine the winner
def determine_winner(player_choice,ai_choice):
    if player_choice==ai_choice:
        return "It's a tie !"
    elif (player_choice=="rock" and ai_choice=="scissors")or\
        (player_choice=="paper" and ai_choice=="rock")or\
        (player_choice=="scissors" and ai_choice=="paper"):
        return "You Win !"
    else:
        return "AI Wins !"
# Game
def play_game():
    print("Welcome to Rock,Pape,Scissors game !")
    while True:
        player_choice=get_player_choice()
        ai_choice=get_ai_choice()
        print(f"You chose:{player_choice}")
        print(f"AI chose:{ai_choice}")
        result=determine_winner(player_choice,ai_choice)
        print(result)
        play_again=input("\nDo you Wanna Play again? (Yes/No):").lower()
        if play_again!="yes":
            print("Thanks for playing !")
            break
if __name__=="__main__":
    play_game()

    
