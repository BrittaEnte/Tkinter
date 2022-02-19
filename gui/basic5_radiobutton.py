import tkinter
from tkinter import IntVar
from tkinter import BOTH

root = tkinter.Tk()
root.title = 'radiobutton'
root.geometry('400x400')
root.iconbitmap('ente.ico')
root.resizable(0,0)


#define functions

def make_label():
	''' print the number for the button'''
	if number.get() == 1:
		number_label = tkinter.Label(outputframe, text = 'i am a one', bg = 'blue')
	elif number.get() == 2:
		number_label = tkinter.Label(outputframe, text = 'i am a two', bg = 'blue')
	number_label.pack()
	

#define frame
inputframe = tkinter.LabelFrame(root, bg = 'green', text ='heute schien doch tatsächlich mal die sonne', width = 400, height = 200)
inputframe.pack(fill = BOTH, pady = 10, padx = 10)
outputframe = tkinter.Frame( root, bg ='blue', width = 400, height = 200)
outputframe.pack(fill = BOTH, pady = 0, padx = 10, ipady = 20)
outputframe.propagate(0)

#define buttons
number = IntVar()
number.set(1)
radio_1 = tkinter.Radiobutton(inputframe, text = 'hello', variable = number, value = 1)
radio_2 = tkinter.Radiobutton(inputframe, text = 'bye', variable = number, value = 2)
radio_1.grid(row = 0, column = 0, pady = 15, padx = 50)
radio_2.grid(row = 0, column = 1, pady = 15,   padx = 50)
print_button = tkinter.Button(inputframe, text = 'print the number', command = make_label)
print_button.grid(row  = 1, column = 0, columnspan = 2, pady = 15, padx = 15)





#run the programm
root.mainloop()