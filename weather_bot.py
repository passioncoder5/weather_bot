from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import speech_recognition as sr
import pyttsx3
from ttkbootstrap import Style

window = Tk()
window.title('Weather Bot')
window.geometry("800x800")
window.resizable(0, 0)



style = Style(theme="superhero")  # Apply ttkbootstrap style

heading = Label(window,text="Weather Forecasting App",font=("Arial", 20, "bold"),bg=style.colors.primary,fg=style.colors.light)
heading.pack(pady=10)

image = Image.open("img.jpg")
img = image.resize((150, 150))
photo = ImageTk.PhotoImage(img)
image_label = Label(window, image=photo)
image_label.pack(pady=10)

climate_1 = Label(window, text="", font=("Arial", 16, "bold"))
climate_1.place(x=500, y=500)

description_1 = Label(window, text="", font=("Arial", 16, "bold"))
description_1.place(x=500, y=545)

temperature_1 = Label(window, text="", font=("Arial", 16, "bold"))
temperature_1.place(x=500, y=590)

pressure_1 = Label(window, text="", font=("Arial", 16, "bold"))
pressure_1.place(x=500, y=635)

city_input = StringVar()

r = sr.Recognizer()
engine = pyttsx3.init()


def run_voice():
    r.pause_threshold = 1.2
    r.energy_threshold = 12000

    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5)
        try:
            message = r.recognize_google(audio)
            print(message)
            input.delete(0, END)
            input.insert(0, message)
        except sr.UnknownValueError:
            print("Could not recognize")
            input.delete(0, END)
            input.insert(0, "Not found")
        else:
            pass


icon = Image.open("mic.jpg").resize((30, 30))
micicon = ImageTk.PhotoImage(icon)
mic_button = Button(
    window,
    image=micicon,
    command=run_voice,
    overrelief="groove",
    relief="sunken",
)
mic_button.place(x=552, y=262)

def display_weather():
    api_key = "e0d91f9cbf1e3b4a51dc8dd7f31e57a1"
    city_name = city_input.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    kelvin = 273.15
    climate_1.config(text=weather_info["weather"][0]["main"])
    description_1.config(text=weather_info["weather"][0]["description"])
    temperature_1.config(text=str(int(weather_info["main"]["temp"] - kelvin)))
    pressure_1.config(text=weather_info["main"]["pressure"])
    engine.say(f"The weather in {city_name} is {weather_info['weather'][0]['main']}")
    engine.say(f"The description of the weather is {weather_info['weather'][0]['description']}")
    engine.say(f"The temperature is {str(int(weather_info['main']['temp'] - kelvin))} degrees Celsius")
    engine.say(f"The pressure is {weather_info['main']['pressure']} hPascal")

    # Set background GIF based on weather condition
    weather_condition = weather_info["weather"][0]["main"].lower()
    if weather_condition == "clouds":
        background_image = "clouds.gif"
    elif weather_condition == "drizzle":
        background_image = "drizzle.gif"
    elif weather_condition == "thunderstorm":
        background_image = "thunderstorm.gif"
    elif weather_condition == "rain":
        background_image = "rain.gif"
    elif weather_condition == "snow":
        background_image = "snow.gif"
    elif weather_condition == "atmosphere":
        background_image = "atmosphere.gif"
    elif weather_condition == "clear":
        background_image = "clear.gif"
    else:
        background_image = "default.gif"  # Use a default GIF if the condition is unknown
        # Create a label for the background GIF
    background_label = Label(window)
    background_label.place(x=0, y=0)

    # Function to update the background GIF
    def update_background():
        # Load and display the updated background GIF
        background = ImageTk.PhotoImage(Image.open(background_image).resize((800, 800)))
        background_label.configure(image=background)
        background_label.image = background  # Keep a reference to the image to prevent it from being garbage collected

        # Schedule the next update
        window.after(5000, update_background)
        # Start the initial update
    update_background()
    climate.lift()
    description.lift()
    temperature.lift()
    pressure.lift()
    climate_1.lift()
    description_1.lift()
    temperature_1.lift()
    pressure_1.lift()
    input.lift()
    mic_button.lift()
    image_label.lift()
    heading.lift()
    button.lift()
    # Update the window
    window.update()
    climate_1.update()
    description_1.update()
    temperature_1.update()
    pressure_1.update()
    engine.runAndWait()
    window.after(60000, display_weather)

input = Entry(window,textvariable=city_input,font=("Arial", 16, "bold"),bg=style.colors.dark,fg=style.colors.light)
input.pack(pady=30)

climate = Label(window, text="Weather Climate", font=("Arial", 16, "bold"), bg=style.colors.primary)
climate.place(x=150, y=500)

description = Label(window,text="Weather Description",font=("Arial", 16, "bold"),bg=style.colors.primary,)
description.place(x=150, y=545)

temperature = Label(window, text="Temperature", font=("Arial", 16, "bold"), bg=style.colors.primary)
temperature.place(x=150, y=590)

pressure = Label(window, text="Pressure", font=("Arial", 16, "bold"), bg=style.colors.primary)
pressure.place(x=150, y=635)

button = Button(window,text="Check Weather",command=display_weather,bg=style.colors.primary,fg=style.colors.light,font=("Arial", 16, "bold"))
button.place(x=300, y=350)

window.mainloop()