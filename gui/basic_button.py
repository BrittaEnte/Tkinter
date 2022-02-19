import tkinter

# define window

root = tkinter.Tk()
#set title
root.title('ente gut, alles gut')

#set icon, geht nur mit ico dateien
root.iconbitmap('ente.ico')

root.geometry('500x500')
root.resizable(0,0)

#define a button 
name_button = tkinter.Button(root, text = 'name')
name_button.grid(row = 0, column = 0)
time_button = tkinter.Button(root, text = 'time')
time_button.grid(row = 0, column = 1)

place_button = tkinter.Button(root, text = 'place', bg = 'yellow', activebackground = 'green')
place_button.grid(row = 0, column = 2, pady = 10 ,  padx = 10, ipadx = 15)

date_button = tkinter.Button(root, text = 'date', bg = 'yellow', activebackground = 'green', borderwidth = 5)
date_button.grid(row = 1, column = 0, columnspan = 3 , sticky = 'WE' ,pady = 10 ,  padx = 10, ipadx = 15)

test_1 = tkinter.Button(root, text = 'test')
test_2 = tkinter.Button(root, text = 'test')
test_3 = tkinter.Button(root, text = 'test')
test_4 = tkinter.Button(root, text = 'test')
test_5 = tkinter.Button(root, text = 'test')
test_6 = tkinter.Button(root, text = 'test')

test_1.grid(row = 2, column = 0, pady = 5, padx = 5)
test_2.grid(row = 2, column = 1, pady = 5, padx = 5)
test_3.grid(row = 2, column = 2, pady = 5, padx = 5, sticky = 'W')
test_4.grid(row = 3, column = 0, pady = 5, padx = 5)
test_5.grid(row = 3, column = 1, pady = 5, padx = 5)
test_6.grid(row = 3, column = 2, pady = 5, padx = 5, sticky = 'W')




#run root window
root.mainloop()