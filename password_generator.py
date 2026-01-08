# Import Libraries
import random 
import tkinter as tk
from tkinter import messagebox
# Characters to use
letters="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
symbols="!@#$"
all_chr=letters+letters.upper()+digits+symbols
# User input : desired length
def generate():
    # Generate password
    length=int(entry.get())
    password=""
    for i in range(length):
        password += random.choice(all_chr)
    result.config(text="Generated Password:"+password)
# Display password
    print("Generated Password:",password)

# Window
root=tk.Tk()
root.geometry("400x300")
root.title("Password Generator")
# Input
tk.Label(root,text="Password Length").pack()
entry=tk.Entry(root)
entry.pack()
# Button
result=tk.Button(root,text="Generate",command=generate).pack()
# Output
result=tk.Label(root,text="",font=("Arial",14))
result.pack()
root.mainloop()