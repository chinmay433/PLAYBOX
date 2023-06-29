from tkinter import *
from subprocess import call




def pong_start():

    call(["python", "pong_game/main.py"])

def snake_start():

    call(["python", "snake_game/main.py"])

def start_black_jack():

    call(["python","black jack/main.py"])

def start_state():
    call(["python","state_game/main.py"])

def start_crossing():
    call(["python","turtle crossing/main.py"])


FONT_NAME="Game Over OTF"
BG_COLOR="#ADE792"
window =Tk()
window.geometry("600x600")
bg=PhotoImage(file="background.png")

canvas=Canvas(window,width=600,height=600)
canvas.create_image(300,300,image=bg)

canvas.pack(fill="both",expand = True)

window.config(pady=20,padx=20)
window.title("Play Box")
window.minsize(width=600,height=600)
play_box_label=Label(text="Play Box",font=(FONT_NAME, 25, "bold"))

#play_box_label.grid(row=0,column=1,padx=20,pady=20)

snake_icon=PhotoImage(file="icon.png")
snake_button=Button(image=snake_icon,relief="groove",command=snake_start,compound="top",text="Snake",font=("HK modular", 10, "bold"))
button1=canvas.create_window(120,430,anchor = "nw", window = snake_button)

#snake_button.grid(row=2,column=0,padx=20,pady=20)

pong_icon=PhotoImage(file="icons8-ping-pong-64.png")
pong_button=Button(image=pong_icon,relief="groove",command=pong_start,compound="top",text="Ping Pong",font=("HK modular", 10, "bold"))
button2=canvas.create_window(450,160,anchor = "nw", window =pong_button)


#pong_button.grid(row=2,column=2,padx=20,pady=20)

black_jack_icon=PhotoImage(file="blackjack icon.png")
black_jack_button=Button(image=black_jack_icon,relief="groove",command=start_black_jack,compound="top",text="Blackjack",font=("HK modular", 10, "bold"))
button3=canvas.create_window(420,430,anchor = "nw", window = black_jack_button)

#black_jack_button.grid(row=4,column=0,padx=20,pady=20)

state_icon=PhotoImage(file="state_icon.png")
state_button=Button(image=state_icon,command=start_state,compound="top",text="Guess States",font=("HK modular", 10, "bold"))
button4=canvas.create_window(65,160,anchor = "nw", window = state_button)

#state_button.grid(row=4,column=2,padx=20,pady=20)

crossing_icon=PhotoImage(file="turtle icon.png")
crossing_button=Button(window,image=crossing_icon,relief="groove",command=start_crossing,compound="top",text="Turtle Cross",font=("HK modular", 10, "bold"))
#crossing_button.grid(row=5,column=0,padx=20,pady=20)
button5=canvas.create_window(265,20,anchor = "nw", window = crossing_button)
window.mainloop()