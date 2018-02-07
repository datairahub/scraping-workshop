# -*- coding: UTF-8 -*-
import os, json, time
from selenium import webdriver
from datetime import datetime


def insert_anunces_selenium_follow():
	pagenum = 1

	chromedriver = 'C:\Python35\Tools\chromedriver.exe' #Windows y chrome
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)  #Windows y chrome

	current_url = ""
	start_url = 'https://www.airbnb.es/s/Madrid'
	driver.get(start_url)
	boton = False

	while True:

		if boton:
			try:
				#get links
				try:
					links = driver.find_elements_by_css_selector(".media-photo.media-cover")
					aptm_array = []

					for link in links:
						apartment_url = link.get_attribute("href")
						apartment_id = apartment_url.rsplit('/', 1)[-1]
						aptm = {
							"_id" : 'airbnb' + str(apartment_id),
							"url" : str(apartment_url),
							"status" : "pending",
							"date_ins" : datetime.now(),
						}
						aptm_array.append(aptm)

					if insert_many_documents_mdb('anunces', aptm_array):
						print('Toma enlaces!!!')

				except:
					print('No se han guardado los enlaces')
					
				next = driver.find_element_by_css_selector(".next.next_page a")
				next.click()
				boton = False
			except:
				boton = True
			boton = False

		print('move')
		time.sleep(2)

		#get links
		try:
			links = driver.find_elements_by_css_selector(".media-photo.media-cover")
			aptm_array = []

			for link in links:
				apartment_url = link.get_attribute("href")
				apartment_id = apartment_url.rsplit('/', 1)[-1]
				aptm = {
					"_id" : 'airbnb' + str(apartment_id),
					"url" : str(apartment_url),
					"status" : "pending",
					"date_ins" : datetime.now(),
				}
				aptm_array.append(aptm)

			if insert_many_documents_mdb('anunces', aptm_array):
				print('Toma enlaces!!!')

		except:
			print('No se han guardado los enlaces')

		#get next link
		try:
			next = driver.find_element_by_css_selector(".next.next_page a")
			next.click()
			boton = False

		except:
			boton = True

	print('Fin del programa')

insert_anunces_selenium_follow()