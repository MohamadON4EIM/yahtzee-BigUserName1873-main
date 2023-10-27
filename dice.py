import random
from PIL import ImageTk, Image
import tkinter  as tk


class Dice:
    def __init__(self) -> None:
        self.roll = True
        self.Dice1 = 1
        self.Dice2 = 2
        self.Dice3 = 3
        self.Dice4 = 4
        self.Dice5 = 5
        self.Dice6 = 6
        self.Dice_list = []


    def roll (self):
        for i in range(5):
            num = random.randint(1,6)
            dice.append(num)
            die_spot_1 = tk.Label(image=image_list[dice[i]]).grid(row=1, column=0, padx=25)
            die_spot_2 = tk.Label(image=image_list[dice[i]]).grid(row=1, column=1, padx=25)
            die_spot_3 = tk.Label(image=image_list[dice[i]]).grid(row=1, column=2, padx=25)
            die_spot_4 = tk.Label(image=image_list[dice[i]]).grid(row=1, column=3, padx=25)
            die_spot_5 = tk.Label(image=image_list[dice[i]]).grid(row=1, column=4, padx=25)
        print (dice)

dice = []
image_list = [
    ImageTk.PhotoImage(Image.open(f'images\\die_{num}.PNG')) for num in range(1,7)
    ]
