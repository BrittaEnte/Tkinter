import tkinter
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image


my_file_path = r'C:\Users\ente\Desktop\gui\notepad\notepad.ico'


#open tkinter
root = tkinter.Tk()
root.title('Notepad')
root.geometry('600x600')
root.iconbitmap(my_file_path)
#root.config(bg = root_color)
root.resizable(0,0)


#define fonts and colors
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'
root.config(bg = root_color)


# define functions

def save_note():
	''' save note, für die geschichtsschreibung'''
	# use fielddialog to geht location
	save_name = filedialog.asksaveasfilename(initialdir = './', title = 'save note', filetypes =(('Text Files', '*.txt'), ('All Files', '*.*')))
	with open(save_name, 'w') as f:
		#irst three lines save file font family, font options and size. size must be a string and not an int.
		f.write(font_family.get() + "\n") # hier "" nehmen und nicht ''
		f.write(str(größe_int.get()) + "\n")
		f.write(style_family.get() + "\n")

		#write now the text
		f.write(input_text.get('1.0', END))



def change_font(event): # wenn hier nicht event steht, dann kommt die fehlermeldung, one argument(zb die größe) was given, but 0 was requested
	#that is always the case with dropboxes 
	''' change the given font to the dropbox actions'''

	if style_family.get() == 'none':
		my_font = (font_family.get(), größe_int.get())
	else:
		my_font = (font_family.get(), größe_int.get(), style_family.get())

	#change the font style
	input_text.config(font = my_font)	


def new_note():
	''' creat a new Note if requested'''
	question = messagebox.askyesno('new note, really?')
	if question == 1:
		#hier auf 1.0 achten, bei text ist es so 
		input_text.delete('1.0', END)


def close_file():
	''' create a save question '''
	question = messagebox.askyesno('you wann close, really?')
	if question == 1:
		root.destroy()


def open_note():
	''' open file. first three lines are font, size and style'''
	open_name = filedialog.askopenfilename(initialdir = './', title = 'open note', filetypes =(('Text Files', '*.txt'), ('All Files', '*.*')))
	with open(open_name, 'r') as f:
		# clear the curent text??
		input_text.delete('1.0', END)

		#first three lines are style, family and size
		# readline will read the line and then stop. with the next calling it will read the next line and so on
		font_family.set(f.readline().strip())
		größe_int.set(int(f.readline().strip()))
		style_family.set(f.readline().strip())

		# call the change font for these .set() and pass an arbitary value. siehe auch change_font(event) docu
		change_font(1)

		# read the rest of the file and insert it to the text field
		text = f.read()
		input_text.insert('1.0', text)



#define lists for comboboxes
style = ['bold', 'italic', 'normal']
style_family = StringVar()
größe = [10,11,12,13,14,15]
größe_int = IntVar()
families = ['Calibri', 'Arial', 'Times New Roman']
font_family = StringVar()



#load all the images
photo1= tkinter.PhotoImage(file = r'C:\Users\ente\Desktop\gui\notepad\new.png')
photo2= tkinter.PhotoImage(file = r'C:\Users\ente\Desktop\gui\notepad\close.png')
photo3= tkinter.PhotoImage(file = r'C:\Users\ente\Desktop\gui\notepad\open.png')
photo4= tkinter.PhotoImage(file = r'C:\Users\ente\Desktop\gui\notepad\save.png')


#define layout
#define frame

menu_frame = tkinter.Frame(root, bg = menu_color)
menu_frame.pack(pady = 5, padx = 5)
text_frame = tkinter.Frame(root, bg = text_color)
text_frame.pack(pady = 5, padx = 5)


#define buttons in menu frame
new_button = tkinter.Button(menu_frame,image = photo1, command = new_note ).grid( row = 0, column = 0, pady = 15, padx = 3)
open_button = tkinter.Button(menu_frame, image = photo3, command = open_note).grid(row = 0, column = 1,pady = 15, padx = 3)
save_button = tkinter.Button(menu_frame, image = photo4, command = save_note).grid(row = 0, column = 2,pady = 15, padx = 3)
delete_button = tkinter.Button(menu_frame, image= photo2, command = close_file).grid(row = 0, column = 3,pady = 15, padx = 3)



#font family
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command = change_font)
font_family_drop.grid(row = 0, column = 4,pady = 10, padx = 3)
font_family.set('Arial')
font_family_drop.config(width = 16) 


#schriftgröße
schriftgröße = tkinter.OptionMenu(menu_frame, größe_int, *größe, command = change_font)
größe_int.set(10)
schriftgröße.grid(row = 0, column = 5,pady = 15, padx = 3)

# style
style_button = tkinter.OptionMenu(menu_frame, style_family, *style, command = change_font)
style_family.set('bold')
style_button.config(width = 12)
style_button.grid(row = 0, column = 6, pady = 15, padx = 3)


#set font for the text_frame
my_font = (font_family.get(), größe_int.get())



# define text _frame 
input_text = tkinter.scrolledtext.ScrolledText(text_frame, bg = text_color, font = my_font, width = 1000, height = 100)
#hier unbedingt pack nehmen und nicht grid, ansonsten passt es nicht mit der width
input_text.pack()


















# run program 
root.mainloop()