import tkinter
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image


my_file_path = r'C:\Users\ente\Desktop\gui\simon game\simon.ico'


#open tkinter
root = tkinter.Tk()
root.title('simon game ')
root.geometry('400x400')
root.iconbitmap(my_file_path)
root.resizable(0,0)


#define button color and font color
game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg=root_color)


# time global
time = 500
score = 0
game_sequence = []
player_sequence = []


#define functions

def pick_sequence():
	pass


def play_sequence():
	pass


def animate():
	pass


def change_labels():
	pass 


def test():
	pick_sequence()
	print(game_sequence)



# define layout and define frames
info_frame = tkinter.Frame(root, bg = root_color)
game_frame = tkinter.LabelFrame(root, bg = game_color)
info_frame.pack(pady = (10,20))
game_frame.pack()



# layout for the info frame
start_button = tkinter.Button(info_frame, text = "new game", font = game_font1, bg = game_color, command = test)
score_label = tkinter.Label(info_frame, text = 'score:' + str(score), font = game_font1, bg = root_color)
start_button.grid(row = 0, column = 0, padx = 20, ipadx = 30)
score_label.grid(row = 0, column = 1)


white_button = tkinter.Button(game_frame, bg = white, activebackground = white_light, borderwidth = 1)
white_button.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 60, ipady = 50)


magenta_button = tkinter.Button(game_frame, bg = magenta, activebackground = magenta_light, borderwidth = 1)
magenta_button.grid(row = 0, column = 2, columnspan = 2, padx = 10, pady = 10, ipadx = 60, ipady = 50)


yellow_button = tkinter.Button(game_frame, bg = yellow, activebackground = yellow_light, borderwidth = 1)
yellow_button.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 60, ipady = 50)

cyan_button = tkinter.Button(game_frame, bg = cyan, activebackground = cyan_light, borderwidth = 1)
cyan_button.grid(row = 1, column = 2, columnspan = 2, padx = 10, pady = 10, ipadx = 60, ipady = 50)


#make radion buttons for difficulty
difficulty = StringVar()
difficulty.set('medium')
tkinter.Label(game_frame, text = ' difficulty', font = game_font2, bg = game_color).grid(row = 2, column = 0)
tkinter.Radiobutton(game_frame, text = 'easy', variable = difficulty, value = 'easy', font = game_font2, bg = game_color).grid(row = 2, column = 1)

tkinter.Label(game_frame, text = ' difficulty', font = game_font2, bg = game_color).grid(row = 2, column = 0)
tkinter.Radiobutton(game_frame, text = 'medium', variable = difficulty, value = 'medium', font = game_font2, bg = game_color).grid(row = 2, column = 2)


tkinter.Label(game_frame, text = ' difficulty', font = game_font2, bg = game_color).grid(row = 2, column = 0)
tkinter.Radiobutton(game_frame, text = 'hard', variable = difficulty, value = 'hard', font = game_font2, bg = game_color).grid(row = 2, column = 3)

#run the program
root.mainloop()