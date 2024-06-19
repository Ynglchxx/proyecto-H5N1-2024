#Autor(es): Vicente Ramirez y Luis Vallejos

def lectura_datos(proyecto): # Abrir archivos
    f= open(proyecto)
    datos=[]
    for linea in f:
        linea= linea.rstrip("\n")
        lista = linea.split(",")
        datos.append(lista)
    f.close
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
    return cantidad
def funcion_c(datos): # Casos de Pelicanos
    casos_peli = 0
    for i in datos:
        if i[5] == 'Pelicano' and i[9] == 'Positivo':
            casos_peli = casos_peli + 1
    return casos_peli
def funcion_d(datos): # Casos de Loros
    casosl = []
    for casosl in datos :
        cantidad = 0
        loro = [5]
        fecha = casosl[2].split("-")
        if loro == "Loro" or "Loro Trincahue" and fecha[1] == "03" and fecha[2] == "2022" :
            cantidad = cantidad + 1
            casosl.append(cantidad)
            print(cantidad)
        return(cantidad)
def funcion_e(datos): # Grafico               #Gaviota , Piquero, Salteador, Pelicano, Guanay
    gaviota = 0
    for i in datos :
        if i[5] == 'Gaviota' and i[9] == 'Positivo' :
            gaviota = gaviota + 1
            gaviota.append(gaviota)
            print(gaviota)
        return gaviota
    gaviota.close

    piquero = 0
    for i in datos :
        if i [5] == 'Piquero' and i[9] == 'Positivo' :
            piquero = piquero + 1
            piquero.append(piquero)
        return piquero
    piquero.close

    salteador = 0
    for i in datos :
        if i[5] == ' Salteador' and i[9] == 'Positivo' :
            salteador = salteador +1
            salteador.append(salteador)
        return salteador
    salteador.close
    
    #GAVIOTA

    guanay = 0
    for i in datos :
        if i[5 == 'Guanay' and i[9] == 'Positivo'] :
            guanay = guanay + 1
            guanay.append(guanay)
        return guanay
    guanay.close

    pass

if __name__ == "__main__":
    datos= lectura_datos("protocolo_vigilancia.txt")
    #print(datos)
    positivos = funcion_a(datos) #casos_positivos
    print(positivos)
     #Regiones
    print(positivos[1][0]) #Cantidades
    pos_febr = funcion_b(datos)  #casospos_febr
    #print(pos_febr)
    pelicano = funcion_c(datos) #casos_pelicanos(datos)
    print(pelicano)
    loro = funcion_d(datos) #casosloro_marzo(datos)
    print(loro)
    grafico = funcion_e(datos) #grafico(datos)
    
    #generar_salida(positivos,pos_febr,pelicano,loro,grafico)