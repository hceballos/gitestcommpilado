import sqlalchemy
import pandas as pd
import glob
from lib.fuente import Fuente
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
import re
import platform
import time
import sqlite3
import re
import platform
import pandas as pd
import glob
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from PyPDF2 import PdfReader
from lib.fuente import Fuente
from lib.elementos import Envio_Informacion, Click
from lib.reliquidacion80Bis.scrapyProceso.tablaPagos import TablaPagos


class scrapingSigfeReports():

	def getMac(self, query):
		chrome_options = webdriver.ChromeOptions()
		prefs = {
			'download.default_directory': '/Users/hector/Documents/Documents/desarrollo/convenios_y_transferencias/input_excel/resolucionesUrgencia/pdfs',
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing_for_trusted_sources_enabled": False,
			"safebrowsing.enabled": False
		}
		chrome_options.add_experimental_option('prefs', prefs)
		chrome_options.add_argument('--ignore-certificate-errors')
		chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
		chrome_options.binary_location = '..//convenios_y_transferencias//webdriver//chrome-mac//Chromium.app//Contents//MacOS//Chromium'  # Ruta a la versión de Chromium 114.0.5735.90
		#chrome_options.add_argument('--headless')
		driver = webdriver.Chrome(executable_path='..//convenios_y_transferencias//webdriver//chromedriver', chrome_options=chrome_options)
		driver.maximize_window()
		
		driver.get('https://www.sis.mejorninez.cl/')
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
		envioInformacion = Envio_Informacion()
		envioInformacion.envio_Informacion_by_name(driver, "usuario", "hceballos@servicioproteccion.gob.cl")
		envioInformacion.envio_Informacion_by_name(driver, "password", "Mejorninez1")
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ingresar"))).click()
		driver.get("https://a1.sis.mejorninez.cl/mod_financiero/Pagos/wf_InformePagos.aspx")
		time.sleep(5)

		for index, row in query.iterrows():
			# print(row)
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "lnkLimpiar"))).click()  # BOTON BUSCAR
			envioInforProyecto = Envio_Informacion()
			time.sleep(2.5)
			envioInforProyecto.envio_Informacion_by_name(driver, "txtPeriodo", row['MESANO'])

			time.sleep(1.5)
			try:
				envioInforProyecto.envio_Informacion_by_name(driver, "I_ProyectoCodigo$txtCodigo", row['CODPROYECTO'])
			except Exception as e:
				print(f"Error: {e}")
				envioInforProyecto.envio_Informacion_by_name(driver, "I_ProyectoCodigo$txtCodigo", row['CODPROYECTO'])
			time.sleep(1.5)
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnBuscarPagos"))).click()  # BOTON BUSCAR
			time.sleep(2.5)
		
			TablaPagos(row, driver)



	def getWin(self, query):
		chrome_options = webdriver.ChromeOptions()
		prefs = {
			'download.default_directory': '/Users/hector/Documents/Documents/desarrollo/convenios_y_transferencias/input_excel/resolucionesUrgencia/pdfs',
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing_for_trusted_sources_enabled": False,
			"safebrowsing.enabled": False
		}
		chrome_options.add_experimental_option('prefs', prefs)
		chrome_options.add_argument('--ignore-certificate-errors')
		chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
		# chrome_options.binary_location = '..//convenios_y_transferencias//webdriver//chrome-mac//Chromium.app//Contents//MacOS//Chromium'  # Ruta a la versión de Chromium 114.0.5735.90
		#chrome_options.add_argument('--headless')
		driver = webdriver.Chrome(executable_path='..//convenios_y_transferencias//webdriver//chromedriver', chrome_options=chrome_options)
		driver.maximize_window()
		
		driver.get('https://www.sis.mejorninez.cl/')
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
		envioInformacion = Envio_Informacion()
		envioInformacion.envio_Informacion_by_name(driver, "usuario", "hceballos@servicioproteccion.gob.cl")
		envioInformacion.envio_Informacion_by_name(driver, "password", "Mejorninez1")
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ingresar"))).click()
		driver.get("https://a1.sis.mejorninez.cl/mod_financiero/Pagos/wf_InformePagos.aspx")
		time.sleep(5)

		for index, row in query.iterrows():
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "lnkLimpiar"))).click()  # BOTON BUSCAR
			envioInforProyecto = Envio_Informacion()
			time.sleep(2.5)
			envioInforProyecto.envio_Informacion_by_name(driver, "txtPeriodo", row['MESANO'])

			time.sleep(1.5)
			try:
				envioInforProyecto.envio_Informacion_by_name(driver, "I_ProyectoCodigo$txtCodigo", row['CODPROYECTO'])
			except Exception as e:
				print(f"Error: {e}")
				envioInforProyecto.envio_Informacion_by_name(driver, "I_ProyectoCodigo$txtCodigo", row['CODPROYECTO'])
			time.sleep(1.5)
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btnBuscarPagos"))).click()  # BOTON BUSCAR
			time.sleep(2.5)
		
			TablaPagos(row, driver)


	def __init__(self, query):
		#self.datos = datos
		sistema_operativo = platform.system()
		if sistema_operativo == 'Darwin':
			print("Estás utilizando un sistema Mac")
			driver = self.getMac(query)
			#driver.close()
			#driver.quit()


		elif sistema_operativo == 'Windows':
			print("Estás utilizando un sistema Windows.")
			driver = self.getWin(query)
			driver.close()
			driver.quit()




if __name__ == '__main__':
	scrapingSigfeReports()
