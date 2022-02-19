import tkinter
from tkinter import BOTH
from tkinter import IntVar, StringVar
from PIL import ImageTk, Image

# set root
root = tkinter.Tk()
root.title('Hello GUI')
root.geometry('800x800')
root.iconbitmap('ente.ico')
root.resizable(0,0)
root.config(bg = '#4885ed')

#define functions

def printtext():
	''' prints the required text'''
	# create a label for the user name of radio button values
	if case_style.get() == 'normal':
		name_label = tkinter.Label(big_frame, text = 'Hello' + ' ' + entry.get() + '!!', bg = '#f4c20d')
	elif case_style.get() == 'upper':
		name_label = tkinter.Label(big_frame, text = 'HELLO ' + ' ' + entry.get() + ' ' + 'KEEP LEARNING', bg = '#f4c20d' )
	name_label.pack()


#erst frame setzen ohne alles und dann anpassen mit den widgets!!!

#set frame
little_frame = tkinter.Frame(root, bg = '#3cba54')
big_frame = tkinter.Frame(root, bg = '#f4c20d')
little_frame.pack(pady = 10)
big_frame.pack(padx = 10, pady = (0,10), fill = BOTH, expand = True)



#make the picture
my_image = tkinter.PhotoImage(file = 'duck1.png')
my_label = tkinter.Label(big_frame, image = my_image)
my_label.pack(pady = 15)


#make the entry button 
entry = tkinter.Entry( little_frame, text = 'enter your name', width = 40)
entry.grid(row = 0, column = 0, pady = 15, padx = 0)

#make the submit buttoon
button = tkinter.Button(little_frame, text = 'submit', command = printtext)
button.grid(row = 0, column = 1, pady = 15, padx = 0, ipadx = 40)

#make the radiobuttons
case_style = StringVar()
case_style.set('normal')
radio1 = tkinter.Radiobutton(little_frame, text = 'Normalcase', width = 50, variable = case_style, value = 'normal', bg = '#3cba54')
radio2 = tkinter.Radiobutton(little_frame, text = 'Uppercase', width = 50, variable = case_style, value = 'upper', bg = '#3cba54')
radio1.grid(row = 1, column = 0, pady = 15, padx = 0)
radio2.grid(row = 1, column = 1, pady = 15, padx = 0)












#run mainloop
root.mainloop()