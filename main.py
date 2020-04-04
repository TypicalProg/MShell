import requests
import os
import pyowm
from tkinter import *
from tkinter.filedialog import *

tk = Tk()
tk.withdraw()

def swp():
	print("\nВнимание! Для работы данной программы требуется подключение к Интернету!\n"
		"ex - Выйти из программы\n")

	while True:
		url = input("Введите URL сайта в формате https://*** или http://***: ")

		if url == "ex":
			break
		else:
			try:
				r = requests.get(url)
				code = r.text
				direct = os.getcwd()
				sf = asksaveasfilename()
				f = open(sf, 'w', encoding="utf-8")
				f.write(code)
				f.close()
				print("Файл успешно сохранен!")
				break
			except Exception as e:
				print("Введите корректное значение!\n")



def wea():
	print("\nВнимание! Для работы данной функции требуется подключение к интернету!\n")

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

def main():
	os.system("color a")
	os.system("cls")

	print("MShell [Version BETA]\n"
		"(c) Michrin Andrey (M14 Software), 2020. All rights reserved.\n"
		"Type \"help\", \"mHelp\", \"copyright\" for more information.")

	directory = os.getcwd()

	while True:
		command = input("\n" + directory + ">")
		
		if command == "mHelp":
			print("""
				#########################################################

				КОМАНДЫ, ДОСТУПНЫЕ В ПРОГРАММЕ
				help 		СИСТЕМНЫЕ КОМАНДЫ
				mHelp 		ПРОГРАММНЫЕ КОМАНДЫ
				copyright 	ИНФОРМАЦИЯ ОБ АВТОРЕ
				restart 	ПЕРЕЗАПУСК СЕССИИ
				cd              ПЕРЕМЕЩЕНИЕ ПО ДИРЕКТОРИЯМ
				feedback 	ОБРАТНАЯ СВЯЗЬ
				var 		ПЕРЕМЕННЫЕ СРЕДЫ
				weather 	УЗНАТЬ ПОГОДУ В КАКОМ-ЛИБО ГОРОДЕ
				calc 		КАЛЬКУЛЯТОР
				cwp 		СОХРАНЕНИЕ КОДА WEB-СТРАНИЦЫ
				
				#########################################################""")

		elif command == "var":
			print(os.environ)

		elif command == "restart":
			main()

		elif command == "cd":
			directory = input("> ")
			os.chdir(directory)
			directory = os.getcwd()

			if directory == "../":
				directory = os.getcwd()

		elif command == "feedback":
			os.startfile("feedback.exe")

		elif command == "copyright":
			print("#############################################################\n\n"
				"(c) Michrin Andrey (M14 Software), 2020. All rights reserved.\n"
				"Site - https://sites.google.com/view/m14software\n"
				"VK - https://vk.com/m14sw"
				"\n\n#############################################################")

		elif command == "weather":
			wea()

		elif command == "calc":
			os.startfile("calc.exe")

		elif command == "cwp":
			swp()

		elif command == "exit":
			break

		else:
			try:
				os.system(command)
			except Exception:
				print('"' + command + '"' + " не является внутренней или внешней командой, исполняемой программой или пакетным файлом.")

main()