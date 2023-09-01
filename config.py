import os # Importamos para poder listar y recorrer las imagenes

API_TOKEN = "6585838987:AAGlCDPgC6nh5S-iFYVMjXST1nvkGjcwBIY"

# Funcion que lista y devuelve las respuestas del bot
def list_response():
    with open('otros/respuestas.txt') as file_object:
        object = file_object.readlines() 
    return object

# Funcion que se encarga de listar las fotos a enviar
def rout_photo():
    directorio = "img/"
    contenido = os.listdir(directorio)
    img = []
    for ficheros in contenido:
        if os.path.isfile(os.path.join(directorio, ficheros)) and ficheros.endswith('.jpg'):
            img.append(ficheros)
    return img