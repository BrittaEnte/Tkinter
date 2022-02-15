import tkinter

# define window

root = tkinter.Tk()
#set title
root.title('ente gut, alles gut')

#set icon, geht nur mit ico dateien
root.iconbitmap('ente.ico')

#größe setzen. width * height
root.geometry('250x700')

# jetzt kann man width nicht ändern, height schon 
root.resizable(0,1)

#hintergrundfarbe setzen
root.config(bg = 'green')


# set second window
top = tkinter.Toplevel()
top.title('neue ente')
top.iconbitmap('ente.ico')
top.config(bg = 'blue')
# das zweite window ganz nach oben setzen, + 50 y achse und 50 x achse
top.geometry('200x500+50+50')






#run root window
root.mainloop()
