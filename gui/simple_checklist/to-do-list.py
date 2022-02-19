import tkinter
from tkinter import BOTH, END, ANCHOR
from tkinter import IntVar, StringVar, ttk 
from PIL import ImageTk, Image

#define fonts and colours
my_file_path = r'C:\Users\ente\Desktop\gui\umrechner\ente.ico'
my_font = ('Times New Roman', 12)
root_color = '#3066BE'

#define functions

def add_item():
	''' add item to the box'''
	my_listbox.insert(END, input_field.get())
	input_field.delete(0, END)

def delete_list():
	my_listbox.delete(0, END)

def remove_item():
	''' remove the item from the listbox'''
	# the anchor will chose the item selected with mouse click
	my_listbox.delete(ANCHOR)

def save_list():
	'''save list to a simple text file'''
	with open('checklist.txt', 'w') as f:
		#listbox.get() returns a tuple
		list_tuple = my_listbox.get(0, END)
		for item in list_tuple:
			f.write(item + "\n")

def open_list():
	''' open list if we got one'''
	try:
		with open('checklist.txt', 'r') as f:
			for line in f:  
				#item werden in der richtigen reihenfolge wieder aufgerufen
				my_listbox.insert(END, line)
	except:
		return 

#open tkinter
root = tkinter.Tk()
root.title('bunny checker')
root.geometry('400x500')
root.iconbitmap(my_file_path)
root.config(bg = root_color)


#define frame
input_frame = tkinter.Frame(root, bg = '#3066BE')
input_frame.pack(pady = 10)

output_frame = tkinter.Frame(root,bg = '#B4C5E4')
output_frame.pack()

button_frame = tkinter.Frame(root, bg = '#3066BE')
button_frame.pack(pady = 10)
 

# input frame layout
input_field = tkinter.Entry(input_frame, width = 30, font = my_font, borderwidth = 3)
input_field.grid(row = 0, column = 0, pady = 5, padx = 5)

enter_button = tkinter.Button(input_frame, bg = '#B4C5E4', width = 15, text = 'ADD', borderwidth = 3, command = add_item)
enter_button.grid(row = 0, column = 1, pady = 5, padx = 5)


# output frame layout
my_scroll_bar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, bg = '#FBFFF1',height = 15, width = 45, font = my_font, borderwidth = 3, yscrollcommand = my_scroll_bar.set)

#link listbox to scrollbar
my_scroll_bar.config(command = my_listbox.yview)
my_listbox.grid(row = 0, column = 0)
my_scroll_bar.grid(row = 0, column = 1, sticky = 'NS')


#button frame
list_remove_button = tkinter.Button(button_frame, bg = '#B4C5E4', text = 'remove item',font = my_font, borderwidth = 3, command = remove_item)
list_clear_button = tkinter.Button(button_frame, bg = '#B4C5E4', text = 'clear list', font = my_font, borderwidth = 3, command = delete_list)
save_button = tkinter.Button(button_frame, bg = '#B4C5E4', text = 'save list', font = my_font, borderwidth = 3, command = save_list)
quit_button = tkinter.Button(button_frame, bg = '#B4C5E4', text = 'quit', font = my_font, borderwidth = 3, command = root.destroy)

list_remove_button.grid(row = 0, column = 0, padx = 2, pady = 10)
list_clear_button.grid(row = 0, column = 1, padx = 2, pady = 10, ipadx = 15)
save_button.grid(row = 0, column = 2, padx = 2, pady = 10, ipadx = 15)
quit_button.grid(row = 0 , column = 3, padx = 2, pady = 10, ipadx = 20)


#open list if available
open_list()


# run program 
root.mainloop()