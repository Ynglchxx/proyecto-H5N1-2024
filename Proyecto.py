#Autor(es): Vicente Ramirez 'El crack´ y Luis Vallejos 'El maquina' juntos son el "Duo Dinamita".
def lectura_datos(proyecto):
    f= open(proyecto)
    datos=[]
    for linea in f:
        linea= linea.rstrip("\n")
        lista = linea.split(",")
        datos.append(lista)
    f.close
    return datos
def funcion_a(datos):
    lista = []
    for i in datos:
        region = i[3]
        if region not in lista :    #Para la lista si ya esta
            lista.append(region)

    cant_reg=[]
    for f in lista :
        cant=0
        for i in datos :
            if i[3] == f and i[9] == 'Positivo':    #primero se busca la region y se ve si el caso es positivo y se agrega 1
                cant = cant + 1
        cant_reg.append(cant)

    return lista , cant_reg
    
    pass
def funcion_b(datos): #Casos de Febrero
    cantidad = 0
    for casof in datos:
        fecha = casof[2].split("-")
        if fecha[1] == "02" and fecha[2] == "2023" :
            cantidad = cantidad + 1
    return cantidad

def funcion_c(datos):
    pass
def funcion_d(datos):
    pass
def funcion_e(datos):
    pass

if __name__ == "__main__":
    datos= lectura_datos("protocolo_vigilancia.txt")
    #print(datos)
    positivos = funcion_a(datos) #casos_positivos
    print(positivos)
    print(positivos[0][0]) #Regiones
    print(positivos[1][0]) #Cantidades
    pos_febr = funcion_b(datos)  #casospos_febr
    print(pos_febr)
    #pelicano= funcion_c(datos) #casos_pelicanos(datos)
    #loro = funcion_d(datos) #casosloro_marzo(datos)
    #grafico = funcion_e(datos) #grafico(datos)
    #generar_salida(positivos,pos_febr,pelicano,loro,grafico)