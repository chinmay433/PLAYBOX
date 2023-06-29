import turtle

wn = turtle.Screen()
canvas = wn.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

tess = turtle.Turtle()

def on_close():
    global running
    running = False

root.protocol("WM_DELETE_WINDOW", on_close)

running = True

while running:
    tess.forward(50)
    if not running:
        break
    tess.left(120)
    if not running:
        break
    tess.forward(50)