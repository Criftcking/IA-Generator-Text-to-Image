from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
import time
import importlib

# Configurar el user-agent deseado
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"

# Configurar las opciones del navegador con el user-agent
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")

# Iniciar el navegador Chrome con las opciones configuradas
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Abrir la URL
url = "https://perchance.org/pretty-ai"
driver.get(url)

# Esperar hasta que la página esté completamente cargada
time.sleep(7)

# Crear una instancia de ActionChains
action_chains = ActionChains(driver)

# Mover el mouse a una posición específica y hacer clic
pyautogui.moveTo(958, 469, duration=1)
pyautogui.click()

msj = importlib.import_module("mensaje")

tiempo_de_espera = 15  # 300 segundos = 5 minutos
tiempo_inicial = time.time()
while time.time() - tiempo_inicial < tiempo_de_espera:
    pass 

from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Mensaje", "API restored successfully.")

# Cerrar el navegador después de esperar el tiempo especificado
driver.quit()
