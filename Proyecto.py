#Autor(es): Vicente Ramirez y Luis Vallejos
import matplotlib.pyplot as plt

def lectura_datos(datos): # Abrir archivos
    f= open(datos, "r", encoding="UTF-8")
    datos=[]
    for linea in f:
        linea= linea.rstrip("\n")
        lista = linea.split(",")
        datos.append(lista)
    f.close()
    return datos
def funcion_a(datos): # Casos por regiones
    lista = []
    for i in datos:
        region = i[3]
        if region not in lista :    #Para la lista si ya esta
            lista.append(region)

    cant_reg=[]
    for f in lista :
        cant=0
        for i in datos :
            if i[3] == f and i[9] == 'Positivo':    #primero se busca la region y se ve si el caso es positivo y se le suma 1
                cant = cant + 1
        cant_reg.append(cant)

    return lista , cant_reg, region
def funcion_b(datos): # Casos de Febrero
    cantidad = 0
    for casof in datos:
        fecha = casof[2].split("-")
        if fecha[1] == "02" and fecha[2] == "2023" :
            cantidad = cantidad + 1

    return cantidad, casof
def funcion_c(datos): # Casos de Pelicanos
    casos_pelicano = 0
    for i in datos:
        if i[5] == 'Pelicano' and i[9] == 'Positivo':
            casos_pelicano = casos_pelicano + 1
    return casos_pelicano
def funcion_d(datos): # Casos de Loros
    cantidad_loro = 0
    for casosl in datos :
        loro = [5]
        fecha = casosl[2].split("-")
        if loro == "Loro" or "Loro Trincahue" and fecha[1] == "03" and fecha[2] == "2022" :
            cantidad_loro = cantidad_loro + 1
        return cantidad_loro
def funcion_e(datos): # Grafico               #Gaviota , Piquero, Salteador, Pelicano, Guanay
    gaviota = 0
    piquero = 0
    salteador = 0
    pelicano = 0
    guanay = 0
    for i in datos :
        if 'Gaviota' in i[5] and 'Positivo' in i[9]  :
            gaviota = gaviota + 1
        if 'Piquero' in i [5] and 'Positivo' in i[9]  :
            piquero = piquero + 1
        if 'Salteador' in i[5] and 'Positivo' in i[9]  :
            salteador = salteador +1
        if 'Pelicano' in i[5] and 'Positivo' in i[9]  :
            pelicano = pelicano + 1
        if 'Guanay' in i[5] and 'Positivo' in  i[9] :
            guanay = guanay + 1
    print(gaviota, piquero, salteador, pelicano, guanay)
    #Datos para el grafico
    Especies = ["Gaviota", "Piquero", "Salteador", "Pelicano", "Guanay"]
    Conteo = gaviota, piquero, salteador , pelicano, guanay
    plt.bar(Especies, Conteo, color =["Yellow", "Blue", "Brown", "Gray", "Black"])
    plt.xlabel("Especies")
    plt.ylabel("Cantidad de Casos")
    plt.title("Casos Positivos por Especie")
    plt.show()
    return gaviota, piquero, salteador, pelicano, guanay, Conteo


def generar_salida(region, casosf, casos_pelicano, casosl) :
    salida = open("ResultadoS3.txt", "w", encoding="UTF-8" )               #Crear archivo de texto
    salida.write("Autor(es): Luis Vallejos Ávila, Vicente Ramírez Muñoz" + "\n")
    salida.write("Cantidad de casos detectados positivos región:" + "\n")
    salida.write('\t' + "Región de Arica: " + str(cant_reg[3]) + "\n")
    salida.write('\t' + "Región de Tarapaca: " + str(cant_reg[2])+ "\n")
    salida.write('\t' + "Región de Antofagasta: " + str(cant_reg[4]) + "\n")
    salida.write('\t' + "Región de Atacama: " + str(cant_reg[5]) + "\n")
    salida.write('\t' + "Región de Coquimbo: " + str(cant_reg[7]) + "\n")
    salida.write('\t' + "Región de Valparaíso: " + str(cant_reg[0]) + "\n")
    salida.write('\t' + "Región de Metropolitana: " + str(cant_reg[9]) + "\n")
    salida.write('\t' + "Región de O'Higgins: " + str(cant_reg[12]) + "\n")
    salida.write('\t' + "Región del Maule: " + str(cant_reg[6]) + "\n")
    salida.write('\t' + "Región de Ñuble: " + str(cant_reg[10]) + "\n")
    salida.write('\t' + "Región del Biobío: " + str(cant_reg[8]) + "\n")
    salida.write('\t' + "Región de La Araucanía: " + str(cant_reg[14]) + "\n")
    salida.write('\t' + "Región de Los Ríos: " + str(cant_reg[13]) + "\n")
    salida.write('\t' + "Región de Los Lagos: " + str(cant_reg[15]) + "\n")
    salida.write('\t' + "Región de Aysén: " + str(cant_reg[11]) + "\n")
    salida.write('\t' + "Región de Magallanes: " + str(cant_reg[1]) + "\n")
    salida.write("Casos positivos mes Febrero del 2023: " + str(cantidad) + '\n')
    salida.write("Casos positivos especie Pelicano: " + str(casos_pelicano) + "\n")
    salida.write("Incidencias 03/2022 del " "'Loro Trincahue Chileno': " + str(cantidad_loro) + "\n" )
    salida.close()



if __name__ == "__main__":
    datos = lectura_datos("protocolo_vigilancia.txt")
    lista, cant_reg, region = funcion_a(datos)
    cantidad, casof = funcion_b(datos)
    casos_pelicano = funcion_c(datos)
    cantidad_loro = funcion_d(datos)
    grafico = funcion_e(datos)
    salida = generar_salida(region,casof,casos_pelicano,cantidad_loro,)
