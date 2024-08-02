from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import sqlite3
import pandas as pd
import os

class scrapingSigfeReports:
	
	@staticmethod
	def iniciar_driver():
		"""
		Inicializa el driver de Chrome con una ruta relativa para el chromedriver.
		"""
		# Definir la ruta relativa al chromedriver
		ruta_relativa_chromedriver = os.path.join('chromedriver')
		print(ruta_relativa_chromedriver)
		# Obtener la ruta absoluta del chromedriver
		# ruta_absoluta_chromedriver = os.path.abspath('..//repositorio_clonado//webdriver//chromedriver')

		# Inicializar el driver de Chrome con la ruta absoluta del chromedriver
		driver = webdriver.Chrome(executable_path='..//repositorio_clonado//webdriver//chromedriver')
		
		return driver

	def __init__(self):
		options = Options()
		options.headless = False
		print("Inicializar el driver de Chrome")
		# Inicializar el driver de Chrome
		time.sleep(5000)
		self.driver = self.iniciar_driver()

		# Asignar las opciones al driver
		self.driver.options = options

		self.setUp(driver)

	def setUp(self, driver):
		fecha_desde = "2024-01-01"
		fecha_hasta = "2024-12-31"
		ejercicio   = "2024"
		coberturas = ["2111001", "2111002", "2111003", "2111004", "2111005", "2111006", "2111007", "2111008", "2111009", "2111010", "2111011", "2111012", "2111013", "2111014", "2111015", "2111016", "2111017"]


		i = 0
		for cobertura in coberturas:
			driver.execute_script("window.open('');")
			ResultadoBusqueda = driver.switch_to.window(driver.window_handles[i])
			urlDestino = "https://asin.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_DisponibilidadDevengoPresupuestario&pp=u=hceballos2111&fecha_desde="+fecha_desde+"&ejercicio="+ejercicio+"&codigo_moneda=CLP&TITLESUBTITULOREPORTE="+ cobertura +"%20Direcci%C3%B3n%20Nacional&TITLETIPOMONEDAREPORTE=Gasto%20-%20Nacional&TITLETITULOREPORTE=Disponibilidad%20de%20Devengos%20Presupuestarios&ambiente=SIGFE2&codigo_presupuesto=02&fecha_hasta="+fecha_hasta+"&unidad_ejecutora="+ cobertura +"&ambiente=SIGFE2&site=SB&standAlone=true&decorate=no&readOnly=true&userLocale=es"
			driver.get(urlDestino)
			i += 1
		time.sleep(5000)

if __name__ == '__main__':
	scrapingSigfeReports()
