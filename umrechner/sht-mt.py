import tkinter
from tkinter import BOTH, END
from tkinter import IntVar, StringVar, ttk 
from PIL import ImageTk, Image


my_file_path = r'C:\Users\ente\Desktop\gui\umrechner\ente.ico'
root = tkinter.Tk()
root.title('convert')
root.geometry('400x300')
root.iconbitmap(my_file_path)
root.config(bg = '#546A76')


# define functions
'''def convert():
	convert as requested
	metric_values = {
	'short tons ' : 10**12, 
	'metric tons' : 2000
	}
	# get all user information
	start_value = float(input_field.get())
	print(start_value)
	start_prefix = input_combobox.get()
	print(start_prefix)
	end_prefix = output_combobox.get()

'''

def convert():

	#clear the outputfield:
	output_field.delete(0, END)


	start = float(input_field.get())
	print(start)
	prefix = input_combobox.get()
	print(prefix)
	# convert all the stuff 
	if prefix == 'short tons': 
		x = start * 0.907185
	else:
		x = start / 0.907185

	print(x) 

	#update output field
	output_field.insert(0, str(x))






# create the input and output fields
input_field = tkinter.Entry(root, width = 20)
output_field = tkinter.Entry(root, width =20)
equal_label = tkinter.Label(root, text = '=')

input_field.grid( row = 0, column = 0, pady = 20, padx = 30)
output_field.grid( row = 0, column = 2, padx = 30)
equal_label.grid( row = 0, column = 1)

input_field.insert(0, 'enter your quantity')

# create the dropdown
metric_list = ['short tons', 'metric tons']
input_combobox = ttk.Combobox(root, value = metric_list, justify = 'center')
input_combobox.grid( row = 1, column = 0)
input_combobox.set('base value')

output_combobox = ttk.Combobox(root, value = metric_list, justify = 'center')
output_combobox.grid( row = 1, column = 2)
output_combobox.set('result value')


input_choice = StringVar()
output_choice = StringVar()

'''
input_dropdown = tkinter.OptionMenu(root, input_choice, *metric_list)
output_dropdown = tkinter.OptionMenu(root, output_choice, *metric_list)

#set base value
input_choice.set('base value')
output_choice.set('base value')


input_dropdown.grid(row = 1, column = 0)
output_dropdown.grid(row = 1, column = 2)

'''
to_label = tkinter.Label(root, text = 'to')
to_label.grid(row = 1, column =1)

#make the convert button
convert_button = tkinter.Button(root, text ='convert', command = convert)
convert_button.grid(row = 4, column = 0, columnspan = 3, pady = 20, ipadx = 20)



















root.mainloop()