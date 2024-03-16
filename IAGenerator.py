import requests
import base64
from io import BytesIO
from PIL import Image
import colorama
from colorama import Fore, Style
import os
import time
import json
import random
import importlib

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
            
                      
def buscar():
    urlKey = f"https://image-generation.perchance.org/api/verifyUser?thread=2&__cacheBust=0.1447499334121352"
    getkey = requests.get(url=urlKey).text
    data = json.loads(getkey)
    user_key = data['userKey']
    print(user_key)
    
    url1 = f'https://image-generation.perchance.org/checkVerificationStatus?userKey={user_key}&__cacheBust=0.1447499334121352'
    
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
    prompt = "anime, hentai, kawai, costplay, otaku"
    resolution = "512x768"
    #defino la url y reemplazo 
    url = f'https://image-generation.perchance.org/textToImage?prompt={dato}&seed=-1&resolution={resolution}&guidanceScale=7&negativePrompt={prompt}&channel=sexy-ai-art-generator&userKey={user_key}&requestId=0.5786562356902364'
    #realizo una peticion get a la url
    req = requests.get(url=url)
    texto = req.text
    print(texto)
    
    data = json.loads(texto)
    Image_key = data['imageId']
    
    urlimage = f"https://image-generation.perchance.org/api/downloadTemporaryImage?imageId={Image_key}"
    print(urlimage)
    
    headd = {
  "Host": "image-generation.perchance.org",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
  "Accept": "*/*",
  "Accept-Language": "en-US,en;q=0.5",
  "Referer": "https://image-generation.perchance.org/embed",
  "Connection": "keep-alive",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin"
}

    imagegen = requests.get(url=urlimage,headers=headd)
    if imagegen.status_code == 200:
        image_data = imagegen.content
        with open("result.jpg", "wb") as f:
            f.write(image_data)
    


def verimagen():
    try:
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
        importlib.import_module('resetAPI')
        menu()
    else:
        print('Opcion incorrecta o No existe')

menu()
