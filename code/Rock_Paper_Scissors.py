import tkinter
import random

from PIL import ImageTk


def click_btn(user_choice):
    computer_choice = random.choice(["Scissor", "Rock", "Paper"])
    com_rps_label["text"] = computer_choice
    com_rps_label.update()

    user_rps_label["text"] = user_choice
    user_rps_label.update()

    res = ""
    if computer_choice == user_choice:
        res = "Draw"
    else:
        if user_choice == "Scissor":
            res = "Win!" if computer_choice == "Paper" else "Lose"
        if user_choice == "Rock":
            res = "Win!" if computer_choice == "Scissor" else "Lose"
        if user_choice == "Paper":
            res = "Win!" if computer_choice == "Rock" else "Lose"

    result_label["text"] = res
    result_label.update()


root = tkinter.Tk()
root.title("Rock Paper Scissor")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

image = ImageTk.PhotoImage(file="../media/다운로드 (33).jpeg")
canvas.create_image(400, 300, image=image)

com_label = tkinter.Label(root, text="Computer", font=("Times New Roman", 55))
user_label = tkinter.Label(root, text="User", font=("Times New Roman", 55))
com_rps_label = tkinter.Label(root, text="??", font=("Times New Roman", 55))
user_rps_label = tkinter.Label(root, text="??", font=("Times New Roman", 55))
result_label = tkinter.Label(root, text="Win or Lose", font=("Times New Roman", 55))

com_label.place(x=100, y=100)
com_rps_label.place(x=100, y=200)
user_label.place(x=600, y=100)
user_rps_label.place(x=600, y=200)
result_label.place(x=320, y=350)

scissor_btn = tkinter.Button(
    root,
    text="Scissor",
    fg="skyblue",
    command=lambda: click_btn("Scissor"),
    font=("Times New Roman", 55),
)
rock_btn = tkinter.Button(
    root, text="Rock", fg="skyblue", command=lambda: click_btn("Rock"), font=("Times New Roman", 55)
)
paper_btn = tkinter.Button(
    root,
    text="Paper",
    fg="skyblue",
    command=lambda: click_btn("Paper"),
    font=("Times New Roman", 55),
)

scissor_btn.place(x=20, y=500)
rock_btn.place(x=335, y=500)
paper_btn.place(x=620, y=500)

root.mainloop()
