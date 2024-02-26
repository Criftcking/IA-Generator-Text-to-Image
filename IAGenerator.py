import requests
import base64
from io import BytesIO
from PIL import Image
import colorama
from colorama import Fore, Style
import os
import time
import json


urlredirect = 'https://perchance.org/sexy-ai-art-generator'



def abrir_url(urlredirect):
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Linux
        os.system(f'xdg-open {urlredirect}')
    elif sistema_operativo == 'nt':  # Windows
        os.system(f'start {urlredirect}')
    else:
        print("No se puede determinar el sistema operativo.")
        
        




colorama.init()


def limpiar_terminal():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac
            os.system('clear')
            
            
urlKey = "https://image-generation.perchance.org/api/verifyUser?thread=2&__cacheBust=0.1577499834121252"
getkey = requests.get(url=urlKey).text
data = json.loads(getkey)
user_key = data['userKey']


def buscar():
    urlKey = "https://image-generation.perchance.org/api/verifyUser?thread=2&__cacheBust=0.1577499834121252"
    getkey = requests.get(url=urlKey).text
    data = json.loads(getkey)
    user_key = data['userKey']
    print(user_key)
    
    url1 = f'https://image-generation.perchance.org/checkVerificationStatus?userKey={user_key}&__cacheBust=0.12611136192562977'
    
    headers = {
  "Host": "image-generation.perchance.org",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
  "Accept-Encoding": "gzip, deflate, br",
  "DNT": "1",
  "Connection": "keep-alive",
  "Cookie": "panoramaId_expiry=1691955059172",
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "none",
  "Sec-Fetch-User": "?1"
}

    
    urlacess = requests.get(url=url1)
    print(urlacess.text)

    #pido al usuario un valor y lo almaceno en una variable
    dato = input('Que imagen quieres generar? (describela en texto): ')
    #defino la url y reemplazo 
    url = f'https://image-generation.perchance.org/textToImage?prompt={dato}&seed=-1&resolution=512x768&guidanceScale=7&negativePrompt=, low-quality, deformed, text, poorly drawn, ugly, amputee, deformed&channel=sexy-ai-art-generator&userKey={user_key}&requestId=0.5786562356902364'
    #realizo una peticion get a la url
    req = requests.get(url=url)


    #almaceno la respuesta en una variable en formato de texto
    texto = req.text
   

    #creo un buscador para sacar lo que quiero desde donde empieza a donde termina de la cadena de texto
    inicio = texto.find('data:image/jpeg;base64,') + 1
    fin = texto.find('"],', inicio)
    valor = texto[inicio:fin]
    valore = valor[22:]
    


    #guardo el resultado en un txt
    texto_a_guardar = valore
    with open("base64.txt", "w") as archivo:
        archivo.write(texto_a_guardar)


def verimagen():
    try:
        # Leer la cadena base64 desde el archivo
        with open("base64.txt", "r") as file:
            base64_image = file.read().strip()

        # Decodificar la cadena base64 en bytes
        image_data = base64.b64decode(base64_image)

        # Crear un objeto de tipo BytesIO para simular un archivo en memoria
        image_stream = BytesIO(image_data)

        # Abrir la imagen usando la biblioteca PIL (Python Imaging Library)
        image = Image.open(image_stream)
        

        # Mostrar la imagen
        #image.show()
        image.save('result.jpg')
        abrir = Image.open('result.jpg')
        abrir.show()
        menu()

    except Exception as e:
        print("Hubo un error al decodificar o mostrar la imagen:", e)
        




def menu():
    limpiar_terminal()
    texto = Fore.LIGHTCYAN_EX+ """
    ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓ 
    ▓╫─▄▀────────────▄▀───────────▄▀─╫▓ by@ Criftcking | Criftcking_Real |GhostHat_Real
    ▓╫─▀▄───────────▐█────────────▀▄─╫▓ 
    ▓╫─▄▌▄───────────▀▄───────────▄▌▄╫▓
    ▓▄▀░▓░▀▄──────────▌─────────▄▀░▓░▀▓ 'Para donaciones'
    ▓░░░░░░░▌──────▄▄▀▀▄▄──────▐▓░░░░░▓ 
    ▓▓░░░░░▓▀────▄▀░░▓▓░░▀▄────▀▄░░░░░▓  BTC WALLET: 13MEq6AABjuzHZEprcRWDckS1PijxYNrPN
    ▓╫▓█▓█▓─────▐▓░░░░░░░░▓▌─────▓█▓█▓▓ 
    ▓╫▐░░░▌─────██▀▀▀▀▀▀▀▀██─────▐░░░╫▓ - 𝑮𝑬𝑵𝑬𝑹𝑨𝑫𝑶𝑹 𝑫𝑬 𝑰𝑴𝑨𝑮𝑬𝑵𝑬𝑺 𝑪𝑶𝑵 -
    ▓╫▐░█░▌───▄▄████████████▄▄───▐░█░╫▓   - 𝑰𝑵𝑻𝑬𝑳𝑰𝑮𝑬𝑵𝑪𝑰𝑨 𝑨𝑹𝑻𝑰𝑭𝑰𝑪𝑨𝑳 -
    ▓╫▐░░░▌───▐▓▓▓▌▐▒▓▓▒▌▐▓▓▓▌───▐░░░╫▓ 
    ▓╫▐░█░▌───▐▓▓▓▌▐▓▒▒▓▌▐▓▓▓▌───▐░█░╫▓ 
    ▓╫▐░░░▌▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄▐░░░╫▓ 
    ▓╫▐░█░███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███░█░╫▓ 
    ▓╫▐░░░▌░█▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▒▒▐░█░╫▓ 
    ◙═════════════════════════════════◙ 
    """
    print(texto)
    print()
    print("1- Iniciar / Start\n2- Exit\n3- Si te da error preciona esta opcion para ir a la web y restablecer la api\n\n")
    
    respuesta = int(input('Elige tu Opcion--> '))
    


    if respuesta == 1:
        buscar()
        verimagen()
    elif respuesta == 2:
        pass
    elif respuesta == 3:
        print('En la web debes de generar una imagen manual para desbloquear el bot')
        input('preciona enter para ir a la web: ')
        print('Redirigiendo a https://perchance.org/sexy-ai-art-generator')
        time.sleep(3)
        abrir_url(urlredirect)
        
    else:
        print('Opcion incorrecta o No existe')

menu()
1
