#Number Guessing Game

#The "Brain" (Imports): import tkinter and import random are like grabbing a toolbox. 
# One box helps us draw the window, and the other helps the computer pick a surprise number.

import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:

    # The "Setup" (__init__): This is like setting the stage for a play. 
    # We tell the window how big to be, give it a title, and hide the 
    # secret number where the player can’t see it yet.

    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x250")

        # Game State
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 5

        # The "Buttons and Boxes" (UI Elements): These are the toys on the screen.
        # The Label is the instruction sign, the Entry is the "mailbox" where you put your guess
        # and the Button is the "Go!" switch.

        # UI Elements
        self.label = tk.Label(root, text="Guess a number between 1 and 100", pady=10)
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.btn_guess = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.btn_guess.pack(pady=10)

        self.stats_label = tk.Label(root, text=f"Guesses left: {self.guesses_left}")
        self.stats_label.pack(pady=10)

    # The "Judge" (check_guess): This is the most important part! 
    # It looks at the number you typed and compares it to the secret one. 
    # It’s like a referee saying, "Higher!" or "Lower!"

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        if user_guess == self.secret_number:
            messagebox.showinfo("Winner!", "Well done, you guessed the right number!")
            self.reset_game()
        elif user_guess < self.secret_number:
            self.handle_incorrect("Too low!")
        else:
            self.handle_incorrect("Too high!")

        self.entry.delete(0, tk.END)

    # The "Second Chance" (handle_incorrect): If you miss, this part takes away one of your 
    # "lives" (guesses). If you run out of lives, it tells you the answer and starts 
    # the game over so you can try again.

    def handle_incorrect(self, hint):
        self.guesses_left -= 1
        if self.guesses_left > 0:
            self.stats_label.config(text=f"{hint} Guesses left: {self.guesses_left}")
        else:
            messagebox.showerror("Game Over", f"Out of guesses! The number was {self.secret_number}.")
            self.reset_game()

    # The "Cleanup" (reset_game): Just like cleaning up toys after playing, 
    # this puts everything back to the start so a new game can begin.

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 5
        self.stats_label.config(text=f"Guesses left: {self.guesses_left}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()


