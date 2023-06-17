import tkinter as tk
import requests
import time
from datetime import date

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=f38df0cf20c6b0393b1198abf3ce7dfe"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temperature = int(json_data['main']['temp_min'] - 273.15)
    max_temperature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    windSpeed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-19800))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-19800))
    final_info = condition + "\n" + str(temperature) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temperature) + "\n" + "Min Temp: " +str(min_temperature)+"\n"+"Pressure: "+str(pressure)+"\n"+ "Humidity: "+str(humidity) +"\n"+ "Wind Speed: " + str(windSpeed)+ "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: "+ sunset  
    label4.config(text = "Hello, The weather details for "+ city + " are:")
    label1.config(text = final_info)
    label2.config(text = final_data)
canvas = tk.Tk()
canvas.geometry("500x500")
canvas.title("Weather App")

f = ("poppins",15,"bold")
t = ("poppins",30,"bold")
k = ("poppins",12,"bold")
textfield = tk.Entry(canvas, justify='center', width = 20, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getWeather)
label3 = tk.Label(canvas,font=k)
label3.pack()
today = date.today()
format_date="DATE: " + f"{today:%a, %b %d %Y}"
label3.config(text = format_date)
label4 = tk.Label(canvas,font=k)
label4.pack()
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas,font = f)
label2.pack()
canvas.mainloop()