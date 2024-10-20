from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
# Inicializa el navegador
driver = webdriver.Chrome()
 
# Abre Google
driver.get("https://www.google.com")
 
search_box = driver.find_element(By.NAME, "q")
 
# Escribe "Fecha de hoy" y presiona Enter
search_box.send_keys("Fecha de hoy")
search_box.send_keys(Keys.RETURN)
 
# Espera un momento para que los resultados se carguen
time.sleep(2)
 
# Captura el resultado que contiene la fecha
date_element = driver.find_element(By.XPATH, '//div[@class="vk_bk dDoNo FzvWSb"]')
 
# Imprime el texto de la fecha en consola
print(date_element.text)
 
#En Wikipedia
 # Inicializar el navegador
driver = webdriver.Chrome()  # Asegúrate de que el driver esté en tu PATH
 
# Abrir Wikipedia
driver.get("https://www.wikipedia.org/")
 
# Almacenar el texto que deseas buscar
texto_a_buscar = "17 de octubre de 2024"
 
# Localizar el campo de búsqueda
campo_busqueda = driver.find_element(By.NAME, "search")
campo_busqueda.send_keys(texto_a_buscar)  # Ingresar texto
 
# Presionar el botón de búsqueda (lupa)
campo_busqueda.send_keys(Keys.RETURN)
 
# Esperar un poco para que cargue la página
time.sleep(3)
 
# Capturar el texto de "Resultados de la búsqueda"
resultados = driver.find_element(By.ID, "firstHeading").text
print("Resultados de la búsqueda:", resultados)
 
# Cerrar el navegador
driver.quit()