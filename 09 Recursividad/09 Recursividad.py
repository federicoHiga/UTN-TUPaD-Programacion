#Trabajo Práctico: Análisis y Navegación de Sistemas de Archivos mediante Recursividad 
#Estructura de DB

class Archivo:
    def __init__(self, nombre:str, tamano_bytes:int):
        self.nombre=nombre
        self.tamano_bytes=tamano_bytes

class Directorio:
    def __init__(self,nombre:str):
        self.nombre=nombre
        self.archivos=[]
        self.subdirectorios=[]

#Estructura de DB

#Directorio

root=Directorio("root/")
root.archivos.append(Archivo("documento.png", 1500))
root.archivos.append(Archivo("config.txt", 0))

imagenes=Directorio("imagenes/")
root.subdirectorios.append(imagenes)
imagenes.archivos.append(Archivo("foto1.png", 2000))
imagenes.archivos.append(Archivo("foto2.png", 3500))

proyectos=Directorio("proyectos/")
root.subdirectorios.append(proyectos)
proyectos.archivos.append(Archivo("avance.pdf", 800))
temp=Directorio("temp/")
proyectos.subdirectorios.append(temp)
temp.archivos.append(Archivo("log.txt",0))

#Directorio

#Funciones

#Calculo del tamaño total de un directorio

def calcular_tamano_total(directorio):
    
    total=0
    
    for archivo in directorio.archivos:
        total += archivo.tamano_bytes 

    for subdirectorios in directorio.subdirectorios:
        total += calcular_tamano_total(subdirectorios)

    return total

def buscar_por_extension(directorio, extension):

    encontrados = []

    # Revisar archivos del directorio actual
    for archivo in directorio.archivos:

        if archivo.nombre.endswith(extension):
            ruta = directorio.nombre + "/" + archivo.nombre
            encontrados.append(ruta)

    # Buscar también en los subdirectorios
    for subdirectorio in directorio.subdirectorios:

        resultados = buscar_por_extension(
            subdirectorio,
            extension
        )

        encontrados.extend(resultados)

    return encontrados


def limpiar_archivos_vacios(directorio):

    eliminados = 0
    archivos_validos = []

    # Revisar archivos del directorio actual
    for archivo in directorio.archivos:

        if archivo.tamano_bytes == 0:
            eliminados += 1
        else:
            archivos_validos.append(archivo)

    # Reemplazar por los archivos que no están vacíos
    directorio.archivos = archivos_validos

    # Repetir en los subdirectorios
    for subdirectorio in directorio.subdirectorios:
        eliminados += limpiar_archivos_vacios(subdirectorio)

    return eliminados



# Puebas


print("Tamaño total:")
print(calcular_tamano_total(root))

print("Archivos PDF:")
print(buscar_por_extension(root, ".pdf"))

print("Archivos vacíos eliminados:")
print(limpiar_archivos_vacios(root))