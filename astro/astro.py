import tkinter, requests
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL, ACTIVE
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image
import random
from io import BytesIO # damit kann man das str bild als image aufmachen 

from tkcalendar import DateEntry

my_file_path = r'C:\Users\ente\Desktop\gui\astro\rocket.ico'


#open tkinter
root = tkinter.Tk()
root.title('astro')
#hier wurde geometry nicht festgelegt, weil sich die größe immer ändert, abhängig von der textlänge
#root.geometry('600x400')
root.iconbitmap(my_file_path)


#define fonts and colors
text_fonts = ('Times New Roman',14)
nasa_blue = '#043c93'
nasa_light_blue = '#7aa5d3'
nasa_red = '#ff1923'
nasa_white = '#ffffff'

root.config(bg = nasa_blue)


#define functions
def get_request():
	''' get the request from nasa apod api'''
	global response


	#set the parameter 
	url = 'https://api.nasa.gov/planetary/apod'
	api_key =  'lQdCTudflIW504zbI1oLlYpox2mCPpKFsy4vkfYp'
	date =  calendar.get_date()
	

	querystring = {'api_key' : api_key, 'date': date}

	#call the request and turn it into a python usable format
	response = requests.request('GET', url, params = querystring)
	response = response.json()
	


	#update our labels 
	set_info()


'''
{'copyright': 'Dawid Glawdzin', 'date': '2022-03-08', 'explanation': "Which moon is this? It's Earth's moon -- but in inverted colors.' 
'Here, the pixel values corresponding to light and dark areas have been translated in reverse, or inverted, producing a false-color representation reminiscent of a black and white photographic negative. 
 However, this is an inverted color image -- where the muted colors of the moon are real but digitally exaggerated before inversion. 
  Normally bright rays from the large crater Tycho dominate the southern (bottom) features as easily followed dark green lines emanating from the 85-kilometer diameter impact site.
' Normally dark lunar mare appear light and silvery.  The image was acquired in Southend-on-Sea, England, UK. 
 Historically, astronomical images recorded on photographic plates were directly examined on inverted-color negatives because it helped the eye pick out faint details.",
 'hdurl': 'https://apod.nasa.gov/apod/image/2203/InvertedMoon_Glawdzin_2048.jpg', 
'media_type': 'image', 'service_version': 'v1', 'title': 'Moon in Inverted Colors', 'url': 'https://apod.nasa.gov/apod/image/2203/InvertedMoon_Glawdzin_960.jpg'}
'''

def set_info():
	'''update output label'''

	#update the picture date and explanation
	picture_date.config(text = response['date'])
	picture_explanation.config(text = response['explanation'])


	#we need three images in other functions. an img, a thumb, and a full img
	global img, thumb
	global full_img

	#grab the photo that is stored in our response
	url = response['url']
	img_response = requests.get(url, stream = True)

	# get the content of the response and use BytesIO to open it as an image.
	# keep a reference to this img as this is what we can use to save the image (image not the photoimage)
	# create the full screen image for a second window

	img_data = img_response.content	# wenn ich das habe, ist es nur ein crazy string. also umwandeln mit BytesIO
	img = Image.open(BytesIO(img_data))
	#jetzt kommt das grosse bild, dass ich ggf auch speichern will 
	full_img = ImageTk.PhotoImage(img)

	#create thumbnail for the main screen
	thumb_data = img_response.content
	thumb = Image.open(BytesIO(thumb_data))
	thumb.thumbnail((200,200)) # this must be a tuple!
	thumb = ImageTk.PhotoImage(thumb)

	#set the thumbnail image
	picture_label.config(image = thumb)


#create frames

input_frame = tkinter.Frame(root, bg = nasa_blue)
input_frame.pack()

output_frame = tkinter.Frame(root, bg = nasa_white)
output_frame.pack(padx = 50, pady = (0,25))



#layout for the input frame
calendar = DateEntry(input_frame, width = 10, font = text_fonts, background = nasa_blue, foreground = nasa_white) # bg muss bei calendar ausgeschrieben werden 
calendar.grid(row = 0, column = 0, padx = 5, pady = 10)

submit_button = tkinter.Button(input_frame, text = 'submit', font = text_fonts, bg = nasa_light_blue, command = get_request)
submit_button.grid(row = 0, column = 1, padx = 5, pady = 10)


full_button = tkinter.Button(input_frame, text = 'full photo', font = text_fonts, bg = nasa_light_blue)
full_button.grid(row = 0, column = 2, padx = 5, pady = 10)


save_button = tkinter.Button(input_frame, text = 'save photo', font = text_fonts, bg = nasa_light_blue)
save_button.grid(row = 0, column = 3, padx = 5, pady = 10)

quit_button = tkinter.Button(input_frame, text = 'EXIT', font = text_fonts, bg = nasa_red, command = root.destroy)
quit_button.grid(row = 0, column = 4, padx = 5, pady = 10)


#layout for the output frame

picture_date = tkinter.Label(output_frame, text = 'testing', font = text_fonts, bg = nasa_white)
picture_explanation = tkinter.Label(output_frame, text = 'testing', font = text_fonts, bg = nasa_white, wraplength = 600)
picture_label = tkinter.Label(output_frame, text = 'testing')

picture_date.grid(row = 0, column = 0)
picture_explanation.grid(row = 1, column = 0)
picture_label.grid(row = 1, column = 1)
























#run the program
root.mainloop()