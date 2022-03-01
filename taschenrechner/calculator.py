import tkinter
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL
from tkinter import IntVar, StringVar, ttk 
from PIL import ImageTk, Image

my_file_path = r'C:\Users\ente\Desktop\gui\taschenrechner\calc.ico'

#set font
my_font = ('Times New Roman', 15)
display_font = ('Times New Roman', 25)

#set color 
root_color = '#91A57E'
first_buttons = '#7E9971'
green_button = '#588157'
figure_button = '#344E41'
input_button = '#DAD7CD'

#define functions
def submit_number(number):
	'''put the number clicked on the entry field'''
	input_field.insert(END, number)
	''' if decimal was pressed disable this button '''
	if "." in input_field.get():
		punkt_button.config(state = DISABLED)


def operate(operator):
	''' store the operator of the expression and the operation be used'''
	global first_number
	global operation	


	# geht the operator pressed and teh current value of the display. this is the first number in the calculation
	operation = operator
	first_number = input_field.get()

	#delete first number from entry display
	input_field.delete(0, END)	

	#disable all operator buttons until equal or clear is pressed 
	minus_button.config(state = DISABLED)
	mal_button.config(state = DISABLED)
	plus_button.config(state = DISABLED)	
	geteilt_button.config(state = DISABLED)
	eins_x_button.config(state = DISABLED)
	xhochn_button.config(state = DISABLED)
	hoch2_button.config(state = DISABLED)


def equal():
	'''run restored information for two number'''

	if operation == 'plus':
		value = float(first_number) + float(input_field.get())
	elif operation == 'minus':
		value = float(first_number) - float(input_field.get())
	elif operation == 'mal':
		value = float(first_number) * float(input_field.get())
	elif operation == 'geteilt':
		if input_field.get() == '0':
			value = 'ERROR'
		else: 
			value = float(first_number) / float(input_field.get())
	elif operation == '':
		value = float(first_number) - float(input_field.get())
	elif operation == 'eins_x':
		value = float(first_number) - float(input_field.get())
	elif operation == 'hoch2':
		value = float(first_number) ** 2
	elif operation == 'xhochn':
		value = float(first_number) ** float(input_field.get())
	elif operation == 'minus':
		value = float(first_number) - float(input_field.get())

	#remove the current display and update the answer
	input_field.delete(0, END)
	input_field.insert(0, value)

	#return buttons to normal state
	enable_buttons()


def enable_buttons():
	''' enable all buttons after calculation'''
	punkt_button.config(state = NORMAL)
	minus_button.config(state = NORMAL)
	mal_button.config(state = NORMAL)
	plus_button.config(state = NORMAL)	
	geteilt_button.config(state = NORMAL)
	eins_x_button.config(state = NORMAL)
	xhochn_button.config(state = NORMAL)
	hoch2_button.config(state = NORMAL)

def clear():
	'''clear the field to start new'''
	input_field.delete(0, END)

	#return buttons to normal state 
	enable_buttons()


def inverse():
	''' calculate for the inverse of a given number'''
	#do not allow 1/0
	if input_field == '0':
		value = 'ERROR'
	else:
		value = 1/float(input_field.get())

	#remove the current display and update the answer
	input_field.delete(0, END)
	input_field.insert(0, value)

def negate():
	value = -1 * float(input_field.get())

	#remove the current display and update the answer
	input_field.delete(0, END)
	input_field.insert(0, value)


#open tkinter
root = tkinter.Tk()
root.title('Taschenrechner')
root.geometry('270x350')
root.iconbitmap(my_file_path)
root.config(bg = root_color)
root.resizable(0,0)

# set first frame
first_frame = tkinter.Frame(root, bg = root_color)
first_frame.pack( padx = 2, pady = (5,10))

#set second frame 
second_frame = tkinter.Frame(root, bg = root_color)
second_frame.pack(padx = 2, pady = 5)


# make input field
input_field = tkinter.Entry(first_frame, bg = input_button, width = 50, font = display_font, borderwidth = 3, justify = RIGHT)
input_field.pack(fill = BOTH, pady = 5, padx = 5)

# set the clear and quit button
clear_button = tkinter.Button(second_frame, bg = first_buttons, text = 'Clear', font = my_font, borderwidth = 3, command = clear)
clear_button.grid(row = 0, column = 0, pady = 1, sticky = 'WE', columnspan = 2)

quit_button = tkinter.Button(second_frame, bg = first_buttons, text = ' Quit ', font = my_font, borderwidth = 3, command = root.destroy)
quit_button.grid(row = 0, column = 2, pady = 1, sticky = 'WE', columnspan = 2, ipadx = 2)

# set all other buttons, hier funktioniert ipadx gar nicht. warum??
eins_x_button = tkinter.Button(second_frame, bg = green_button, text = '1/x', font = my_font, borderwidth = 3, command = inverse)
eins_x_button.grid(row = 1, column = 0, pady = 1,sticky = 'WE', ipadx = 0)

hoch2_button = tkinter.Button(second_frame, bg = green_button, text = ' x^2 ', font = my_font, borderwidth = 3, command = lambda:operate('hoch2'))
hoch2_button.grid(row = 1, column = 1, pady = 1,sticky = 'WE', ipadx = 0)

xhochn_button = tkinter.Button(second_frame, bg = green_button, text = ' x^n ', font = my_font, borderwidth = 3, command = lambda:operate('xhochn'))
xhochn_button.grid(row = 1 , column = 2,pady = 1,sticky = 'WE', ipadx = 0)

geteilt_button = tkinter.Button(second_frame, bg = green_button, text = ' / ', font = my_font, borderwidth = 3, command = lambda:operate('geteilt'))
geteilt_button.grid(row = 1, column = 3, pady = 1,sticky = 'WE', ipadx = 0)


#wenn ich hier nicht ipdax nehme, dann hat ganze linke reihe mehr platz und es sieht ungleich aus. warum kann man 
# nicht in row 1 machen, wieso passt sich row 1 an, wenn ich doch row 2 ändere.
sieben_button = tkinter.Button(second_frame, bg = figure_button, text = '7', font = my_font, borderwidth = 3 , command=lambda:submit_number(7))
sieben_button.grid(row = 2, column = 0, pady = 1,sticky = 'WE', ipadx = 15)
#submit_number

acht_button = tkinter.Button(second_frame, bg = figure_button, text = '8', font = my_font, borderwidth = 3 ,command=lambda:submit_number(8))
acht_button.grid(row = 2, column = 1, pady = 1,sticky = 'WE', ipadx = 15)

neun_button = tkinter.Button(second_frame, bg = figure_button, text = '9', font = my_font, borderwidth = 3, command=lambda:submit_number(9))
neun_button.grid(row = 2, column = 2, pady = 1,sticky = 'WE', ipadx = 15)

mal_button = tkinter.Button(second_frame, bg = green_button, text = '*', font = my_font, borderwidth = 3, command = lambda:operate('mal'))
mal_button.grid(row = 2, column = 3, pady = 1,sticky = 'WE', ipadx = 15)


vier_button = tkinter.Button(second_frame, bg = figure_button, text = '4', font = my_font, borderwidth = 3, command=lambda:submit_number(4))
vier_button.grid(row = 3, column = 0, pady = 1,sticky = 'WE')

fünf_button = tkinter.Button(second_frame, bg = figure_button, text = '5', font = my_font, borderwidth = 3, command=lambda:submit_number(5))
fünf_button.grid(row = 3, column = 1, pady = 1,sticky = 'WE')

sechs_button = tkinter.Button(second_frame, bg = figure_button, text = '6', font = my_font, borderwidth = 3, command=lambda:submit_number(3))
sechs_button.grid(row = 3, column = 2, pady = 1,sticky = 'WE')

minus_button = tkinter.Button(second_frame, bg = green_button, text = '-', font = my_font, borderwidth = 3, command = lambda:operate('minus'))
minus_button.grid(row = 3, column = 3, pady = 1,sticky = 'WE')


eins_button = tkinter.Button(second_frame, bg = figure_button, text = '1', font = my_font, borderwidth = 3, command=lambda:submit_number(1))
eins_button.grid(row = 4, column = 0, pady = 1,sticky = 'WE')

zwei_button = tkinter.Button(second_frame, bg = figure_button, text = '2', font = my_font, borderwidth = 3, command=lambda:submit_number(2))
zwei_button.grid(row = 4, column = 1, pady = 1,sticky = 'WE')

drei_button = tkinter.Button(second_frame, bg = figure_button, text = '3', font = my_font, borderwidth = 3, command=lambda:submit_number(3))
drei_button.grid(row = 4, column = 2, pady = 1,sticky = 'WE')

plus_button = tkinter.Button(second_frame, bg = green_button, text = '+', font = my_font, borderwidth = 3, command = lambda:operate('plus'))
plus_button.grid(row = 4, column = 3, pady = 1,sticky = 'WE')


komisch_button = tkinter.Button(second_frame, bg = figure_button, text = '-/+', font = my_font, borderwidth = 3, command = negate)
komisch_button.grid(row = 5, column = 0, pady = 1,sticky = 'WE')

null_button = tkinter.Button(second_frame, bg = figure_button, text = '0', font = my_font, borderwidth = 3, command=lambda:submit_number(0))
null_button.grid(row = 5, column = 1, pady = 1, sticky = 'WE')

punkt_button = tkinter.Button(second_frame, bg = figure_button, text = ',', font = my_font, borderwidth = 3 , command=lambda:submit_number('.'))
punkt_button.grid(row = 5, column = 2, pady = 1, sticky = 'WE')

gleich_button = tkinter.Button(second_frame, bg = green_button, text = '=', font = my_font, borderwidth = 3, command = equal)
gleich_button.grid(row = 5, column = 3, pady = 1, sticky = 'WE')





# run program 
root.mainloop()