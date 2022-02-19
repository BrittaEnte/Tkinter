import tkinter
from tkinter import END

# define window

root = tkinter.Tk()
#set title
root.title('ente gut, alles gut')

#set icon, geht nur mit ico dateien
root.iconbitmap('ente.ico')
root.config(bg = '#30C5FF' )

root.geometry('500x500')
root.resizable(0,0)

#define my functions
def make_label():
	''' print a label to the app'''
	text = tkinter.Label(output_frame, text = text_entry.get(), bg = 'red')
	text.pack()

	text_entry.delete(0, END)

def count(number):
	global value
	text = tkinter.Label(output_frame, text = number, bg = 'red')	
	value = number + 1
	text.pack()

#define frames
input_frame = tkinter.Frame(root, bg ='#0000ff', width=500, height=100)
output_frame = tkinter.Frame(root, bg = '#ff0000', width=500, height=400)

#pack the frames
input_frame.pack(pady = 5, padx = 10)
output_frame.pack(pady = 5, padx = 10)


#add inputs
text_entry = tkinter.Entry(input_frame, width = 40)
text_entry.grid(row = 0, column = 0, padx = 10, pady = 10)

# we want that the inpute frame still have the size originally given and the same for the output frame. 
# das bezieht sich auf text.pack(output) and button.grid(input)
output_frame.pack_propagate(0)
input_frame.grid_propagate(0)

#produce a print button
print_button = tkinter.Button(input_frame, text = 'print!', command = make_label)
print_button.grid(row = 0, column = 1, pady = 5, padx = 5, ipadx = 30)

#produce a count button with lambda
value = 0
count_button = tkinter.Button(input_frame, text = 'count', command = lambda:(count(value)))
count_button.grid(row = 1, column = 0, pady = 5, padx = 5, ipadx = 30)


#run the mainloop
root.mainloop()
