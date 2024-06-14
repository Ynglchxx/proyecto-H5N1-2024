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
    pass
def funcion_b(datos):
    pass
def funcion_c(datos):
    pass
def funcion_d(datos):
    pass
def funcion_e(datos):
    pass

if __name__ == "__main__":
    datos= lectura_datos("protocolo_vigilancia.txt")
    print(datos)
    positivos = funcion_a(datos) #casos_positivos
    pos_febr = funcion_b(datos)  #casospos_febr(datos)
    pelicano= funcion_c(datos) #casos_pelicanos(datos)
    loro = funcion_d(datos) #casosloro_marzo(datos)
    grafico = funcion_e(datos) #grafico(datos)
    generar_salida(positivos,pos_febr,pelicano,loro,grafico)