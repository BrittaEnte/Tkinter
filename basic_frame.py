import tkinter
from tkinter import BOTH

#define window

root = tkinter.Tk()
root.title('frame')

#set icon, geht nur mit ico dateien
root.iconbitmap('ente.ico')

root.geometry('500x500')
root.resizable(0,0)

# you can not use pack and grid together. 

#define frames
pack_frame = tkinter.Frame(root, bg = 'green')
grid_frame = tkinter.Frame(root, bg = 'blue')
grid_frame1 = tkinter.LabelFrame(root, bg = 'yellow', text = 'the grid rules the world')

# pack frames onto root
pack_frame.pack(fill = BOTH, expand = True)
grid_frame.pack(fill = 'x', expand = True)
grid_frame1.pack(fill = BOTH, expand = True, pady = 5, padx = 5)

# pack frame
tkinter.Label(pack_frame,text = 'test').pack()
tkinter.Label(pack_frame,text = 'test').pack()
tkinter.Label(pack_frame,text = 'test').pack()

# grid frame
tkinter.Label(grid_frame,text = 'test').grid(row = 0, column = 0)
tkinter.Label(grid_frame,text = 'test').grid(row = 1, column = 1)
tkinter.Label(grid_frame,text = 'test').grid(row = 2, column = 2)


#grid1frame 
tkinter.Label(grid_frame1,text = 'testaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row = 0, column = 0)

root.mainloop()