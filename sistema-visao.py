#      TESTANDO RECONHECIMENTE FACIAL PELA WEBCAM
from datetime import datetime
import numpy
import cv2

xml_haar_cascade = "haarcascade_frontalface_alt2.xml"

#carregar classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

#iniciar camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,100)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1100)

n = 1 #n é o número que vai identificar a imagem ou pallete 

while not cv2.waitKey(5) & 0xFF == ord("q"):

    # frame webcam
    ret, frame_color = cap.read()

    # Janela em branco para adicionar os contornos mais pra frente no código
    contornos = numpy.zeros(frame_color.shape, dtype='uint8')

    #Condição para armezenar um frame da webcam
    k = cv2.waitKey(5)
    
    if k == ord("s") :   #futuramente essa condição vai ser substituida pela biblioteca i\o do raspberry
        now = datetime.now() #extrai o timestamp da máquina host
        time = now.strftime("%Hh_%Mm_%Ss") #Horario de referencia para o programa
        cv2.imwrite("Pallet_Picture/pallete_"+ str(n) +"_"+ time +".jpg",frame_color)
        n += 1

    # frame arquivo de video
    ret, frame = cap.read()
    #frame_resized = rescaleFrame(frame)

    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT) #blur serve para diminuir o ruído de luz da imagem
    edge = cv2.Canny(blur, 125, 175) #os paramentros 125 e 175 de forma simplificada são a sensibilidade para detectar bordas
    contours, hierarchies = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    ret, thresh =cv2.threshold(gray,135,255,cv2.THRESH_BINARY) #os parametros precisam ser ajustados
    cv2.drawContours (contornos,contours,-1,(0,255,0),1)

    #ajuste de parametros do sistema neural.
    face = faceClassifier.detectMultiScale(gray, scaleFactor=1.5, minSize=(150, 150), minNeighbors=1)
  
    for x, y, w, h in face:
        cv2.rectangle(frame_color, (x, y),  (x + w, y + h), (0, 255, 0), 2)
    
<<<<<<< HEAD
    cv2.imshow("Reconhecimento Facial - ITF AUTOMACAO AMBEV", frame_color)
    #cv2.imshow("edge",edge)   

=======
    #cv2.imshow("Reconhecimento Facial - ITF AUTOMACAO AMBEV", frame_color)
    #cv2.imshow("gray",gray) 
    cv2.imshow("edge",edge)   
    cv2.imshow("thresh",thresh)
    cv2.imshow("contornos",contornos)
>>>>>>> c83c56d77f37607d25b956d36f061baf1997f68a
