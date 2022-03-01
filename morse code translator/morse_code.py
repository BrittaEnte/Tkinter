import tkinter
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image
from playsound import playsound

my_file_path = r'C:\Users\ente\Desktop\gui\morse code translator\morse.ico'
dot = r'C:\Users\ente\Desktop\gui\morse code translator\dot.mp3'
dash = r'C:\Users\ente\Desktop\gui\morse code translator\dash.mp3'



#open tkinter
root = tkinter.Tk()
root.title('morse code')
root.geometry('500x350')
root.iconbitmap(my_file_path)
#root.config(bg = root_color)
root.resizable(0,0)


#define font colors
button_font = ('Arial', 10)
root_color = '#778899'
frame_color = '#dcdcdc'
button_color = '#c0c0c0'
text_color = '#f8f8ff'
root.config(bg = root_color)


#define funtions

def convert():

	''' convert from english to morse'''
	if language.get() == 1:
		get_morse()

	elif language.get() ==2:
		get_english()



def get_morse():
	''' convert from english to morse'''
	morse_code = ''

	#get the input text and make it lower case
	text = input_text.get("1.0", END)
	text = text.lower()

	#remove any letters or symbols that are not in dict
	for letter in text: 
		if letter not in english_to_morse.keys():
			text = text.replace(letter, ' ')

	#break up words into a list based on space
	word_list = text.split()


	#turn each word into a list of letters
	for word in word_list:
		letters = list(word)
		
		for letter in letters:
			morse_char = english_to_morse[letter]
			morse_code = morse_code + morse_char + " "
		#seperate individual wordswith a |
		morse_code += "|"
		

	output_text.insert('1.0', morse_code)


def get_english():
	''' convert morse code to english'''
	#string to hold the message
	english = ""

	#get the input text
	text = input_text.get("1.0", END)

	#remove any lettters or symbols not in dict
	for letter in text: 
		if letter not in morse_to_english.keys():
			text = text.replace(letter, ' ')

	#break up words into a list based on | and put into a list
	word_list = text.split("|")

	#turn each word into a list of letters
	for word in word_list:
		letters = word.split(" ")
		
		# for each letter get the english char
		
		for letter in letters:
			english_char = morse_to_english[letter]
			english +=  english_char
		#print(word_code)
		#seperate individual wordswith a |
		english += " "
		

	output_text.insert('1.0', english)


def clear():
	''' clear al text fields'''
	input_text.delete('1.0', END)
	output_text.delete('1.0', END)


def play():
	''' play morse code'''
	# where is the morse code?

	if language.get() == 1:
		text = output_text.get('1.0', END)
	elif language.get() == 2:
		text = input_text.get('1.0', END)	
		
	#play the tones
	for value in text:
		if value == '.':
			playsound(dot)
			root.after(100) # delay after sound
		elif value == '-':			
			playsound(dash)
			root.after(200)
		elif value == ' ':
			root.after(300)
		elif value == '|':
			root.after(700)



def show_guide():
	''' show a morse code guide in another window'''
	#image morse  and window guid needs to be a global variable 
	global morse
	global guide

	#create a second window
	guide = tkinter.Toplevel()
	guide.title('morse code')
	guide.iconbitmap(my_file_path)
	guide.geometry('350x350+' + str(root.winfo_x() + 500) + '+' + str(root.winfo_y()))
	guide.config(bg = root_color)


	#create the image, label, and pack
	morse = ImageTk.PhotoImage(Image.open(r'C:\Users\ente\Desktop\gui\morse code translator\morse_chart.JPG'))
	label = tkinter.Label(guide, image = morse, bg = frame_color)
	label.pack(padx = 10, pady = 10, ipadx = 5, ipady = 5)

	# create a close button
	close_button = tkinter.Button(guide, text ='close', font = button_font, bg = button_color, command = high_guide)
	close_button.pack(padx = 10, ipadx = 50)

	#disable the guide button
	guide_button.config(state = DISABLED)


def high_guide():
	''' hide the guide'''
	guide_button.config(state = NORMAL)
	guide.destroy()


#define dic

english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
 'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
 'y': '-.--', 'z': '--..', '1': '.----',
 '2': '..---', '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..', '9': '----.',
 '0': '-----', ' ':' ', '|':'|', "":"" }


morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])


#layout for the input_frame
input_frame = tkinter.LabelFrame(root, bg = frame_color)
output_frame = tkinter.LabelFrame(root, bg = frame_color)
input_frame.pack(padx = 16, pady = (16,8))
output_frame.pack(padx = 16, pady = (8,16))



input_text = tkinter.Text(input_frame, height = 8, width = 30, bg = text_color)
input_text.grid( row = 0, column = 1, rowspan = 3, padx = 5, pady = 5)


language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text = 'english to morse', variable = language, value = 1, font= button_font, bg = frame_color)
englisch_button = tkinter.Radiobutton(input_frame, text = 'morse to english', variable = language, value = 2, font= button_font, bg = frame_color)
guide_button = tkinter.Button(input_frame, text = 'Guide', font = button_font, bg = button_color, command = show_guide)

morse_button.grid(row = 0, column = 0, pady = (15,0))
englisch_button.grid(row = 1, column = 0)
guide_button.grid(row = 2, column = 0,sticky = 'WE', padx = 10, ipadx = 53)


#layout for the output_frame 
output_text = tkinter.Text(output_frame, height = 8, width = 30, bg = text_color)
output_text.grid( row = 0, column = 1, rowspan = 4, padx = 5, pady = 5)

convert_button = tkinter.Button(output_frame, text = 'convert', font = button_font, bg = button_color, command = convert)
play_button = tkinter.Button(output_frame, text = 'play', font = button_font, bg = button_color, command = play)
clear_button = tkinter.Button(output_frame, text = 'clear', font = button_font, bg = button_color, command = clear)
quit_button = tkinter.Button(output_frame, text = 'quit', font = button_font, bg = button_color, command = root.destroy)

convert_button.grid(row = 0, column = 0, padx = 10, ipadx = 50) # convert ipadx defines column width, for all columns underneath
play_button.grid(row = 1, column = 0, padx = 10, sticky = 'WE')
clear_button.grid(row = 2, column = 0, padx = 10,  sticky = 'WE')
quit_button.grid(row = 3, column = 0, padx = 10, sticky = 'WE')





#run the program
root.mainloop()