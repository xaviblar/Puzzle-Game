# -*- coding: cp1252 -*-
##Importar librerias Tkinter y Random
from Tkinter import*
import random

##Funcion que recibe una ventana como argumento y muestra esta ventana
def mostrar(ventana):
    ventana.deiconify()

##Funcion que recibe una ventana como argumente y oculta esta ventana    
def ocultar(ventana):
    ventana.withdraw()

##Listas y variables globales utilizadas en diversas ocasiones del programa
listausuarios=[['Xavier','x','xaviblar']]
newuser=[]
usuario=""
lista_historial_numeros=[]
lista_historial_numeros_ord=[]
lista_historial_numeros_obj=[]
juego_numeros_actual=[]
tipo_ordenamiento=""
lista_historial_letras=[]
lista_historial_letras_ord=[]
lista_historial_letras_obj=[]
juego_letras_actual=[]

numeros2=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
##El modulo random.shuffle revuelve una lista
random.shuffle(numeros2[0])
random.shuffle(numeros2[1])
random.shuffle(numeros2[2])
random.shuffle(numeros2[3])
random.shuffle(numeros2)
matriz_numeros1=[]
numeros=[]
letras2=[[16,17,18,19,20,21,22],[23,24,25,26,27,28,29],[30,31,32,33,34,35,36],[37,38,39,40,41,42,43]]
##El modulo random.shuffle revuelve una lista
random.shuffle(letras2[0])
random.shuffle(letras2[1])
random.shuffle(letras2[2])
random.shuffle(letras2[3])
random.shuffle(letras2)
matriz_letras1=[]
letras=[]

##Funcion que recibe un elemento y una lista como argumentos, e inserta ese elemento en la lista de manera que respete el orden ascendente
def insertarordenados(ele,lista):
    i=0
    while i<len(lista):
        if lista[i][2]>ele[2]:
            lista.insert(i,ele)
            break
        else:
            i+=1
    if i==len(lista):
        lista.append(ele)

##Funcion que ordena ascendentemente la lista que contiene el historial de los juegos ganados con numeros
def ordenar_historial_numeros():
    global lista_historial_numeros
    global lista_historial_numeros_ord
    if lista_historial_numeros!=[]:
        insertarordenados(lista_historial_numeros[0],lista_historial_numeros_ord)
        del lista_historial_numeros[0]

##Funcion que ordena ascendentemente la lista que contiene el historia de los juegos ganados con letras
def ordenar_historial_letras():
    global lista_historial_letras
    global lista_historial_letras_ord
    if lista_historial_letras!=[]:
        insertarordenados(lista_historial_letras[0],lista_historial_letras_ord)
        del lista_historial_letras[0]

##Funcion que declara el tipo de ordenamiento como Ascendente Horizontal
def tipo_orden_asc_hori():
    global tipo_ordenamiento
    tipo_ordenamiento="Ascendente Horizontal"

##Funcion que declara el tipo de ordenamiento como Descendiente Horizontal
def tipo_orden_des_hori():
    global tipo_ordenamiento
    tipo_ordenamiento="Descendiente Horizontal"

##Funcion que declara el tipo de ordenamiento como Ascendente Vertical
def tipo_orden_asc_verti():
    global tipo_ordenamiento
    tipo_ordenamiento="Ascendente Vertical"

##Funcion que declara el tipo de ordenamiento como Descendente Vertical
def tipo_orden_des_verti():
    global tipo_ordenamiento
    tipo_ordenamiento="Descendiente Vertical"

##Funcion que inserta los datos de un juego ganado en la lista del historial de juegos con numeros
def insertar_historial():
    global lista_historial_numeros
    global juego_numeros_actual
    global usuario
    global movidas
    global tipo_ordenamiento
    juego_numeros_actual.append(usuario)
    juego_numeros_actual.append(tipo_ordenamiento)
    juego_numeros_actual.append(movidas)
    lista_historial_numeros.append(juego_numeros_actual)
    juego_numeros_actual=[]

##Funcion que inserta los datos de un juego ganado en la lista del historial de juegos con letras
def insertar_historial_letras():
    global lista_historial_letras
    global juego_letras_actual
    global usuario
    global movidas
    global tipo_ordenamiento
    juego_letras_actual.append(usuario)
    juego_letras_actual.append(tipo_ordenamiento)
    juego_letras_actual.append(movidas)
    lista_historial_letras.append(juego_letras_actual)
    juego_letras_actual=[]

##Funcion que termina la aplicacion
def salir():
    v0.destroy()

##Funcione que inserta un nuevo usuario a la lista de los usuarios del juego, esta funcion tambien valida que todos los datos hayan sido introducidos
def insertar_new():
    global newuser
    global listausuarios
    global usuario
    i=0
    if nickname_entry.get()!='' and password_entry.get()!='' and email_entry.get()!='':
        while i<len(listausuarios):
            if listausuarios[i][0]==nickname_entry.get():
                nickname_entry.set("")
                password_entry.set("")
                email_entry.set("")
                return mostrar(vnick_repetido)
            i+=1
        newuser.append(nickname_entry.get())
        newuser.append(password_entry.get())
        newuser.append(email_entry.get())
        listausuarios.append(newuser)
        usuario=nickname_entry.get()
        nickname_entry.set("")
        password_entry.set("")
        email_entry.set("")
        newuser=[]
        return mostrar(vregistrocorrecto)
    else:
        nickname_entry.set("")
        password_entry.set("")
        return mostrar(vregistroincorrecto)

##Funcion que comprueba si los datos introducidos al iniciar sesion, son correctos
def comprobar_login():
    usu=0
    nick=0
    password=1
    global listausuarios
    global usuario
    while len(listausuarios)>usu:
        if listausuarios[usu][nick]==nickname1_entry.get() and listausuarios[usu][password]==password1_entry.get():
            usuario=nickname1_entry.get()
            nickname1_entry.set("")
            password1_entry.set("")
            return mostrar(vlogincorrecto), ocultar(vlogin)
        else:
            usu+=1
    nickname1_entry.set("")
    password1_entry.set("")
    return mostrar(vlogin_incorrecto), ocultar(vlogin)

##Funcion para cambiar de posiciones el puzzle de numeros, recibe como argumentos la fila y la columna donde esta colocado el numero a intercambiar
##Comprueba que haya un cero a la izquierda, derecha, arriba o abajo de ese numero y si lo hay, coloca la imagen del numero en el espacio en blanco
##e inserta una imagen en blanco en la posicion original del numero (fila y columna enviadas como argumentos).
def cambiar(f,c):
    global blancox
    global blancoy
    global cont_movidas
    global movidas
    if f>0:
        if numeros2[f-1][c]==0:
            blancoy=f-1
            blancox=c
            matriz_numeros1[blancoy][blancox].config(image=numeros[f][c])
            matriz_numeros1[f][c].config(image=numeros[blancoy][blancox])
            numeros2[blancoy][blancox]=numeros2[f][c]
            numeros2[f][c]=0
            numeros[blancoy][blancox]=numeros[f][c]
            numeros[f][c]=PhotoImage(file="0.gif")
            movidas+=1
            cont_movidas.set(movidas)
    if f<3:
        if numeros2[f+1][c]==0:
            blancoy=f+1
            blancox=c
            matriz_numeros1[blancoy][blancox].config(image=numeros[f][c])
            matriz_numeros1[f][c].config(image=numeros[blancoy][blancox])
            numeros2[blancoy][blancox]=numeros2[f][c]
            numeros2[f][c]=0
            numeros[blancoy][blancox]=numeros[f][c]
            numeros[f][c]=PhotoImage(file="0.gif")
            movidas+=1
            cont_movidas.set(movidas)
    if c<3:
        if numeros2[f][c+1]==0:
            blancoy=f
            blancox=c+1
            matriz_numeros1[blancoy][blancox].config(image=numeros[f][c])
            matriz_numeros1[f][c].config(image=numeros[blancoy][blancox])
            numeros2[blancoy][blancox]=numeros2[f][c]
            numeros2[f][c]=0
            numeros[blancoy][blancox]=numeros[f][c]
            numeros[f][c]=PhotoImage(file="0.gif")
            movidas+=1
            cont_movidas.set(movidas)

    if c>0:
        if numeros2[f][c-1]==0:
            blancoy=f
            blancox=c-1
            matriz_numeros1[blancoy][blancox].config(image=numeros[f][c])
            matriz_numeros1[f][c].config(image=numeros[blancoy][blancox])
            numeros2[blancoy][blancox]=numeros2[f][c]
            numeros2[f][c]=0
            numeros[blancoy][blancox]=numeros[f][c]
            numeros[f][c]=PhotoImage(file="0.gif")
            movidas+=1
            cont_movidas.set(movidas)

##Funcion que muestra el historial de numeros en su respectiva ventana, crea un objeto tipo label para cada posicion de la matriz
##Donde estan guardados los datos del historial
def mostrar_historial_numeros():
    global lista_historial_numeros_ord
    global lista_historial_numeros_obj
    nombre_usu=Label(vhistorial_numeros,font=('Cambria','14'),bg="lightblue",text="Jugador     ")
    nombre_usu.grid(column=0, row=0)
    ltipo_orden=Label(vhistorial_numeros,font=('Cambria','14'),bg="lightblue",text="Tipo de Ordenamiento     ")
    ltipo_orden.grid(column=1, row=0)
    lmovidas=Label(vhistorial_numeros,font=('Cambria','14'),bg="lightblue",text="Cantidad de Movidas     ")
    lmovidas.grid(column=2, row=0)
    for i in range(len(lista_historial_numeros_ord)):
        lista_historial_numeros_obj.append([])
        lista_historial_numeros_obj[i]=lista_historial_numeros_ord[i][:]
    for y in range(len(lista_historial_numeros_obj)):
        for x in range(len(lista_historial_numeros_obj[y])):
            histo=StringVar()
            histo.set(lista_historial_numeros_ord[y][x])
            obj=Label(vhistorial_numeros,font=('Cambria','14'),bg="lightblue",textvariable=histo)
            lista_historial_numeros_obj[y][x]=obj
            lista_historial_numeros_obj[y][x].grid(column=x,row=y+1)
    

##Funcion que muestra el historial de letras en su respectiva ventana, crea un objeto tipo label para cada posicion de la matriz
##Donde estan guardados los datos del historial
def mostrar_historial_letras():
    global lista_historial_letras_ord
    global lista_historial_letras_obj
    nombre_usu1=Label(vhistorial_letras,font=('Cambria','14'),bg="lightblue",text="Jugador     ")
    nombre_usu1.grid(column=0, row=0)
    ltipo_orden1=Label(vhistorial_letras,font=('Cambria','14'),bg="lightblue",text="Tipo de Ordenamiento     ")
    ltipo_orden1.grid(column=1, row=0)
    lmovidas1=Label(vhistorial_letras,font=('Cambria','14'),bg="lightblue",text="Cantidad de Movidas     ")
    lmovidas1.grid(column=2, row=0)
    for i in range(len(lista_historial_letras_ord)):
        lista_historial_letras_obj.append([])
        lista_historial_letras_obj[i]=lista_historial_letras_ord[i][:]
    for y in range(len(lista_historial_letras_obj)):
        for x in range(len(lista_historial_letras_obj[y])):
            histo1=StringVar()
            histo1.set(lista_historial_letras_ord[y][x])
            obj1=Label(vhistorial_letras,font=('Cambria','14'),bg="lightblue",textvariable=histo1)
            lista_historial_letras_obj[y][x]=obj1
            lista_historial_letras_obj[y][x].grid(column=x,row=y+1)

##Funcion para cambiar de posiciones el puzzle de letras, recibe como argumentos la fila y la columna donde esta colocado la letra a intercambiar
##Comprueba que haya un blanco(numero 16) a la izquierda, derecha, arriba o abajo de ese numero y si lo hay, coloca la imagen de la letra en el espacio en blanco
##e inserta una imagen en blanco en la posicion original de la letra (fila y columna enviadas como argumentos).
def cambiar_letras(f,c):
    global blancox
    global blancoy
    global cont_movidas
    global movidas
    
    if f>0:
        if letras2[f-1][c]==16:
            blancoy=f-1
            blancox=c
            matriz_letras1[blancoy][blancox].config(image=letras[f][c])
            matriz_letras1[f][c].config(image=letras[blancoy][blancox])
            
            letras2[blancoy][blancox]=letras2[f][c]
            letras2[f][c]=16
            letras[blancoy][blancox]=letras[f][c]
            letras[f][c]=PhotoImage(file="16.gif")
            movidas+=1
            cont_movidas.set(movidas)
    
    if f<3:
        if letras2[f+1][c]==16:
            blancoy=f+1
            blancox=c
            matriz_letras1[blancoy][blancox].config(image=letras[f][c])
            matriz_letras1[f][c].config(image=letras[blancoy][blancox])
            letras2[blancoy][blancox]=letras2[f][c]
            letras2[f][c]=16
            letras[blancoy][blancox]=letras[f][c]
            letras[f][c]=PhotoImage(file="16.gif")
            movidas+=1
            cont_movidas.set(movidas)

    if c<6:     
        if letras2[f][c+1]==16:
            blancoy=f
            blancox=c+1
            matriz_letras1[blancoy][blancox].config(image=letras[f][c])
            matriz_letras1[f][c].config(image=letras[blancoy][blancox])
            letras2[blancoy][blancox]=letras2[f][c]
            letras2[f][c]=16
            letras[blancoy][blancox]=letras[f][c]
            letras[f][c]=PhotoImage(file="16.gif")
            movidas+=1
            cont_movidas.set(movidas)
    if c>0:
        if letras2[f][c-1]==16:
            blancoy=f
            blancox=c-1
            matriz_letras1[blancoy][blancox].config(image=letras[f][c])
            matriz_letras1[f][c].config(image=letras[blancoy][blancox])
            letras2[blancoy][blancox]=letras2[f][c]
            letras2[f][c]=16
            letras[blancoy][blancox]=letras[f][c]
            letras[f][c]=PhotoImage(file="16.gif")
            movidas+=1
            cont_movidas.set(movidas)

##Funcion para resetear todos los datos referentes al puzzle de numeros, olvida los objetos en la ventana y los inserta nuevamente de manera aleatoria, ademas la cantidad de movidas
##regresa a cero
def reset_numeros():
    global numeros2
    global matriz_numeros1
    global numeros
    global movidas
    global cont_movidas
    global tipo_ordenamiento
    for y in range(len(matriz_numeros1)):
        for x in range(len(matriz_numeros1)):
            matriz_numeros1[y][x].grid_forget()
    for y in range(len(lista_historial_numeros_obj)):
        for x in range(len(lista_historial_numeros_obj[y])):
            lista_historial_numeros_obj[y][x].grid_forget()
    numeros2=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    random.shuffle(numeros2[0])
    random.shuffle(numeros2[1])
    random.shuffle(numeros2[2])
    random.shuffle(numeros2[3])
    random.shuffle(numeros2)
    matriz_numeros1=[]
    numeros=[]
    movidas=0
    cont_movidas.set(movidas)
    tipo_ordenamiento=""

##Funcion para resetear todos los datos referentes al puzzle de letras, olvida los objetos en la ventana y los inserta nuevamente de manera aleatoria, ademas la cantidad de movidas
##regresa a cero
def reset_letras():
    global letras2
    global matriz_letras1
    global letras
    global movidas
    global cont_movidas
    global tipo_ordenamiento
    for y in range(len(matriz_letras1)):
        for x in range(len(matriz_letras1)):
            matriz_letras1[y][x].grid_forget()
    for y in range(len(lista_historial_letras_obj)):
        for x in range(len(lista_historial_letras_obj[y])):
            lista_historial_letras_obj[y][x].grid_forget()
    letras2=[[16,17,18,19,20,21,22],[23,24,25,26,27,28,29],[30,31,32,33,34,35,36],[37,38,39,40,41,42,43]]
    random.shuffle(letras2[0])
    random.shuffle(letras2[1])
    random.shuffle(letras2[2])
    random.shuffle(letras2[3])
    random.shuffle(letras2)
    matriz_letras1=[]
    letras=[]
    movidas=0
    cont_movidas.set(movidas)
    tipo_ordenamiento=""

##Funcion que  inserta las imagenes de los numeros y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal numeros2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar los numeros de manera Ascendente Horizontal
def numeros_asc_hori():
    global Newgame
    global Revolver
    for i in range(len(numeros2)):
        matriz_numeros1.append([])
        matriz_numeros1[i]=numeros2[i][:]
        
    for i in range(len(numeros2)):
        numeros.append([])
        numeros[i]=numeros2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<4:
            numeros[i3][i4]=PhotoImage(file=str(numeros[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<4:
            bnumero=Button(vordenar_numeros_asc_hori, image=numeros[i][i2])
            bnumero.config(command=lambda columna=i2, fila=i:cambiar(fila,columna) or comp_numeros_asc_hori())
            matriz_numeros1[i][i2]=bnumero
            matriz_numeros1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1
        
    lnum_movidas=Label(vordenar_numeros_asc_hori,font=('Cambria','11'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_numeros_asc_hori,font=('Cambria','11'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_numeros_asc_hori,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_numeros_asc_hori) or reset_numeros())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_numeros_asc_hori,image=iRevolver,command=lambda: reset_numeros() or numeros_asc_hori())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si los numeros estan ordenados de manera ascendente horizontal, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_numeros_asc_hori():    
    i=0
    i2=0
    num=numeros2[0][0]
    while i<4:
        if i==3:
            while i2<2:
                if numeros2[i][i2+1]>=num:
                    num=numeros2[i][i2+1]
                    i2+=1
                else:
                    return ""
            i2=0
            i+=1
        else:
            while i2<=2:
                if numeros2[i][i2+1]>=num:
                    num=numeros2[i][i2+1]
                    i2+=1
                else:
                    return ""
            i+=1
            i2=0
    insertar_historial()
    return mostrar(vwin), ocultar(vordenar_numeros_asc_hori)

##Funcion que  inserta las imagenes de los numeros y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal numeros2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar los numeros de manera Descendente Horizontal
def numeros_des_hori():
    global Newgame
    global Revolver
    for i in range(len(numeros2)):
        matriz_numeros1.append([])
        matriz_numeros1[i]=numeros2[i][:]
        
    for i in range(len(numeros2)):
        numeros.append([])
        numeros[i]=numeros2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<4:
            numeros[i3][i4]=PhotoImage(file=str(numeros[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<4:
            bnumero=Button(vordenar_numeros_des_hori, image=numeros[i][i2])
            bnumero.config(command=lambda columna=i2, fila=i:cambiar(fila,columna) or comp_numeros_des_hori())
            matriz_numeros1[i][i2]=bnumero
            matriz_numeros1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1

    lnum_movidas=Label(vordenar_numeros_des_hori,font=('Cambria','11'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_numeros_des_hori,font=('Cambria','11'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_numeros_des_hori,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_numeros_des_hori) or reset_numeros())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_numeros_des_hori,image=iRevolver,command=lambda: reset_numeros() or numeros_des_hori())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si los numeros estan ordenados de manera descendente horizontal, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_numeros_des_hori():
    i=0
    i2=0
    num=numeros2[0][0]
    while i<4:
        while i2<=2:
            if numeros2[i][i2+1]<=num:
                num=numeros2[i][i2+1]
                i2+=1
            else:
                return ""
        i2=0
        i+=1
    insertar_historial()
    return mostrar(vwin),ocultar(vordenar_numeros_des_hori)

##Funcion que  inserta las imagenes de los numeros y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal numeros2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar los numeros de manera Ascendente Vertical
def numeros_asc_verti():
    global Newgame
    global Revolver
    for i in range(len(numeros2)):
        matriz_numeros1.append([])
        matriz_numeros1[i]=numeros2[i][:]
        
    for i in range(len(numeros2)):
        numeros.append([])
        numeros[i]=numeros2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<4:
            numeros[i3][i4]=PhotoImage(file=str(numeros[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<4:
            bnumero=Button(vordenar_numeros_asc_verti, image=numeros[i][i2])
            bnumero.config(command=lambda columna=i2, fila=i:cambiar(fila,columna) or comp_numeros_asc_verti())
            matriz_numeros1[i][i2]=bnumero
            matriz_numeros1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1

    lnum_movidas=Label(vordenar_numeros_asc_verti,font=('Cambria','11'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_numeros_asc_verti,font=('Cambria','11'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_numeros_asc_verti,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_numeros_asc_verti) or reset_numeros())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_numeros_asc_verti,image=iRevolver,command=lambda: reset_numeros() or numeros_asc_verti())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si los numeros estan ordenados de manera ascendente vertical, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_numeros_asc_verti():
    i=0
    i2=0
    num=numeros2[0][0]
    while i2<4:
        if i2==3:
            while i<2:
                if numeros2[i+1][i2]>=num:
                    num=numeros2[i+1][i2]
                    i+=1
                else:
                    return ""
            i=0
            i2+=1
        else:
            while i<=2:
                if numeros2[i+1][i2]>=num:
                    num=numeros2[i+1][i2]
                    i+=1
                else:
                    return ""
            i=0
            i2+=1
    insertar_historial()
    return mostrar(vwin),ocultar(vordenar_numeros_asc_verti)

##Funcion que  inserta las imagenes de los numeros y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal numeros2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar los numeros de manera Descendente Vertical
def numeros_des_verti():
    global Newgame
    global Revolver
    for i in range(len(numeros2)):
        matriz_numeros1.append([])
        matriz_numeros1[i]=numeros2[i][:]
        
    for i in range(len(numeros2)):
        numeros.append([])
        numeros[i]=numeros2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<4:
            numeros[i3][i4]=PhotoImage(file=str(numeros[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<4:
            bnumero=Button(vordenar_numeros_des_verti, image=numeros[i][i2])
            bnumero.config(command=lambda columna=i2, fila=i:cambiar(fila,columna) or comp_numeros_des_verti())
            matriz_numeros1[i][i2]=bnumero
            matriz_numeros1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1

    lnum_movidas=Label(vordenar_numeros_des_verti,font=('Cambria','11'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_numeros_des_verti,font=('Cambria','11'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_numeros_des_verti,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_numeros_des_verti) or reset_numeros())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_numeros_des_verti,image=iRevolver,command=lambda: reset_numeros() or numeros_des_verti())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si los numeros estan ordenados de manera descendente vertical, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_numeros_des_verti():
    i=0
    i2=0
    num=numeros2[0][0]
    while i2<4:
        while i<=2:
            if numeros2[i+1][i2]<=num:
                num=numeros2[i+1][i2]
                i+=1
            else:
                return ""
        i=0
        i2+=1
    insertar_historial()
    return mostrar(vwin),ocultar(vordenar_numeros_des_verti)

##Funcion que  inserta las imagenes de las letras y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal letras2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar las letras de manera Ascendente Horizontal
def letras_asc_hori():
    global Newgame
    global Revolver
    for i in range(len(letras2)):
        matriz_letras1.append([])
        matriz_letras1[i]=letras2[i][:]
        
    for i in range(len(letras2)):
        letras.append([])
        letras[i]=letras2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<7:
            letras[i3][i4]=PhotoImage(file=str(letras[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<7:
            bletra=Button(vordenar_letras_asc_hori, image=letras[i][i2])
            bletra.config(command=lambda columna=i2, fila=i:cambiar_letras(fila,columna) or comp_letras_asc_hori())
            matriz_letras1[i][i2]=bletra
            matriz_letras1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1
    lnum_movidas=Label(vordenar_letras_asc_hori,font=('Cambria','9'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_letras_asc_hori,font=('Cambria','9'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_letras_asc_hori,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_letras_asc_hori) or reset_letras())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_letras_asc_hori,image=iRevolver,command=lambda: reset_letras() or letras_asc_hori())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si las letras estan ordenadas de manera Ascendente Horizontal, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_letras_asc_hori():
    
    i=0
    i2=0
    letra=letras2[0][0]
    while i<4:
        if i==3:
            while i2<5:
                if letras2[i][i2+1]>=letra:
                    letra=letras2[i][i2+1]
                    i2+=1
                else:
                    return ""
            i2=0
            i+=1
        else:
            while i2<=5:
                if letras2[i][i2+1]>=letra:
                    letra=letras2[i][i2+1]
                    i2+=1
                else:
                    return ""
            i+=1
            i2=0
    insertar_historial_letras()
    return mostrar(vwin),ocultar(vordenar_letras_asc_hori)

##Funcion que  inserta las imagenes de las letras y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal letras2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar las letras de manera Descendente Horizontal
def letras_des_hori():
    global Newgame
    global Revolver
    for i in range(len(letras2)):
        matriz_letras1.append([])
        matriz_letras1[i]=letras2[i][:]
        
    for i in range(len(letras2)):
        letras.append([])
        letras[i]=letras2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<7:
            letras[i3][i4]=PhotoImage(file=str(letras[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<7:
            bletra=Button(vordenar_letras_des_hori, image=letras[i][i2])
            bletra.config(command=lambda columna=i2, fila=i:cambiar_letras(fila,columna) or comp_letras_des_hori())
            matriz_letras1[i][i2]=bletra
            matriz_letras1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1

    lnum_movidas=Label(vordenar_letras_des_hori,font=('Cambria','9'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_letras_des_hori,font=('Cambria','9'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_letras_des_hori,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_letras_des_hori) or reset_letras())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_letras_des_hori,image=iRevolver,command=lambda: reset_letras() or letras_des_hori())
    brevolver.grid(column=1, row=5)
    
##Funcion que verifica si las letras estan ordenadas de manera Descendente Horizontal, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_letras_des_hori():
        i=0
        i2=0
        letra=letras2[0][0]
        while i<4:
            while i2<=5:
                if letras2[i][i2+1]<=letra:
                    letra=letras2[i][i2+1]
                    i2+=1
                else:
                    return ""
            i2=0
            i+=1
        insertar_historial_letras()
        return mostrar(vwin),ocultar(vordenar_letras_des_hori)

##Funcion que  inserta las imagenes de las letras y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal letras2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar las letras de manera Ascendente Vertical
def letras_asc_verti():
    global Newgame
    global Revolver
    for i in range(len(letras2)):
        matriz_letras1.append([])
        matriz_letras1[i]=letras2[i][:]
        
    for i in range(len(letras2)):
        letras.append([])
        letras[i]=letras2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<7:
            letras[i3][i4]=PhotoImage(file=str(letras[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<7:
            bletra=Button(vordenar_letras_asc_verti, image=letras[i][i2])
            bletra.config(command=lambda columna=i2, fila=i:cambiar_letras(fila,columna) or comp_letras_asc_verti())
            matriz_letras1[i][i2]=bletra
            matriz_letras1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1
    lnum_movidas=Label(vordenar_letras_asc_verti,font=('Cambria','9'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_letras_asc_verti,font=('Cambria','9'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_letras_asc_verti,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_letras_asc_verti) or reset_letras())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_letras_asc_verti,image=iRevolver,command=lambda: reset_letras() or letras_asc_verti())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si las letras estan ordenadas de manera Ascendente Vertical, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_letras_asc_verti():
    i=0
    i2=0
    letra=letras2[0][0]
    while i2<7:
        if i2==6:
            while i<2:
                if letras2[i+1][i2]>=letra:
                    letra=letras2[i+1][i2]
                    i+=1
                else:
                    return ""
            i=0
            i2+=1
        else:
            while i<=2:
                if letras2[i+1][i2]>=letra:
                    letra=letras2[i+1][i2]
                    i+=1
                else:
                    return ""
            i=0
            i2+=1
    insertar_historial_letras()
    return mostrar(vwin),ocultar(vordenar_letras_asc_verti)
        
##Funcion que  inserta las imagenes de las letras y asigna un boton con su respectiva imagen a cada posicion de la matriz, ademas crea dos clones de la matriz principal letras2
##donde se asignan los botones y las imagenes, esta funcion se ejecuta cada vez que se selecciona ordenar las letras de manera Descendente Vertical
def letras_des_verti():
    global Newgame
    global Revolver
    for i in range(len(letras2)):
        matriz_letras1.append([])
        matriz_letras1[i]=letras2[i][:]
        
    for i in range(len(letras2)):
        letras.append([])
        letras[i]=letras2[i][:]
            
    i3=0
    i4=0
    while i3<4:
        while i4<7:
            letras[i3][i4]=PhotoImage(file=str(letras[i3][i4])+".gif")
            i4+=1
        i4=0    
        i3+=1
         
    i=0
    i2=0
    while i<4:
        while i2<7:
            bletra=Button(vordenar_letras_des_verti, image=letras[i][i2])
            bletra.config(command=lambda columna=i2, fila=i:cambiar_letras(fila,columna) or comp_letras_des_verti())
            matriz_letras1[i][i2]=bletra
            matriz_letras1[i][i2].grid(column=i2,row=i)
            i2=i2+1
        i2=0
        i=i+1
    lnum_movidas=Label(vordenar_letras_des_verti,font=('Cambria','9'),bg="lightblue",text="Numero de Movimientos :")
    lnum_movidas.grid(column=0,row=4)
    lmovidas=Label(vordenar_letras_des_verti,font=('Cambria','9'),bg="lightblue",textvariable=cont_movidas)
    lmovidas.grid(column=1,row=4)
    bnew_game=Button(vordenar_letras_des_verti,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_letras_des_verti) or reset_letras())
    bnew_game.grid(column=0,row=5)
    brevolver=Button(vordenar_letras_des_verti,image=iRevolver,command=lambda: reset_letras() or letras_des_verti())
    brevolver.grid(column=1, row=5)

##Funcion que verifica si las letras estan ordenadas de manera Descendente Vertical, si es correcto retorna una ventana donde indica que ha ganado, de lo contrario no realiza nada
def comp_letras_des_verti():
    i=0
    i2=0
    letra=letras2[0][0]
    while i2<7:
        while i<=2:
            if letras2[i+1][i2]<=letra:
                letra=letras2[i+1][i2]
                i+=1
            else:
                return ""
        i=0
        i2+=1
    insertar_historial_letras()
    return mostrar(vwin),ocultar(vordenar_letras_des_verti)
   
 
##Ventana Principal del Puzzle, aqui se inicia sesion o se registra un nuevo usuario
v0=Tk()

##Imagenes para botones
iAceptar=PhotoImage(file="Aceptar.gif")
iAscHori=PhotoImage(file="AscHori.gif")
iAscVerti=PhotoImage(file="AscVerti.gif")
iDesHori=PhotoImage(file="DesHori.gif")
iDesVerti=PhotoImage(file="DesVerti.gif")
iHistorial=PhotoImage(file="Historial.gif")
iInicio=PhotoImage(file="Inicio.gif")
iLogin=PhotoImage(file="Login.gif")
iLogout=PhotoImage(file="Logout.gif")
iNewgame=PhotoImage(file="Newgame.gif")
iNewgame2=PhotoImage(file="Newgame2.gif")
iPuzzLetras=PhotoImage(file="PuzzLetras.gif")
iPuzzNumeros=PhotoImage(file="PuzzNumeros.gif")
iRegistrarse=PhotoImage(file="Registrarse.gif")
iRevolver=PhotoImage(file="Revolver.gif")
iSalir=PhotoImage(file="Salir.gif")
iHistoNumeros=PhotoImage(file="HistoNumeros.gif")
iHistoLetras=PhotoImage(file="HistoLetras.gif")

v0.config(bg="lightblue")
v0.geometry("500x500")
v0.title("Puzzle")
bregistrar=Button(v0,image=iRegistrarse,command=lambda:mostrar(vregistrar)or ocultar(v0))
bregistrar.pack()
blogin=Button(v0,image=iLogin,command=lambda:mostrar(vlogin)or ocultar(v0))
blogin.pack()
bsalir=Button(v0,image=iSalir,command=lambda:salir())
bsalir.pack()

##Contador de movimientos
cont_movidas=StringVar()
cont_movidas.set(0)
movidas=0

##Ventana para el proceso de registrar un nuevo usuario
vregistrar=Toplevel(v0)
vregistrar.config(bg="lightblue")
vregistrar.title("Registrar nuevo usuario")
vregistrar.geometry("500x500")
labnick=Label(vregistrar,font=('Cambria','14'),bg="lightblue",text="Escoja un Nombre de Usuario")
labnick.pack()
nickname_entry=StringVar()
nickname=Entry(vregistrar,textvar=nickname_entry)
nickname.pack()
labpass=Label(vregistrar,font=('Cambria','14'),bg="lightblue",text="Escoja una contraseña")
labpass.pack()
password_entry=StringVar()
password=Entry(vregistrar,textvar=password_entry)
password.pack()
labemail=Label(vregistrar,font=('Cambria','14'),bg="lightblue",text="Digite su E-mail")
labemail.pack()
email_entry=StringVar()
email=Entry(vregistrar,textvar=email_entry)
email.pack()
biniregistrar=Button(vregistrar,image=iRegistrarse,command=lambda:insertar_new() or ocultar(vregistrar))
biniregistrar.pack()
vregistrar.withdraw()
bsalir1=Button(vregistrar,image=iSalir,command=lambda:salir())
bsalir1.pack()

##Ventana para iniciar sesion
vlogin=Toplevel(v0)
vlogin.title("Iniciar Sesion")
vlogin.config(bg="lightblue")
vlogin.geometry("500x500")
labnick1=Label(vlogin,font=('Cambria','14'),bg="lightblue",text="Digite su Nombre de Usuario")
labnick1.pack()
nickname1_entry=StringVar()
nickname1=Entry(vlogin,textvar=nickname1_entry)
nickname1.pack()
labpass1=Label(vlogin,font=('Cambria','14'),bg="lightblue",text="Digite su contraseña")
labpass1.pack()
password1_entry=StringVar()
password1=Entry(vlogin,textvar=password1_entry)
password1.pack()
binilogin=Button(vlogin,image=iLogin,command=lambda:comprobar_login())
binilogin.pack()
vlogin.withdraw()
bsalir2=Button(vlogin,image=iSalir,command=lambda:salir())
bsalir2.pack()

##Ventana donde se elige en que modo jugar: Letras o Numeros
vfjuego=Toplevel(v0)
vfjuego.title("Elija el modo de juego")
vfjuego.config(bg="lightblue")
vfjuego.geometry("800x700")
num_o_letras=Label(vfjuego,font=('Cambria','14'),bg="lightblue",text="Escoja el Puzzle que desea jugar")
num_o_letras.pack()
bpuzznumeros=Button(vfjuego,image=iPuzzNumeros,command=lambda:mostrar(vordenar_numeros) or ocultar(vfjuego))
bpuzznumeros.pack()
bpuzzletras=Button(vfjuego,image=iPuzzLetras,command=lambda:mostrar(vordenar_letras) or ocultar(vfjuego))
bpuzzletras.pack()
blogout3=Button(vfjuego,image=iLogout,command=lambda:mostrar(v0) or ocultar(vfjuego))
blogout3.pack()
bsalir3=Button(vfjuego,image=iSalir,command=lambda:salir())
bsalir3.pack()
bhistorial_fjuego=Button(vfjuego,image=iHistorial,command=lambda:mostrar(vhistorial) or ocultar(vfjuego))
bhistorial_fjuego.pack()
vfjuego.withdraw()

##Ventana que muestra el mensaje de Sesion iniciada correctamente
vlogincorrecto=Toplevel(v0)
vlogincorrecto.title("Sesion Iniciada")
vlogincorrecto.config(bg="lightblue")
vlogincorrecto.geometry("450x75")
lablogincorrecto=Label(vlogincorrecto,font=('Cambria','14'),bg="lightblue",text="Has Iniciado Sesion Correctamente")
lablogincorrecto.pack()
baceptarlogin=Button(vlogincorrecto,image=iAceptar,command=lambda:mostrar(vfjuego) or ocultar(vlogincorrecto))
baceptarlogin.pack()
vlogincorrecto.withdraw()

##Ventana que muestra el mensaje de error al iniciar sesion
vlogin_incorrecto=Toplevel(v0)
vlogin_incorrecto.title("Usuario o contraseña invalida")
vlogin_incorrecto.config(bg="lightblue")
vlogin_incorrecto.geometry("650x75")
lablogin_incorrecto=Label(vlogin_incorrecto,font=('Cambria','14'),bg="lightblue",text="Nombre de Usuario o contraseña invalidas, digitalos nuevamente")
lablogin_incorrecto.pack()
baceptarlogin_inc=Button(vlogin_incorrecto,image=iAceptar,command=lambda:ocultar(vlogin_incorrecto) or mostrar(vlogin))
baceptarlogin_inc.pack()
vlogin_incorrecto.withdraw()

##Ventana que muestra el mensaje al registrarse correctamente
vregistrocorrecto=Toplevel(v0)
vregistrocorrecto.title("Registro exitoso")
vregistrocorrecto.config(bg="lightblue")
vregistrocorrecto.geometry("450x75")
labregistrocorrecto=Label(vregistrocorrecto,font=('Cambria','14'),bg="lightblue",text="Has sido registrado Correctamente")
labregistrocorrecto.pack()
baceptarregistro=Button(vregistrocorrecto,image=iAceptar,command=lambda:mostrar(vfjuego) or ocultar(vregistrocorrecto))
baceptarregistro.pack()
vregistrocorrecto.withdraw()

##Ventana que muestra un mensaje cuando no has sido ingresados todos los datos al intentar un registro de usuario
vregistroincorrecto=Toplevel(v0)
vregistroincorrecto.title("Complete todos los espacios")
vregistroincorrecto.config(bg="lightblue")
vregistroincorrecto.geometry("450x75")
labregistroincorrecto=Label(vregistroincorrecto,font=('Cambria','14'),bg="lightblue",text="Complete todos los espacios")
labregistroincorrecto.pack()
baceptarregistro_inc=Button(vregistroincorrecto,image=iAceptar,command=lambda:mostrar(vregistrar) or ocultar(vregistroincorrecto))
baceptarregistro_inc.pack()
vregistroincorrecto.withdraw()

##Ventana que muestra un mensaje al tratar de registrar un usuario  con un nick ya existente
vnick_repetido=Toplevel(v0)
vnick_repetido.title("Nickname no disponible")
vnick_repetido.config(bg="lightblue")
vnick_repetido.geometry("550x75")
labregistroincorrecto1=Label(vnick_repetido,font=('Cambria','14'),bg="lightblue",text="El Nickname seleccionado ya existe, seleccione otro")
labregistroincorrecto1.pack()
baceptarregistro_inc1=Button(vnick_repetido,image=iAceptar,command=lambda:mostrar(vregistrar) or ocultar(vnick_repetido))
baceptarregistro_inc1.pack()
vnick_repetido.withdraw()

##Ventana para elegir de que manera desea ordenar los numeros
vordenar_numeros=Toplevel(v0)
vordenar_numeros.config(bg="lightblue")
vordenar_numeros.title("Tipo de Ordenamiento")
vordenar_numeros.geometry("800x1000")
lab_ordenar_numeros=Label(vordenar_numeros,font=('Cambria','14'),bg="lightblue",text="Escoja la forma en que desea ordenar los numeros")
lab_ordenar_numeros.pack()
bnum_asc_hori=Button(vordenar_numeros,image=iAscHori,command=lambda:mostrar(vordenar_numeros_asc_hori) or ocultar(vordenar_numeros) or numeros_asc_hori() or tipo_orden_asc_hori())
bnum_asc_hori.pack()
bnum_des_hori=Button(vordenar_numeros,image=iDesHori,command=lambda:mostrar(vordenar_numeros_des_hori) or ocultar(vordenar_numeros) or numeros_des_hori() or tipo_orden_des_hori())
bnum_des_hori.pack()
bnum_asc_verti=Button(vordenar_numeros,image=iAscVerti,command=lambda:mostrar(vordenar_numeros_asc_verti) or ocultar(vordenar_numeros) or numeros_asc_verti() or tipo_orden_asc_verti())
bnum_asc_verti.pack()
bnum_des_verti=Button(vordenar_numeros,image=iDesVerti,command=lambda:mostrar(vordenar_numeros_des_verti) or ocultar(vordenar_numeros) or numeros_des_verti() or tipo_orden_des_verti())
bnum_des_verti.pack()
bnew_game1=Button(vordenar_numeros,image=iInicio,command=lambda:mostrar(vfjuego) or ocultar(vordenar_numeros))
bnew_game1.pack()
vordenar_numeros.withdraw()

##Ventana para elegir de que manera desea ordenar las letras
vordenar_letras=Toplevel(v0)
vordenar_letras.config(bg="lightblue")
vordenar_letras.title("Tipo de Ordenamiento")
vordenar_letras.geometry("800x1000")
lab_ordenar_letras=Label(vordenar_letras,font=('Cambria','14'),bg="lightblue",text="Escoja la forma en que desea ordenar las letras")
lab_ordenar_letras.pack()
blet_asc_hori=Button(vordenar_letras,image=iAscHori,command=lambda:mostrar(vordenar_letras_asc_hori) or ocultar(vordenar_letras) or letras_asc_hori() or tipo_orden_asc_hori())
blet_asc_hori.pack()
blet_des_hori=Button(vordenar_letras,image=iDesHori,command=lambda:mostrar(vordenar_letras_des_hori) or ocultar(vordenar_letras) or letras_des_hori() or tipo_orden_des_hori())
blet_des_hori.pack()
blet_asc_verti=Button(vordenar_letras,image=iAscVerti,command=lambda:mostrar(vordenar_letras_asc_verti) or ocultar(vordenar_letras) or letras_asc_verti() or tipo_orden_asc_verti())
blet_asc_verti.pack()
blet_des_verti=Button(vordenar_letras,image=iDesVerti,command=lambda:mostrar(vordenar_letras_des_verti) or ocultar(vordenar_letras) or letras_des_verti() or tipo_orden_des_verti())
blet_des_verti.pack()
bnew_game2=Button(vordenar_letras,image=iNewgame,command=lambda:mostrar(vfjuego) or ocultar(vordenar_letras))
bnew_game2.pack()
vordenar_letras.withdraw()

##Venta de notificacion de juego ganado, muestra las opciones de historial, nuevo juego o salir del puzzle  
vwin=Toplevel(v0)
vwin.config(bg="lightblue")
vwin.title("Felicidades")
lwin=Label(vwin,font=('Cambria','14'),bg="lightblue",text="Has Ganado!!!")
lwin.pack()
Bver_historial=Button(vwin,image=iHistorial,command=lambda:mostrar(vhistorial) or ocultar(vwin) or reset_numeros() or reset_letras() or ordenar_historial_numeros() or ordenar_historial_letras())
Bver_historial.pack()
Botro_juego=Button(vwin,image=iNewgame2,command=lambda:mostrar(vfjuego) or ocultar(vwin) or reset_numeros() or reset_letras() or ordenar_historial_numeros() or ordenar_historial_letras())
Botro_juego.pack()
Blogout_win=Button(vwin,image=iLogout,command=lambda:mostrar(v0) or ocultar(vwin) or reset_numeros() or reset_letras() or ordenar_historial_numeros() or ordenar_historial_letras())
Blogout_win.pack()
Bsalir=Button(vwin,image=iSalir,command=lambda:salir(v0))
Bsalir.pack()
vwin.withdraw()


##Ventana donde se muestra el puzzle de numeros Ascendente Horizontal
vordenar_numeros_asc_hori=Toplevel(v0)
vordenar_numeros_asc_hori.title("Numeros Ascendente Horizontal")
vordenar_numeros_asc_hori.config(bg="lightblue")
vordenar_numeros_asc_hori.geometry("824x900")
vordenar_numeros_asc_hori.withdraw()

##Ventana donde se muestra el puzzle de numeros Descendente Horizontal
vordenar_numeros_des_hori=Toplevel(v0)
vordenar_numeros_des_hori.title("Numeros Descendente Horizontal")
vordenar_numeros_des_hori.config(bg="lightblue")
vordenar_numeros_des_hori.geometry("824x900")
vordenar_numeros_des_hori.withdraw()

##Ventana donde se muestra el puzzle de numeros ascendente vertical
vordenar_numeros_asc_verti=Toplevel(v0)
vordenar_numeros_asc_verti.title("Numeros Ascendente Vertical")
vordenar_numeros_asc_verti.config(bg="lightblue")
vordenar_numeros_asc_verti.geometry("824x900")
vordenar_numeros_asc_verti.withdraw()

##Ventana donde se muestra el puzzle de numeros descendente vertical
vordenar_numeros_des_verti=Toplevel(v0)
vordenar_numeros_des_verti.title("Numeros Descendente Vertical")
vordenar_numeros_des_verti.config(bg="lightblue")
vordenar_numeros_des_verti.geometry("824x900")
vordenar_numeros_des_verti.withdraw()

##Ventana donde elegir si se desea ver  el historial de numeros o de letras
vhistorial=Toplevel(v0)
vhistorial.config(bg="lightblue")
vhistorial.title("Historial")
bhistorial_numeros=Button(vhistorial,image=iHistoNumeros,command=lambda:mostrar(vhistorial_numeros) or ocultar(vhistorial) or mostrar_historial_numeros())
bhistorial_numeros.pack()
bhistorial_letras=Button(vhistorial,image=iHistoLetras,command=lambda:mostrar(vhistorial_letras) or ocultar(vhistorial) or mostrar_historial_letras())
bhistorial_letras.pack()
vhistorial.withdraw()

##Ventana donde se muestra todo el historial de numeros
vhistorial_numeros=Toplevel(v0)
vhistorial_numeros.config(bg="lightblue")
vhistorial_numeros.title("Historial de numeros")
bsalir5=Button(vhistorial_numeros,image=iSalir,command=lambda:salir())
bsalir5.grid(column=3,row=1)
blogout5=Button(vhistorial_numeros,image=iLogout,command=lambda:mostrar(v0) or ocultar(vhistorial_numeros))
blogout5.grid(column=3,row=2)
bnew_game4=Button(vhistorial_numeros,image=iNewgame2,command=lambda:mostrar(vfjuego) or ocultar(vhistorial_numeros))
bnew_game4.grid(column=3, row=0)
vhistorial_numeros.withdraw()

##Ventana donde se muestra todo el historial de letras
vhistorial_letras=Toplevel(v0)
vhistorial_letras.config(bg="lightblue")
vhistorial_letras.title("Historial de letras")
bsalir6=Button(vhistorial_letras,image=iSalir,command=lambda:salir())
bsalir6.grid(column=3,row=1)
blogout6=Button(vhistorial_letras,image=iLogout,command=lambda:mostrar(v0) or ocultar(vhistorial_letras))
blogout6.grid(column=3,row=2)
bnew_game5=Button(vhistorial_letras,image=iNewgame2,command=lambda:mostrar(vfjuego) or ocultar(vhistorial_letras))
bnew_game5.grid(column=3, row=0)
vhistorial_letras.withdraw()

##Ventana donde se muestra el puzzle de letras asc horizontal
vordenar_letras_asc_hori=Toplevel(v0)
vordenar_letras_asc_hori.title("Letras Ascendente Horizontal")
vordenar_letras_asc_hori.config(bg="lightblue")
vordenar_letras_asc_hori.geometry("1267x800")
vordenar_letras_asc_hori.withdraw()

##Ventana donde se muestra el puzzle de letras descendente horizontal 
vordenar_letras_des_hori=Toplevel(v0)
vordenar_letras_des_hori.title("Letras descendente Horizontal")
vordenar_letras_des_hori.config(bg="lightblue")
vordenar_letras_des_hori.geometry("1267x800")
vordenar_letras_des_hori.withdraw()

##Ventana donde se muestra el puzzle de letras Ascendente Vertical       
vordenar_letras_asc_verti=Toplevel(v0)
vordenar_letras_asc_verti.title("Letras Ascendente Vertical")
vordenar_letras_asc_verti.config(bg="lightblue")
vordenar_letras_asc_verti.geometry("1267x800")
vordenar_letras_asc_verti.withdraw()

##Ventana donde se muestra el puzzle de letras Descendente Vertical
vordenar_letras_des_verti=Toplevel(v0)
vordenar_letras_des_verti.title("Letras descendente Vertical")
vordenar_letras_des_verti.config(bg="lightblue")
vordenar_letras_des_verti.geometry("1267x800")
vordenar_letras_des_verti.withdraw()

##Inicia la ventana principal y el programa
v0.mainloop()
