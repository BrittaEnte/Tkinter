import tkinter, requests
from tkinter import BOTH, END, ANCHOR, RIGHT, DISABLED, NORMAL, ACTIVE
from tkinter import IntVar, StringVar, ttk, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image
import random
from io import BytesIO # damit kann man das str bild als image aufmachen 


my_file_path = r'C:\Users\ente\Desktop\gui\weather\weather.ico'


#open tkinter
root = tkinter.Tk()
root.title('weather')
root.geometry('400x400')
root.iconbitmap(my_file_path)
root.resizable(0,0)


#define fonts and colours
grass_color = '#C9F299'
large_font = ('SimSun',14)
small_font = ('SimSun', 10)
output_color = '#B8F3FF'

#define functions
def search():
	''' use open weather to look up current weather conditions'''
	global response

	# get the api response / URL and my api key 
	url = 'https://api.openweathermap.org/data/2.5/weather'
	api_key = 'd4b8fb6369b5457b2072088d170b3f19'

	# search by city name or zip code
	if search_method.get() == 1:
		querystring = {'q': city_entry.get(), 'appid': api_key, 'units': 'imperial'} # mit units imperial wird auf degree umgerechnet, die daten sind auf der api website zu finden. 
	elif search_method.get() == 2:
		querystring = {'zip': city_entry.get(), 'appid': api_key,'units': 'imperial'}

	#call api
	response = requests.request('GET', url, params = querystring)
	response = response.json()
	print(response)



	'''{'coord': {'lon': 9.7299, 'lat': 52.5471}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
	'base': 'stations', 'main': {'temp': 276.78, 'feels_like': 272.97, 'temp_min': 275.79, 'temp_max': 278.8, 'pressure': 1025, 'humidity': 67},
	'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 130}, 'clouds': {'all': 20}, 'dt': 1646473651,
 	'sys': {'type': 2, 'id': 2010660, 'country': 'DE', 'sunrise': 1646459953, 'sunset': 1646499980}, 
 	'timezone': 3600, 'id': 3221033, 'name': 'Hanover', 'cod': 200}'''

	get_weather()
	get_icon()


def get_weather():
	''' get the info from api and update our lables'''
	#gather the data from the response

	city_name = response['name']
	city_lat = str(response['sys']['country'])
	#city_lon = str(response['coord']['lon'])


	# dic weather, dann kommt ein nested dic(von id bis icon, also 0, und dann in dem neuen dict main aufrufen)
	main_weather = response['weather'][0]['main']	
	description = response['weather'][0]['description']

	temp =  str(response['main']['temp'])
	print((float(temp)-32)*5/9)
	feels_like = str(response['main']['feels_like'])
	temp_min = str(response['main']['temp_min'])
	temp_max = str(response['main']['temp_max'])
	humidity = str(response['main']['humidity'])


    #update output lables
	city_info_label.config(text=city_name +" " + city_lat, font=large_font, bg=output_color)
	weather_label.config(text="Weather: " + main_weather + ", " + description,font=small_font, bg=output_color)
	temp_label.config(text='Temperature: ' + temp + " F", font=small_font, bg=output_color)
	feels_label.config(text="Feels Like: " + feels_like + " F", font=small_font, bg=output_color)
	temp_min_label.config(text="Min Temperature: " + temp_min + " F", font=small_font, bg=output_color)
	temp_max_label.config(text="Max Temperature: " + temp_max + " F", font=small_font, bg=output_color)
	humidity_label.config(text="Humidity: " + humidity, font=small_font, bg=output_color)


def get_icon():
	''' get the icon from api response'''
	global img

	# get the icon id from the api response
	icon_id = response['weather'][0]['icon']
	

	#get the icon from the correct website
	url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

	# make a request at the url to download the icon, stream = True automatischer download
	icon_response = requests.get(url, stream = True)
	print (icon_response)

	#turn into a form tkinter/python can use, this time with response content
	img_data = icon_response.content
	
	img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
	

	#update photo label
	photo_label.config(image = img)


#build two frames 

sky_frame = tkinter.Frame(root, bg = '#05B2DC', height = 250)
sky_frame.pack(fill = BOTH, expand = True)

grass_frame = tkinter.Frame(root, bg = grass_color)
grass_frame.pack(fill = BOTH, expand = True)


output_frame = tkinter.LabelFrame(sky_frame, bg = output_color, width = 325, height = 225)
#make sure that the outputframe got always the same width and height
output_frame.pack_propagate(0)
output_frame.pack(pady = 30)


input_frame = tkinter.LabelFrame(grass_frame, bg = "#9CDE9F", width = 325)
input_frame.pack(pady = 15)


#output frame layout
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#9CDE9F

# input frame layout
city_entry = tkinter.Entry(input_frame, width = 20, font = large_font)
submit_button = tkinter.Button(input_frame, text = 'submit', font = large_font, bg ="#9CDE9F",  command = search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text = 'search by city name', variable = search_method, value = 1, font = small_font, bg = "#9CDE9F")
search_zip = tkinter.Radiobutton(input_frame, text = 'search by zip code', variable = search_method, value = 2, font = small_font, bg = "#9CDE9F")


city_entry.grid(row = 0, column = 0, padx = 10, pady = (10,0))
submit_button.grid(row = 0, column = 1, padx = 10, pady = (10,0), ipadx = 20) 
search_city.grid(row = 1, column = 0, pady = 2)
search_zip.grid(row = 1, column = 1, pady = 2, padx = (0,10))



























root.mainloop()