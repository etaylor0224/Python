from tkinter import *
import pandas as pd
import random

# ----CONSTANTS----

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv(r"data\words_to_learn.csv")

except FileNotFoundError:
    df = pd.read_csv(r"data\french_words.csv")
finally:
    learn = df.to_dict(orient="records")

current_card = {}

# ----Functions----
def update_word():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(learn)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_time = window.after(3000, func=card_flip)

def card_flip():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=card_back)

def check_button():
    learn.remove(current_card)
    df_learn = pd.DataFrame(learn)
    df_learn.to_csv("words_to_learn.csv")
    update_word()

# ----UI SETUP----

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file=r"images\card_back.png")
card_front = PhotoImage(file=r"images\card_front.png")
check_image = PhotoImage(file=r"images\right.png")
wrong_image = PhotoImage(file=r"images\wrong.png")
card = canvas.create_image(400,263, image=card_front)
language = canvas.create_text(400, 150,text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263,text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
check_button = Button(image=check_image, highlightthickness=0, command=check_button)
check_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=update_word)
wrong_button.grid(column=0, row=1)

update_word()

window.mainloop()
