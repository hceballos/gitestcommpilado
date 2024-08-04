from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import platform

class Main(object):
	"""Clase principal para ejecutar el scraping"""

	def __init__(self):
		chrome_options = webdriver.ChromeOptions()
		sistema_operativo = platform.system()
		if sistema_operativo == 'Darwin':
			print("Estás utilizando un sistema Mac")
			chrome_options.add_argument('--ignore-certificate-errors')
			chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
			chrome_options.binary_location = '/Users/hector/Documents/Documents/desarrollo/validadorUrgenciasCommpilado/webdriver/chrome-mac/Chromium.app/Contents/MacOS/Chromium'  # Ruta a la versión de Chromium
			
			# Crear el objeto Service para especificar el path del chromedriver
			service = Service('/Users/hector/Documents/Documents/desarrollo/validadorUrgenciasCommpilado/webdriver/chrome-mac/chromedriver')
			
			# Pasar el objeto service y las opciones al controlador de Chrome
			try:
				driver = webdriver.Chrome(service=service, options=chrome_options)
				driver.maximize_window()
				
				# Intentar abrir la página web especificada
				driver.get("https://www.sis.mejorninez.cl/")
				print("Página abierta con éxito")
			except Exception as e:
				print(f"Error al abrir la página: {e}")

if __name__ == '__main__':
	Main()
