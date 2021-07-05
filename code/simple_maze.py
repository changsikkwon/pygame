import tkinter
import tkinter.messagebox

key = 0
mx = 1
my = 1
yuka = 0


def key_down(e):
    global key
    key = e.keysym


def key_up(e):
    global key
    key = ""


def main_proc():
    global mx, my, yuka

    if key == "Shift_L" and yuka > 1:
        canvas.delete("PAINT")
        mx = 1
        my = 1
        yuka = 0
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0

    if key == "Up" and maze[my - 1][mx] == 0:
        my -= 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my += 1
    if key == "Left" and maze[my][mx - 1] == 0:
        mx -= 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx += 1

    if maze[my][mx] == 0:
        maze[my][mx] = 2
        yuka += 1
        canvas.create_rectangle(
            mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="light green", width=0, tag="PAINT"
        )
    canvas.delete("mimi")
    canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="mimi")

    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("Clear!", "Clear!")
    else:
        root.after(200, main_proc)


root = tkinter.Tk()
root.title("Maze Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

for i in range(7):
    for j in range(10):
        if maze[i][j] == 1:
            canvas.create_rectangle(
                j * 80, i * 80, j * 80 + 79, i * 80 + 79, fill="sky blue", width=0
            )

img = tkinter.PhotoImage(file="../media/다운로드.png")
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="mimi")
main_proc()
root.mainloop()
