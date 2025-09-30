from tkinter import *
from PIL import ImageTk, Image, ImageSequence
import requests
import pyttsx3
import speech_recognition as sr
from ttkbootstrap import Style

# -------------------- Window Setup -------------------- #
window = Tk()
window.title("Weather Bot")
window.geometry("900x700")
window.resizable(0, 0)
style = Style(theme="superhero")

# -------------------- Global Variables -------------------- #
city_input = StringVar()
engine = pyttsx3.init()
r = sr.Recognizer()
bg_label = Label(window)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
current_gif = None
gif_frames_cache = {}  # Cache loaded GIFs
gif_anim_id = None

# -------------------- Heading -------------------- #
heading = Label(window, text="🌦 Weather Forecasting App",
                font=("Arial", 26, "bold"),
                bg=style.colors.primary, fg=style.colors.light)
heading.pack(fill=X)

# -------------------- Logo -------------------- #
img = Image.open("img.jpg").resize((130, 130))
photo = ImageTk.PhotoImage(img)
image_label = Label(window, image=photo, bg=style.colors.dark)
image_label.pack(pady=10)

# -------------------- Input Box -------------------- #
input_box = Entry(window, textvariable=city_input,
                  font=("Arial", 16, "bold"),
                  bg=style.colors.dark, fg=style.colors.light,
                  justify="center")
input_box.pack(pady=15, ipadx=5, ipady=5)

# -------------------- Labels -------------------- #
labels_text = ["Weather Climate", "Weather Description", "Temperature (°C)", "Pressure (hPa)"]
labels = {}
values = {}
for i, text in enumerate(labels_text):
    lbl = Label(window, text=text, font=("Arial", 16, "bold"), bg=style.colors.primary, fg="white")
    lbl.place(x=150, y=500 + i*45)
    labels[text] = lbl
    val = Label(window, text="", font=("Arial", 16, "bold"), bg=style.colors.dark, fg="white")
    val.place(x=500, y=500 + i*45)
    values[text] = val

# -------------------- Background GIF Animation -------------------- #
def animate_gif(frames, index=0):
    global gif_anim_id
    frame = frames[index]
    bg_label.configure(image=frame)
    bg_label.image = frame
    bg_label.lower()
    next_index = (index + 1) % len(frames)
    gif_anim_id = bg_label.after(100, animate_gif, frames, next_index)

def update_background_gif(gif_path):
    global current_gif, gif_frames_cache, gif_anim_id
    if gif_path == current_gif:
        return  # already showing this GIF

    if gif_anim_id:
        bg_label.after_cancel(gif_anim_id)
        gif_anim_id = None

    if gif_path not in gif_frames_cache:
        try:
            img = Image.open(gif_path)
            frames = [ImageTk.PhotoImage(frame.copy().resize((900, 700))) for frame in ImageSequence.Iterator(img)]
            gif_frames_cache[gif_path] = frames
        except Exception as e:
            print("Error loading GIF:", e)
            return

    current_gif = gif_path
    animate_gif(gif_frames_cache[gif_path])

# -------------------- Weather Fetch -------------------- #
def display_weather():
    api_key = "e0d91f9cbf1e3b4a51dc8dd7f31e57a1"
    city_name = city_input.get().strip()
    if not city_name:
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    res = requests.get(url)
    data = res.json()

    if data.get("cod") != 200:
        for val in values.values():
            val.config(text="N/A")
        values["Weather Description"].config(text="City not found")
        return

    kelvin = 273.15
    climate = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp = str(int(data["main"]["temp"] - kelvin))
    pressure = str(data["main"]["pressure"])

    # ---------------- Update Labels First ---------------- #
    values["Weather Climate"].config(text=climate)
    values["Weather Description"].config(text=description)
    values["Temperature (°C)"].config(text=temp)
    values["Pressure (hPa)"].config(text=pressure)

    # ---------------- Update Background GIF First ---------------- #
    cond = climate.lower()
    if "cloud" in cond:
        update_background_gif("clouds.gif")
    elif "drizzle" in cond:
        update_background_gif("drizzle.gif")
    elif "thunderstorm" in cond:
        update_background_gif("thunderstorm.gif")
    elif "rain" in cond:
        update_background_gif("rain.gif")
    elif "snow" in cond:
        update_background_gif("snow.gif")
    elif "clear" in cond:
        update_background_gif("clear.gif")
    else:
        update_background_gif("default.gif")

    window.update()  # Make sure GUI updates before speaking

    # ---------------- Voice Output After Update ---------------- #
    speech_text = f"The weather in {city_name} is {climate}. " \
                  f"Description: {description}. " \
                  f"Temperature: {temp} degrees Celsius. " \
                  f"Pressure: {pressure} hPascal."
    engine.say(speech_text)
    engine.runAndWait()

# -------------------- Voice Input -------------------- #
def run_voice():
    r.pause_threshold = 1.2
    r.energy_threshold = 12000
    try:
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=5)
            city = r.recognize_google(audio)
            input_box.delete(0, END)
            input_box.insert(0, city)
            display_weather()
    except sr.UnknownValueError:
        input_box.delete(0, END)
        input_box.insert(0, "Not found")
    except Exception as e:
        print("Voice input error:", e)

# -------------------- Buttons -------------------- #
check_btn = Button(window, text="Check Weather", command=display_weather,
                   bg=style.colors.primary, fg=style.colors.light,
                   font=("Arial", 16, "bold"))
check_btn.place(x=350, y=350)

mic_img = Image.open("mic.jpg").resize((40, 40))
mic_icon = ImageTk.PhotoImage(mic_img)
mic_btn = Button(window, image=mic_icon, command=run_voice, relief="groove")
mic_btn.place(x=600, y=260)

# -------------------- Initialize -------------------- #
update_background_gif("default.gif")
window.mainloop()
