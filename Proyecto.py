#Autor(es): Vicente Ramirez y Luis Vallejos

def lectura_datos(proyecto): # Abrir archivos
    f= open(proyecto)
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

    return lista , cant_reg
    pass
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
    cantidad = 0
    for casosl in datos :
        loro = [5]
        fecha = casosl[2].split("-")
        if loro == "Loro" or "Loro Trincahue" and fecha[1] == "03" and fecha[2] == "2022" :
            cantidad = cantidad + 1
        print(cantidad)    
        return(cantidad)
def funcion_e(datos): # Grafico               #Gaviota , Piquero, Salteador, Pelicano, Guanay
    gaviota = 0
    piquero = 0
    salteador = 0
    pelicano = 0
    guanay = 0
    for i in datos :
        if i[5] == 'Gaviota' and i[9] == 'Positivo' :
            gaviota = gaviota + 1
        if i [5] == 'Piquero' and i[9] == 'Positivo' :
            piquero = piquero + 1
        if i[5] == ' Salteador' and i[9] == 'Positivo' :
            salteador = salteador +1
        if i[5] == 'Pelicano' and i[9] == 'Positivo' :
            pelicano = pelicano + 1
        if i[5] ==  'Guanay' and i[9] == 'Positivo' :
            guanay = guanay + 1
    return gaviota, piquero, salteador, pelicano, guanay
def generar_salida(region, casosf, casos_pelicano, casosl) :
    salida = open("ResultadoS3.txt", "w") as salida :   # Crear archivo de texto
    salida.write("Autor(es): Luis Vallejos Ávila, Vicente Ramírez Muñoz" + "\n")
    salida.write("Cantidad de casos detectados positivos Region" + "\n")
    salida.write('\t' + "Región de Arica: " + str(region[3]) + "\n")
    salida.write('\t' + "Región de Tarapaca:" + str(region[2])+ "\n")
    salida.write('\t' + "Región de Antofagasta:" + str(region[4]) + "\n")
    salida.write('\t' + "Región de Atacama:" + str(region[5]) + "\n")
    salida.write('\t' + "Región de Coquimbo:" + str(region[7]) + "\n")
    salida.write('\t' + "Región de Valparaíso:" + str(region[0]) + "\n")
    salida.write('\t' + "Región de Metropolitana:" + str(region[9]) + "\n")
    salida.write('\t' + "Región de O'Higgins:" + str(region[12]) + "\n")
    salida.write('\t' + "Región del Maule:" + str(region[6]) + "\n")
    salida.write('\t' + "Región de Ñuble:" + str(region[10]) + "\n")
    salida.write('\t' + "Región del Biobío:" + str(region[8]) + "\n")
    salida.write('\t' + "Región de La Araucanía:" + str(region[14]) + "\n")
    salida.write('\t' + "Región de Los Ríos:" + str(region[13]) + "\n")
    salida.write('\t' + "Región de Los Lagos:" + str(region[15]) + "\n")
    salida.write('\t' + "Región de Aysén:" + str(region[11]) + "\n")
    salida.write('\t' + "Región de Magallanes:" + str(region[1]) + "\n")
    salida.write("Casos positivos mes Febrero del 2023: " + str(casosf) + '\n')
    salida.write("Casos positivos especie Pelicanos: " + str(casos_pelicano + "\n"))
    salida.write("Incidencias 03/2022 del" "Loro Trincahue Chileno: " + str(casosl) + "\n" )

    pass

if __name__ == "__main__":
    datos= lectura_datos("protocolo_vigilancia.txt")
    positivos = funcion_a(datos) #casos_positivos
    pos_febr = funcion_b(datos)  #casospos_febr
    pelicano = funcion_c(datos) #casos_pelicanos(datos)
    loro = funcion_d(datos) #casosloro_marzo(datos)
    grafico = funcion_e(datos) #grafico(datos)
    generar_salida(positivos,pos_febr,pelicano,loro,grafico)