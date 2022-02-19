import tkinter
from tkinter import BOTH
from tkinter import END


def p():
	text = tkinter.Label(frame2, text = text1.get())
	text.pack()
	text1.delete(0, END)

def count(number):
	global value
	text = tkinter.Label(frame1, text = number, bg = 'orange')	
	value = number + 1
	text.pack()

#main window
root = tkinter.Tk()
root.title('spiel 1')
root.iconbitmap('ente.ico')
root.geometry('400x400')

# define frames
frame1 = tkinter.Frame(root, bg = 'orange')
frame2 = tkinter.Frame(root, bg = 'green')


# pack frame 
#frame1.grid(row = 0, column = 0)
#frame2.grid(row = 1, column = 1)

frame1.pack(fill = BOTH, side = 'right', expand = True)
frame2.pack(fill = BOTH, side = 'left', expand = True)


#make print button 
text1 = tkinter.Entry(frame2, width = 15)
text1.pack()

#propapate
frame1.pack_propagate(0)
frame2.pack_propagate(0)

#produce print button
button = tkinter.Button(frame1, command = p, text = 'print')
button.pack()

#produce count button 
value = 0
button_count = tkinter.Button(frame1, text = 'count', command = lambda:(count(value)))
button_count.pack()


#run window 
root.mainloop()