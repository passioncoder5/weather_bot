---

# 🌦 Weather Bot

A Python GUI application to check the weather, with **animated background GIFs**, **voice input**, and **voice output** of weather details.

---
### Find the docker image of this as global docker image name aravindaakumar/weather-bot:latest
---

# 🌦 Weather Bot (Dockerized)

A **Python GUI Weather Application** with:

* ✅ Animated background GIFs based on weather conditions
* 🎙️ Voice input (ask the weather by speaking)
* 🔊 Voice output (weather details spoken aloud)
* 🖥️ Simple and responsive GUI

---

## 🚀 Run Anywhere with Docker

### **1️⃣ Pull the Image**

```bash
docker pull aravindaakumar/weather-bot:latest
```

### **2️⃣ Run with GUI + Sound (Linux)**

Allow Docker to access your X11 display and audio devices:

```bash
xhost +local:docker
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --device /dev/snd \
    aravindaakumar/weather-bot:latest
```

---

## 🛠️ Features

* 🌍 Check weather for **any city**
* 🎞️ **Animated GIF backgrounds** (clouds, rain, snow, etc.)
* 🎙️ **Voice input** for city names
* 🔊 **Voice output** with `pyttsx3`
* 🎨 Built with `Tkinter` + `ttkbootstrap`

---
## Build from source
## **Features**

* Check the weather for any city
* Animated GIF background based on weather condition
* Voice input for city name
* Voice output for weather details (climate, description, temperature, pressure)
* Simple and responsive GUI

---

## **Requirements**

* Python ≥ 3.10 (recommended 3.13)
* Internet connection (for weather API)
* OpenWeatherMap API key (replace in `weather_bot.py`)
* Microphone and speakers for voice input/output

**Python Packages:**

* Pillow
* requests
* pyttsx3
* SpeechRecognition
* ttkbootstrap
* PyAudio

---

## **Installation**

### **1️⃣ Clone the Project**

```bash
git clone https://github.com/yourusername/weather-bot.git
cd weather-bot
```

---

### **2️⃣ Create a Virtual Environment (Recommended)**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

---

### **3️⃣ Install Dependencies**

#### **Linux**

1. Install system dependency for PyAudio:

```bash
sudo apt-get update
sudo apt-get install portaudio19-dev python3-pyaudio
```

2. Install Python packages:

```bash
pip install -r requirements.txt
```

#### **Windows**

1. Download the correct PyAudio wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

   * Example for Python 3.11/3.13 64-bit:
     `PyAudio‑0.2.13‑cp311‑cp311‑win_amd64.whl`

2. Install the wheel:

```bash
pip install path\to\PyAudio‑0.2.13‑cp311‑cp311‑win_amd64.whl
```

3. Install the rest of the dependencies:

```bash
pip install Pillow requests pyttsx3 SpeechRecognition ttkbootstrap
```

**Troubleshooting:**

* If PyAudio installation fails on Linux, ensure `portaudio19-dev` is installed.
* On Windows, ensure you download the correct wheel for your Python version and architecture.

---

### **4️⃣ Prepare Assets**

Ensure the following files exist in the project directory:

* `img.jpg` – App logo
* `mic.jpg` – Microphone icon for voice input
* Weather GIFs:

  * `clouds.gif`
  * `drizzle.gif`
  * `thunderstorm.gif`
  * `rain.gif`
  * `snow.gif`
  * `clear.gif`
  * `default.gif`

> You can replace the GIFs/images with your own as long as the filenames remain the same.

---

### **5️⃣ Run the Application**

```bash
python weather_bot.py
```

* Enter a city name in the input box **or** click the **mic icon** to speak the city name.
* Press **Check Weather** to update the weather data and background GIF.
* Weather details will be spoken **after the GUI updates**.

---

## **6️⃣ Notes**

* Replace the API key in `weather_bot.py`:

```python
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
```

* Animated GIFs remain animated and update according to weather conditions.
* Voice input/output requires a working microphone and speakers.
* Make sure all image and GIF files are in the same folder as `weather_bot.py`.
* On first run, the GUI will initialize all widgets and background.

---

## **7️⃣ Requirements.txt**

```text
Pillow==10.4.0
requests==2.32.5
pyttsx3==2.99
SpeechRecognition==3.14.3
ttkbootstrap==1.14.2
PyAudio==0.2.14
charset_normalizer==3.4.3
idna==3.10
urllib3==2.5.0
certifi==2025.8.3
typing-extensions==4.15.0
standard-aifc==3.13.0
audioop-lts==0.2.2
standard-chunk==3.13.0
```

**Linux users:** install system dependencies for PyAudio first:

```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

**Windows users:** install PyAudio wheel as described above.

---

## **8️⃣ Credits**

* OpenWeatherMap API: [https://openweathermap.org/api](https://openweathermap.org/api)
* Python Libraries: Tkinter, Pillow, pyttsx3, SpeechRecognition, ttkbootstrap

---


