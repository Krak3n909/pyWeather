import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Weather App')

        self.location_label = tk.Label(root, text='Enter city name:')
        self.location_label.pack()

        self.location_entry = tk.Entry(root)
        self.location_entry.pack()

        self.get_weather_button = tk.Button(root, text='Get Weather', command=self.get_weather)
        self.get_weather_button.pack()

        self.weather_info_label = tk.Label(root, text='')
        self.weather_info_label.pack()

    def get_weather(self):
        city = self.location_entry.get()
        url = f'https://wttr.in/{city}?format=%t+%C+%w'

        try:
            response = requests.get(url)
            data = response.text

            # Update GUI
            self.weather_info_label.config(text=data)

        except Exception as e:
            messagebox.showerror('Error', 'Could not fetch weather data')

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
