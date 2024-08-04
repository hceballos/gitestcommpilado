# chromedriver_path = '/Users/hector/Documents/Documents/desarrollo/validadorUrgenciasCommpilado/webdriver/chrome-mac/Chromium.app/Contents/MacOS/Chromium'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import platform
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Main:
	def __init__(self):
		chrome_options = webdriver.ChromeOptions()
		sistema_operativo = platform.system()


		if sistema_operativo == 'Darwin':
			print("Estás utilizando un sistema Mac")
			# Configuración de las opciones de Chrome
			chrome_options = Options()

			# Preferencias para la descarga de archivos
			prefs = {
			    'download.default_directory': '/Users/hector/Documents/Documents/desarrollo/convenios_y_transferencias/input_excel/resolucionesUrgencia/pdfs',
			    'download.prompt_for_download': False,
			    'download.directory_upgrade': True,
			    'safebrowsing_for_trusted_sources_enabled': False,
			    'safebrowsing.enabled': False
			}
			chrome_options.add_experimental_option('prefs', prefs)

			# Argumentos adicionales para la configuración del navegador
			chrome_options.add_argument('--ignore-certificate-errors')
			chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

			# Especificar la ubicación del binario de Chromium
			chrome_options.binary_location = '/Users/hector/Documents/Documents/desarrollo/validadorUrgenciasCommpilado/webdriver/chrome-mac/Chromium.app/Contents/MacOS/Chromium'

			# Ruta al archivo del controlador de Chrome
			chromedriver_path = '/Users/hector/Documents/Documents/desarrollo/validadorUrgenciasCommpilado/webdriver/chromedriver'

			# Configuración del servicio del controlador de Chrome
			service = Service(chromedriver_path)

			# Inicializar el navegador con las opciones y el servicio configurados
			driver = webdriver.Chrome(service=service, options=chrome_options)

			# Maximizar la ventana del navegador
			driver.maximize_window()
			print(" antes ")
			# Abrir la página web especificada
			driver.get('https://www.sis.mejorninez.cl/')

			time.sleep(8)

			print(" despues ")

if __name__ == '__main__':
	Main()

