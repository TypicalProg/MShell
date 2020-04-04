import pyowm
import os

os.system("color a")
os.system("cls")

print("Внимание! Для работы данной функции требуется подключение к интернету!\n")

while True:
	try:
		place = input("Введите название города: ")
		owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc", language="ru")
		observation = owm.weather_at_place(place)
		w = observation.get_weather()
		temp = w.get_temperature("celsius")["temp"]

		print("В городе " + place + " сейчас " + w.get_detailed_status() + ". Температура около " + str(temp) + "°C")
		break

	except Exception as e:
		        print("Введите корректное значение\n")