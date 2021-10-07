#      TESTANDO RECONHECIMENTE FACIAL PELA WEBCAM
from datetime import datetime
import cv2

xml_haar_cascade = "haarcascade_frontalface_alt2.xml"

#carregar classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

#ajuste de dimensão tela de arquivos em videos
#def rescaleFrame(frame, scale=1.2):
    #width = int(frame.shape[1] * scale)
    #height = int(frame.shape[0] * scale)

    #dimensions = (width, height)

    #return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


#iniciar camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,100)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1100)

n = 1 #n é o número que vai identificar a imagem ou pallete 

while not cv2.waitKey(5) & 0xFF == ord("q"):

    # frame webcam
    ret, frame_color = cap.read()

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
    blur = cv2.GaussianBlur(frame_color, (3,3), cv2.BORDER_DEFAULT) #blur serve para diminuir o ruído de luz da imagem
    edge = cv2.Canny(frame_color, 125, 175) #a imagem frame_color vai ser substituida por blur futuramente após testes
    
    #ajuste de parametros do sistema neural.
    face = faceClassifier.detectMultiScale(gray, scaleFactor=1.5, minSize=(150, 150), minNeighbors=1)
  


    for x, y, w, h in face:
        cv2.rectangle(frame_color, (x, y),  (x + w, y + h), (0, 255, 0), 2)
  
    
    #cv2.imshow("Reconhecimento Facial - ITF AUTOMACAO AMBEV", frame_color)
    cv2.imshow("edge",edge)   

