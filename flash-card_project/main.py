from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
words_to_learn = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")

def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(card_image, image=front_card_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# TODO: Create flashcard flipping mechanism
def flip_card():
    canvas.itemconfig(card_image, image=back_card_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")


def is_known():
    words_to_learn.remove(current_word)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# TODO: Create flashcard UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_card_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_button_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=check_button_img, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

cross_button_img = PhotoImage(file="./images/right.png")
known_button = Button(image=cross_button_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_word()

window.mainloop()
