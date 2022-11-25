import os

CARPETA = 'contactos/'
EXTENCION = '.txt'

def app():

    crear_directorio()
    mostrar_menu()
    
    pregunta = True
    while pregunta:
        opcion=input('Seleccionar opción: \r\n')
        opcion=int(opcion)
        
        if opcion == 1:
            agregar_contacto()
            pregunta = False
        elif opcion == 2:
            print('Editar contacto \r\n')
            pregunta = False
        elif opcion == 3:
            print('Ver contacto \r\n')
            pregunta = False
        elif opcion == 4:
            print('Buscar contacto \r\n')
            pregunta = False
        elif opcion == 5:
            print('Eliminar contacto \r\n')
            pregunta = False
        else:
            print('Opcion no valida')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)           #Crea carpeta
    else:
        print('La carpeta ya existe')
        
def mostrar_menu():
    print('Menu\r\n\r\n')
    print('Seleccione lo que desea hacer:\r\n')
    print('1) Agregar contacto: \r\n')
    print('2) Editar contacto: \r\n')
    print('3) Ver contacto \r\n')
    print('4) Buscar contacto \r\n')
    print('5) Eliminar contacto \r\n')
    
def agregar_contacto():
    print('Escribe los datos del nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')
    
    with open(CARPETA + nombre_contacto + EXTENCION, 'w') as archivo:
        archivo.write('Nombre: ' + nombre_contacto + '\r\n')

app()