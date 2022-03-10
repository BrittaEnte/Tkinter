import tkinter, requests, webbrowser
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL, ACTIVE
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image
import random
import datetime
from io import BytesIO # damit kann man das str bild als image aufmachen 

from tkcalendar import DateEntry

my_file_path = r'C:\Users\ente\Desktop\gui\laufrechner\laufrechner.ico'


#define color
blau = '#9197AE'
heller = '#C0C7CE'
hell = '#EFF6EE'
font = ('Arial', 12)
überschrift = ('Arial', 15)


#open tkinter
root = tkinter.Tk()
root.title('Laufrechner')
root.geometry('400x400')
root.iconbitmap(my_file_path)
root.config(bg = blau)


#define all functions
def delete():
	lauftrecke_eingabe.delete(0, END)
	laufzeit_eingabe.delete(0, END)
	zeit_eingabe.delete(0, END)
	geschwindigkeit_eingabe.delete(0, END)


def umrechnen():	
	
	if geschwindigkeit_eingabe.get():		
		zeit = 60/ float(geschwindigkeit_eingabe.get()) 
		print(zeit)
		# https://stackoverflow.com/questions/27496889/converting-a-float-to-hhmm-format
		zeit = str(datetime.timedelta(hours = zeit))[:-3]
		zeit_eingabe.insert(0, zeit)	


		# diese nested if muss rein, weil er sonst die lautzeit nicht berechnet, sondern nur auf die erst if clause zugreift. 
		if lauftrecke_eingabe.get() and geschwindigkeit_eingabe.get():
			laufzeit = float(lauftrecke_eingabe.get()) / float(geschwindigkeit_eingabe.get())
			laufzeit = str(datetime.timedelta(hours = laufzeit))[:-3]
			laufzeit_eingabe.insert(0, laufzeit) 

	
	elif lauftrecke_eingabe.get() and laufzeit_eingabe.get():		
		zeit = float(laufzeit_eingabe.get())/ float(lauftrecke_eingabe.get())
		zeit = round(zeit, 2)
		zeit_eingabe.insert(0, zeit)
		geschwindigkeit = 60 / zeit
		geschwindigkeit = round(geschwindigkeit, 2)
		geschwindigkeit_eingabe.insert(0, geschwindigkeit)



#überschrift
überschrift = tkinter.Label(root, bg = heller, text = 'Laufrechner (englische Schreibweise)', font = font)
überschrift.pack(ipadx = 300, ipady = 10)


#mittelframe
mitte = tkinter.Label(root, bg = blau)
mitte.pack()


# 4 textfelder und 4 bescheibungen
laufstrecke = tkinter.Label(mitte, text = 'Laufstrecke [km]', font = font, bg = blau)
lauftrecke_eingabe = tkinter.Entry(mitte, font = font, bg = blau)
laufstrecke.grid(row = 0, column = 0)
lauftrecke_eingabe.grid(row = 0, column = 1, pady = 20)


laufzeit = tkinter.Label(mitte, text = 'Laufzeit in min', font = font, bg = blau)
laufzeit_eingabe = tkinter.Entry(mitte, font = font, bg = blau)
laufzeit.grid(row = 2, column = 0)
laufzeit_eingabe.grid(row = 2, column = 1, pady = 20)


zeit = tkinter.Label(mitte, text = 'Zeit/Km [min:sec]', font = font, bg = blau)
zeit_eingabe = tkinter.Entry(mitte, font = font, bg = blau)
zeit.grid(row = 3, column = 0)
zeit_eingabe.grid(row = 3, column = 1, pady = 20)


geschwindigkeit = tkinter.Label(mitte, text = 'Geschwindigkeit [km/h]', font = font, bg = blau)
geschwindigkeit_eingabe = tkinter.Entry(mitte, font = font, bg = blau)
geschwindigkeit.grid(row = 4, column = 0)
geschwindigkeit_eingabe.grid(row = 4, column = 1, pady = 20)




#untere reihe mit zwei buttons
unten = tkinter.Label(root, bg = heller)
unten.pack(ipadx = 300, ipady = 5)

umrechnen = tkinter.Button(unten, text = 'Umrechnen', command = umrechnen)
umrechnen.grid(row = 0, column = 0, columnspan = 2, padx = 60, ipadx = 20, pady = (20,0))

löschen = tkinter.Button(unten, text ='Löschen', command = delete)
löschen.grid(row = 0, column = 3, columnspan = 2, ipadx = 30, pady = (20,0) )
























root.mainloop()