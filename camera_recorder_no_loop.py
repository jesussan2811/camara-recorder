from importlib.resources import path
import cv2
import os
import errno
def grabar(dir,primera):
    salidas = []    
    #nombre de la carpeta donde se guardan la grabacion  
    try:
        os.mkdir(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
     
    num = 5
    valores = [180,162,144,126,108]
    
    paths = []
    #SI ES LA PRIMERA CAMINATA SE DEBERÁN DE EMPLEAR 6 CAMARAS POR LO TANTO SE USARAN LOS SIGUIENTE VALORES
    #TANTO DE NUMERO COMO DE ANGULOS UTILIZADOS
    if primera:
        num = 6
        valores = [0,18,36,54,72,90]
    
    for i in range(num):
        paths.append(dir+"/take_"+valores[i]+".avi")
    
    video_capture_0 = cv2.VideoCapture(0)
    salidas.append(cv2.VideoWriter(paths[0],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    video_capture_1 = cv2.VideoCapture(1)
    salidas.append(cv2.VideoWriter(paths[1],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    video_capture_2 = cv2.VideoCapture(2)
    salidas.append(cv2.VideoWriter(paths[2],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    video_capture_3 = cv2.VideoCapture(3)
    salidas.append(cv2.VideoWriter(paths[3],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    video_capture_4 = cv2.VideoCapture(4)
    salidas.append(cv2.VideoWriter(paths[4],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    video_capture_5 = cv2.VideoCapture(5)
    salidas.append(cv2.VideoWriter(paths[5],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    if primera:
        video_capture_6 = cv2.VideoCapture(6)
        salidas.append(cv2.VideoWriter(paths[6],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    '''
    video_capture_7 = cv2.VideoCapture(7)
    salidas.append(cv2.VideoWriter(paths[7],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    
    video_capture_8 = cv2.VideoCapture(8)
    salidas.append(cv2.VideoWriter(paths[8],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    video_capture_9 = cv2.VideoCapture(9)
    salidas.append(cv2.VideoWriter(paths[9],cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    
    video_capture_10 = cv2.VideoCapture(10)
    salidas.append(cv2.VideoWriter('Toma_'+str(10)+'.avi',cv2.VideoWriter_fourcc(*'XVID'),60.0,(640,480)))
    '''


    while True:
        ret0, frame0 = video_capture_0.read()
        ret1, frame1 = video_capture_1.read()
        ret2, frame2 = video_capture_2.read()
       
        ret3, frame3 = video_capture_3.read()
         
        ret4, frame4 = video_capture_4.read()
        ret5, frame5 = video_capture_5.read()
        if primera:
            ret6, frame6 = video_capture_6.read()
        '''
        ret7, frame7 = video_capture_7.read()
        
        ret8, frame8 = video_capture_8.read()
        ret9, frame9 = video_capture_9.read()
        
        ret10, frame10 = video_capture_10.read()
        '''

        if (ret0):
            cv2.imshow('camara 0', frame0)
            salidas[0].write(frame0)

        if (ret1):
            cv2.imshow('camara 1', frame1)
            salidas[1].write(frame1)

        if (ret2):
            cv2.imshow('camara 2', frame2)
            salidas[2].write(frame2)
        
        if (ret3):
            cv2.imshow('camara 3', frame3)
            salidas[3].write(frame3)
         
        if (ret4):
            cv2.imshow('camara 4', frame4)
            salidas[4].write(frame4)    

        if (ret5):
            cv2.imshow('camara 5', frame5)
            salidas[5].write(frame5)
        
        if primera:
            if (ret6):
                cv2.imshow('camara 6', frame6)
                salidas[6].write(frame6)
            '''
        if (ret7):
            cv2.imshow('camara 7', frame7)
            salidas[7].write(frame7)
        
        if (ret8):
            cv2.imshow('camara 8', frame8)
            salidas[8].write(frame8)
        
        if (ret9):
            cv2.imshow('camara 9', frame9)
            salidas[9].write(frame9)
        
        if (ret10):
            cv2.imshow('camara 10', frame10)
            salidas[10].write(frame10)
        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture_0.release()
    video_capture_1.release()
    video_capture_2.release()
    
    video_capture_3.release()
   
    video_capture_4.release()
    video_capture_5.release()
    
    video_capture_6.release()
    '''
    video_capture_7.release()
    
    video_capture_8.release()
    video_capture_9.release()
    
    video_capture_10.release()
    '''
    cv2.destroyAllWindows()
