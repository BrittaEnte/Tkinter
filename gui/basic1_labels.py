# labels and pack

import tkinter

#define window

root = tkinter.Tk()

root.title('basic')
root.iconbitmap('ente.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg = 'orange')

#create widgets
label1 = tkinter.Label(root, text = 'test')
label2 = tkinter.Label(root, text ='dies ist die zweite zeile', font = ('Arial', 20, 'bold'))
label3 = tkinter.Label(root, text = 'dies ist die dritte zeile', font =('Cambria', 15, 'bold'), bg = 'blue')
label4 = tkinter.Label(root, text = 'dies ist die 4te zeile', font =('Cambria', 15, 'bold'), fg = 'blue', bg = 'yellow')
label5 = tkinter.Label(root, text = 'dies ist die 5te zeile', font =('Cambria', 12, 'bold'), fg = 'blue', bg = 'green')
#place the window
label1.pack()
label2.pack()
label3.pack(padx = 100, pady = 15)
#pady mit 0 on the top and 10 on the bottom 
#ipadx = interner margin
#anchor = n, w, e and s
label4.pack(pady = (0,10) ,ipadx = 100, ipady = 20, anchor = 'w')
# fill y only fill till the characters, you need to expand 
label5.pack(fill = 'both', expand = True, padx = 10, pady = 10)


root.mainloop()