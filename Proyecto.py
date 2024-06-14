#Autor(es): Vicente Ramirez 'El crack´ y Luis Vallejos 'El maquina' juntos son el "Duo Dinamita".
def lectura_datos(proyecto):
    f = open("proyecto.txt", 'r')
    for linea in f:
        datos.append(linea.strip().split(','))
        return datos




if __name__ =="__main__":
    datos= lectura_datos("proyecto.txt")
    print(datos)
    positivos = funcion_a(casos_positivos) #casos_positivos(datos)
    pos_febr = funcion_b(casospos_febr)  #casospos_febr(datos)
    pelicano= funcion_c(casos_pelicanos) #casos_pelicanos(datos)
    loro = funcion_d(casosloro_marzo) #casosloro_marzo(datos)
    grafico = funcion_e(grafico) #grafico(datos)
    generar_salida(datos,positivos,pos_febr,pelicano,loro,grafico)