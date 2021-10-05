#      TESTANDO RECONHECIMENTE FACIAL PELA WEBCAM

import cv2

xml_haar_cascade = "haarcascade_frontalface_alt2.xml"

#carregar classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

#ajuste de dimensão tela de arquivos em videos
def rescaleFrame(frame, scale=1.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


#iniciar camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,100)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1100)

while not cv2.waitKey(20) & 0xFF == ord("q"):


    # frame webcam
    ret, frame_color = cap.read()

    #Condição para armezenar um frame da webcam
    k = cv2.waitKey(250)

    if k == ord("s"):
        cv2.imwrite("Pallet_Picture/wasd.png",frame_color)

    # frame arquivo de video
    ret, frame = cap.read()
    frame_resized = rescaleFrame(frame)
   

    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    face = faceClassifier.detectMultiScale(gray)


    for x, y, w, h in face:
        cv2.rectangle(frame_color, (x, y),  (x + w, y + h), (0, 255, 0), 1)
  
    
    cv2.imshow("Reconhecimento Facial - ITF AUTOMACAO AMBEV", frame_color)
    


