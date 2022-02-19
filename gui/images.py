import tkinter
from tkinter import BOTH
from PIL import ImageTk, Image


root = tkinter.Tk()
root.title('radiobutton')
root.geometry('800x800')
root.iconbitmap('ente.ico')

#works for png 
my_image = tkinter.PhotoImage(file = 'duck1.png')
my_label = tkinter.Label(root, image = my_image)
my_label.pack()


my_button = tkinter.Button(root, image = my_image)
my_button.pack()


# works not for jpeg
# pip install pillow !!!
# using PIL for jpg
img = ImageTk.PhotoImage(Image.open('1.jpg'))
img_label = tkinter.Label(root, image = img, bg = 'orange')
img_label.pack(fill = BOTH)







root.mainloop()