import camera_recorder_no_loop as recorder
import os

ocupado = False


# CON LA LETRA Q SE TERMINA LA GRABACION PARA PODER CONTINUAR
while True:
    print("Bienvenido al miltigraba-inador del caminar humano del area limitrofe")
    if(not ocupado):
        print("ingrese el nombre del sujeto de prueba")
        id = input()
        if(os.path.exists(id)):
            print("carpeta ya existente, elije otra")
            continue
        else:
            os.mkdir(id)
        ocupado = True
    
    print("Que desea hacer?")
    print("0 --- Grabar caminata normal")
    print("1 --- Grabar caminata con mochila")
    print("2 --- Grabar caminata con maleta")
    print("3 --- Grabar caminata abrigo")
    print("4 --- Grabar caminata con caja")
    print("5 --- salir")
    print("para terminar una grabacion presione la letra 'Q'")

    accion = int(input())


    #caminata normal
    if accion == 0:
    
        i = 0
        while i < 12:
            print("listo para grabar? 'y' para confirmar")
            if input() == 'y':
                #instruccion para grabar
                recorder.grabar(id+"/cn"+str(i), i%2==1)
                print("Desea descartar la grabacion? 'y' para confirmar")
                if input() == 'y':
                    continue
            else:
                continue
            i += 1

    #caminata con mochila
    if accion == 1:
        i = 0
        while i < 4:
            print("listo para grabar? 'y' para confirmar")
            if input() == 'y':
                #instruccion para grabar
                recorder.grabar(id+"/cmo"+str(i), i%2==1)
                print("Desea descartar la grabacion? 'y' para confirmar")
                if input() == 'y':
                    continue
            else:
                continue
            
            i += 1    
        

    #caminata con maletin
    if accion == 4:
        i = 0
        while i < 2:
            print("listo para grabar? 'y' para confirmar")
            if input() == 'y':
                #instruccion para grabar
                recorder.grabar(id+"/cma"+str(i), i%2==1)
                print("Desea descartar la grabacion? 'y' para confirmar")
                if input() == 'y':
                    continue
            else:
                continue
            
            i += 1    
       

    #caminata con abrigo
    if accion == 3:
        i = 0
        while i < 4:
            print("listo para grabar? 'y' para confirmar")
            if input() == 'y':
                #instruccion para grabar
                recorder.grabar(id+"/ca"+str(i), i%2==1)
                print("Desea descartar la grabacion? 'y' para confirmar")
                if input() == 'y':
                    continue
            else:
                continue
            
            i += 1    
        

    #caminata con caja
    if accion == 4:
        i = 0
        while i < 4:
            print("listo para grabar? 'y' para confirmar")
            if input() == 'y':
                #instruccion para grabar
                recorder.grabar(id+"/cc"+str(i), i%2==1)
                print("Desea descartar la grabacion? 'y' para confirmar")
                if input() == 'y':
                    continue
            else:
                continue
            
            i += 1
        

    #condicion de salida
    if accion == 5:
        break

    print("terminaste de grabar a "+id+"? 'y' para confirmar")
    if input() == "y":
        ocupado = False