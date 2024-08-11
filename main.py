import random
from tkinter import *

class RockPaperSorter:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("300x200")

        self.label = Label(master, text="Choose Rock, Paper, or Scissors")
        self.label.pack(pady=10)

        self.rock_button = Button(master, text="Rock", command=lambda: self.play('r'))
        self.rock_button.pack(side=LEFT, padx=20)

        self.paper_button = Button(master, text="Paper", command=lambda: self.play('p'))
        self.paper_button.pack(side=LEFT, padx=20)

        self.scissors_button = Button(master, text="Scissors", command=lambda: self.play('s'))
        self.scissors_button.pack(side=LEFT, padx=20)

        self.result_label = Label(master, text="")
        self.result_label.pack(pady=10)

        self.play_again_button = Button(master, text="Play Again", command=self.reset)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        self.user = user_choice
        self.choices = ['r', 'p', 's']
        self.computer = random.choice(self.choices)
        result = self.logic()
        self.result_label.config(text=f"You chose {self.get_full_name(self.user)}, "
                                      f"Computer chose {self.get_full_name(self.computer)}. {result}")
        
    def logic(self):
        if self.user == self.computer:
            return "It's a tie!"
        elif self.is_win(self.user, self.computer):
            return "You won!"
        else:
            return "You lost!"

    def is_win(self, player, computer):
        # Return True if the player wins
        # r > s, s > p, p > r
        return (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r')

    def get_full_name(self, choice):
        names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        return names[choice]

    def reset(self):
        self.result_label.config(text="")
        self.label.config(text="Choose Rock, Paper, or Scissors")

# Example of how to use the class
if __name__ == "__main__":
    root = Tk()
    game = RockPaperSorter(root)
    root.mainloop()
