# Rock Paper Scissor 
# Import Libraries
import random
import tkinter as tk
# Get ai choice
def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])
# Determine the winner
def determine_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "It's a Tie!"
    elif (player_choice == "rock" and ai_choice == "scissors") or \
         (player_choice == "paper" and ai_choice == "rock") or \
         (player_choice == "scissors" and ai_choice == "paper"):
        return "You Win!"
    else:
        return "AI Wins!"
# GUI
# Initial Score 
player_score = 0
ai_score = 0
# Game
def play(player_choice):
    global player_score, ai_score
    
    ai_choice = get_ai_choice()
    result = determine_winner(player_choice, ai_choice)
    
    if result == "You Win!":
        player_score += 1     # Track score of Player
    elif result == "AI Wins!":
        ai_score += 1         # Track score of AI

    result_label.config(text=f"Your Choice: {player_choice}\nAI Choice: {ai_choice}\n\n{result}")
    score_label.config(text=f"Player: {player_score}   AI: {ai_score}")

# GUI
# Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x350")
# Labels
# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack(pady=10)
# Score
score_label = tk.Label(root, text="Player: 0   AI: 0", font=("Arial", 12))
score_label.pack(pady=5)
# Result
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 11))
result_label.pack(pady=10)
# Buttons
# Rock Button
rock_btn = tk.Button(root, text="Rock", width=10, command=lambda: play("rock"))
rock_btn.pack(pady=5)
# Paper BUtton
paper_btn = tk.Button(root, text="Paper", width=10, command=lambda: play("paper"))
paper_btn.pack(pady=5)
# Scissor Button
scissors_btn = tk.Button(root, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_btn.pack(pady=5)

root.mainloop()
