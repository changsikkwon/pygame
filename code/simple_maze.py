import tkinter
import tkinter.messagebox

mx = 1
my = 1
state = 0
key = 0


def key_down(e):
    global key
    key = e.keysym


def key_up(e):
    global key
    key = ""


def move():
    global mx, my

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

        canvas.create_rectangle(
            mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="pink", width=0, tag="PAINT"
        )
    canvas.delete("Winter")
    canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="Winter")


def count_tile():
    cnt = 0
    for i in range(7):
        for j in range(10):
            if maze[i][j] == 0:
                cnt += 1
    return cnt


def check():
    cnt = count_tile()

    if 0 not in [maze[my - 1][mx], maze[my + 1][mx], maze[my][mx - 1], maze[my][mx + 1]]:
        return 2
    elif cnt == 0:
        return 1
    else:
        return 0


def reset():
    global mx, my, state
    state = 0
    canvas.delete("PAINT")
    mx = 1
    my = 1
    for i in range(7):
        for j in range(10):
            if maze[i][j] == 2:
                maze[i][j] = 0


def main_proc():
    global mx, my, state, key
    if key == "Escape":
        key = 0
        ret = tkinter.messagebox.askyesno("Quit", "Quit?")
        if ret:
            root.destroy()
            return
    if key == "Shift_L":
        reset()

    state = check()

    if state == 0:
        move()
    if state == 1:
        canvas.update()
        tkinter.messagebox.showinfo("Clear!", "Clear!")
        reset()
    if state == 2:
        tkinter.messagebox.showinfo("Fail!", "Fail!")
        reset()

    root.after(100, main_proc)


root = tkinter.Tk()
root.title("Maze Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=560, bg="white")
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
                j * 80, i * 80, j * 80 + 79, i * 80 + 79, fill="skyblue", width=0
            )

img = tkinter.PhotoImage(file="../media/다운로드.png")
canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="Winter")
main_proc()
root.mainloop()
