import requests
import tkinter as tk
from tkinter import messagebox

def tell_weather():
    api_key = "ff3d93b07bd64681bea175918240103"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get().strip()  # Remove leading/trailing whitespace from city name
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name")
        return

    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404, 500)
        weather_data = response.json()

        if weather_data.get("cod") == 200:  # Check if response code is 200 (success)
            main_data = weather_data.get("main")
            weather_description = weather_data.get("weather")[0].get("description")

            temp = main_data.get("temp")
            pressure = main_data.get("pressure")
            humidity = main_data.get("humidity")

            temp_field.delete(0, tk.END)
            temp_field.insert(0, f"{temp:.2f} Kelvin")

            atm_field.delete(0, tk.END)
            atm_field.insert(0, f"{pressure} hPa")

            humid_field.delete(0, tk.END)
            humid_field.insert(0, f"{humidity} %")

            desc_field.delete(0, tk.END)
            desc_field.insert(0, weather_description)
        else:
            messagebox.showerror("Error", f"City '{city_name}' not found")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data: {e}")

def clear_all():
    city_field.delete(0, tk.END)
    temp_field.delete(0, tk.END)
    atm_field.delete(0, tk.END)
    humid_field.delete(0, tk.END)
    desc_field.delete(0, tk.END)
    city_field.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weather Application")
    root.configure(background="light blue")
    root.geometry("425x175")

    # Labels
    labels = ["City name:", "Temperature:", "Atmospheric pressure:", "Humidity:", "Description:"]
    for i, label_text in enumerate(labels):
        label = tk.Label(root, text=label_text, fg="white", bg="dark gray")
        label.grid(row=i+1, column=0, sticky="E")

    # Entry fields
    city_field = tk.Entry(root)
    city_field.grid(row=1, column=1, ipadx="100")

    temp_field = tk.Entry(root)
    temp_field.grid(row=2, column=1, ipadx="100")

    atm_field = tk.Entry(root)
    atm_field.grid(row=3, column=1, ipadx="100")

    humid_field = tk.Entry(root)
    humid_field.grid(row=4, column=1, ipadx="100")

    desc_field = tk.Entry(root)
    desc_field.grid(row=5, column=1, ipadx="100")

    # Buttons
    button1 = tk.Button(root, text="Submit", bg="pink", fg="black", command=tell_weather)
    button1.grid(row=6, column=1)

    button2 = tk.Button(root, text="Clear", bg="pink", fg="black", command=clear_all)
    button2.grid(row=7, column=1)

    root.mainloop()
