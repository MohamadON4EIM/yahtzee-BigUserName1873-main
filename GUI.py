from scorecard import Scorecard
import tkinter  as tk
import sys
from PIL import ImageTk, Image
import random

def quit():
    sys.exit()

def roll (dice:list, images:list):
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
sc = Scorecard()
window = tk.Tk()

window.geometry("1200x900")

window.title("This is Yahtzee.")
title = tk.Label(text="Yahtzee")
title.grid(row=0, column=0)





die_spot_1 = tk.Label(image=image_list[0]).grid(row=1, column=0, padx=25)
die_spot_2 = tk.Label(image=image_list[1]).grid(row=1, column=1, padx=25)
die_spot_3 = tk.Label(image=image_list[2]).grid(row=1, column=2, padx=25)
die_spot_4 = tk.Label(image=image_list[3]).grid(row=1, column=3, padx=25)
die_spot_5 = tk.Label(image=image_list[4]).grid(row=1, column=4, padx=25)

roll_button = tk.Button(window, text = 'Roll!', command = roll(dice, image_list)).grid(row=3, column=2,padx=25)
three_of_kind_button = tk.Button(window, text = 'Claim Three of a Kind!').grid(row=3, column=0, padx=10, pady=(50, 10))
four_of_kind_button = tk.Button(window, text = 'Claim Four of a Kind!').grid(row=4, column=0,padx=10, pady=10)
full_house_button = tk.Button(window, text = 'Claim Full House!').grid(row=5, column=0,padx=10, pady=10)
sm_straight_button = tk.Button(window, text = 'Claim Small Straight!').grid(row=6, column=0,padx=10, pady=10)
lg_straight_button = tk.Button(window, text = 'Claim Large Straight').grid(row=7, column=0,padx=10, pady=10)
yahtzee_button = tk.Button(window, text = 'Claim Yahtzee!').grid(row=8, column=0,padx=10, pady=10)
chance_button = tk.Button(window, text = 'Claim Chance!').grid(row=9, column=0,padx=10, pady=10)
aces_button = tk.Button(window, text = 'Claim Aces!').grid(row=3, column=4,padx=10, pady=20)
twos_button = tk.Button(window, text = 'Claim Twos!').grid(row=4, column=4,padx=10, pady=10)
threes_button = tk.Button(window, text = 'Claim Threes!').grid(row=5, column=4,padx=10, pady=10)
fours_button = tk.Button(window, text = 'Claim Four!').grid(row=6, column=4,padx=10, pady=10)
fives_button = tk.Button(window, text = 'Claim Fives!').grid(row=7, column=4,padx=10, pady=10)
sixes_button = tk.Button(window, text = 'Claim Sixes!').grid(row=8, column=4,padx=10, pady=10)

die_1_check_box = tk.Checkbutton(window, text='Keep').grid(row=2, column= 0)
die_2_check_box = tk.Checkbutton(window, text='Keep').grid(row=2, column= 1)
die_3_check_box = tk.Checkbutton(window, text='Keep').grid(row=2, column= 2)
die_4_check_box = tk.Checkbutton(window, text='Keep').grid(row=2, column= 3)
die_5_check_box = tk.Checkbutton(window, text='Keep').grid(row=2, column= 4)



window.mainloop()