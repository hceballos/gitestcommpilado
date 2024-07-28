# https://sb.sigfe.gob.cl/jasperserver-pro/flow.html?_flowId=viewReportFlow&reportUnit=/SIGFE2/Reportes/SB_CarteraFinancieraContable&pp=u=hceballos2111&nombre_cuenta=1210601%20Deudores%20por%20Transferencias%20Corrientes%20al%20Sector%20Privado;&TITLESUBTITULOREPORTE=2111%20Servicio%20Nacional%20de%20Protecci%C3%B3n%20Especializada%20a%20la%20Ni%C3%B1ez%20y%20Adolescencia&TITLETIPOMONEDAREPORTE=Nacional%20-%20Unidad&TITLETITULOREPORTE2=Reporte%20Relacionado%20-%20Variaci%C3%83%C2%B3n%20Patrimonial%20Cartera%20Financiera&mostrar_detalle=false&ejercicio=2022&page=flow.html%3F_flowId=viewReportFlow&cuenta_contable=1210601&unidad_ejecutora=2111&vista_cuenta=CUENTA_PRINCIPAL&site=SB&contenido=T&cant_saldo=2022-01-01&ambiente=SIGFE2&url=http%3A//sb.sigfe.gob.cl%3A80/sigfeReports/comun/popup/popupJasperReportRelacionado.jsp&fecha_desde=2022-01-01&codigo_moneda=CLP&nombre_contenido=Saldos%20o%20Flujos&proceso_funcionalidad=VACF&codigo_contab=00&TITLETITULOREPORTE=Cartera%20Financiera%20Contable&server=https%3A//sb.sigfe.gob.cl/jasperserver-pro/&reporte_link=ComparativoCompromiso_Relacionado&mostrar_filtros=false&expresion_valores=1&fecha_hasta=2022-12-31&nombre_vista=Cuenta/Principal&ambiente=SIGFE2&site=SB&standAlone=true&decorate=no&readOnly=true&userLocale=es
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


class ScrapingSigfeReports(object):


	def iniciar_driver():
		"""
		Inicializa el driver de Chrome con una ruta relativa para el chromedriver.
		"""
		# Definir la ruta relativa al chromedriver
		ruta_relativa_chromedriver = os.path.join('..', 'mejorninez', 'webdriver', 'chromedriver')
		
		# Obtener la ruta absoluta del chromedriver
		ruta_absoluta_chromedriver = os.path.abspath(ruta_relativa_chromedriver)
		
		# Inicializar el driver de Chrome con la ruta absoluta del chromedriver
		driver = webdriver.Chrome(executable_path=ruta_absoluta_chromedriver)
		
		return driver


	def __init__(self):

		options = Options()
		options.headless = True
		

		driver = iniciar_driver()



		#driver = webdriver.Chrome(executable_path='..//mejorninez//webdriver//chromedriver')

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
	ScrapingSigfeReports()