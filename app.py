from tkinter import *
from PIL import ImageTk, Image
import requests
import json
window = Tk()
window.title('Weather App')
window.geometry("800x800")
window.resizable(0,0)
heading=Label(window,text="Weather Forecasting App",font="arial 20 bold",bg="black",fg="lightblue").pack(pady="10")
image=Image.open("img.png")
img=image.resize((200,150))
photo=ImageTk.PhotoImage(img)
image_label=Label(window,image=photo).pack(pady="10")
climate_1 = Label(window, text="", font="arial 16 bold")
climate_1.place(x=500, y=500)

description_1 = Label(window, text="", font="arial 16 bold")
description_1.place(x=500, y=530)

temperature_1 = Label(window, text="", font="arial 16 bold")
temperature_1.place(x=500, y=560)

pressure_1 = Label(window, text="", font="arial 16 bold")
pressure_1.place(x=500, y=590)
city_input=StringVar()
def display_weather():
    api_key = "e0d91f9cbf1e3b4a51dc8dd7f31e57a1"
    city_name=city_input.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    kelvin=273.15
    climate_1.config(text=weather_info["weather"][0]["main"])
    description_1.config(text=weather_info["weather"][0]["description"])
    temperature_1.config(text=str(int(weather_info["main"]["temp"]-kelvin)))
    pressure_1.config(text=weather_info["main"]["pressure"])
input=Entry(window,textvariable=city_input,font="arial 20 italic",bg="black",fg="lightblue").pack(pady="30")
climate=Label(window,text="Weather Climate",font="arial 16 bold").place(x=150,y=500)
description=Label(window,text="Weather Description",font="arial 16 bold").place(x=150,y=530)
temperature=Label(window,text="Temperature",font="arial 16 bold").place(x=150,y=560)
pressure=Label(window,text="Pressure",font="arial 16 bold").place(x=150,y=590)
button=Button(window,text="Check Weather",command=display_weather,bg="lightblue",fg="black",font="arial 20 bold").place(x=280,y=350)
window.mainloop()