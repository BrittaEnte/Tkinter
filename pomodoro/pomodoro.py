import tkinter, requests, webbrowser, time 
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL, ACTIVE, HORIZONTAL, CURRENT
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image
import random
import datetime
from io import BytesIO # damit kann man das str bild als image aufmachen 

from tkcalendar import DateEntry

my_file_path = r'C:\Users\ente\Desktop\gui\pomodoro\tomato.ico'



#define fonts and colours
# use the 60-20-10 rule 
'''It's a classic decor rule that helps create a color palette for a space. It states that 60% of the room should be a dominant color,
 30% should be the secondary color or texture and the last 10% should be an accent. 
 https://www.saralynnbrennan.com/blog/the-60-30-10-design-rule#:~:text=It%27s%20a%20classic%20decor%20rule,10%25%20should%20be%20an%20accent.'''
haupt_farbe = '#EFF6EE'
zwanzig_farbe = '#9197AE'
zehn_farbe = '#273043'

#set the root 
root = tkinter.Tk()
root.title('Zeit')
root.geometry('200x200')
root.iconbitmap(my_file_path)
root.resizable(0,0)
root.config(bg = haupt_farbe)






#declare the variable
#string var is used to edit a widget text field
#https://stackoverflow.com/questions/51783852/what-is-the-difference-between-a-variable-and-stringvar-of-tkinter
hour = StringVar()
minute = StringVar()
second = StringVar()

# setting all the values to 0, when the app is opened
hour.set('00')
minute.set('00')
second.set('00')




#define functions
#https://www.geeksforgeeks.org/divmod-python-application/

def submit():

    zeit = int(hour.get()) *3600 + int(minute.get())*60 + int(second.get())


    while zeit > -0.01:

        #calculate the minutes and seconds with divmod. the first figure is the nominator and the second figure is the denominator. 
        #example divmod(8,3) is (2,2) 2*3 are six and 2 are left

        mins, secs = divmod(zeit,60)

        hours = 0

        if mins > 60: # then we got more than one hour!
            hours, mins = divmod(mins,60)

        #now we must format the figures to the 2nd decimal place
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))


        #now the system shall update the new given figures
        root.update()
        # with one second delay each time
        time.sleep(1)


        #zeit must be 1 second go
        zeit -= 1


        if zeit == 0:
            messagebox.showinfo('fertig', "du hast es geschafft")





hourEntry = tkinter.Entry(root, width = 3, font = ('Arial', 20), textvariable = hour)
minuteEntry = tkinter.Entry(root,width = 3, font = ('Arial', 20), textvariable = minute)
secondEntry = tkinter.Entry(root, width = 3, font = ('Arial', 20),textvariable = second)
hourEntry.grid(row = 0, column = 0, pady = 10, padx = (30,0))
minuteEntry.grid(row = 0, column = 1)
secondEntry.grid(row = 0, column = 2)


# bd = ist so ne art schatten in 3d 
submit_button = tkinter.Button(root, text = 'submit', bd = '5', command = submit)
submit_button.grid(row = 1, column = 1, sticky ='WE')







root.mainloop()