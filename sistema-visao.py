#      TESTANDO RECONHECIMENTE FACIAL PELA WEBCAM

import cv2

xml_haar_cascade = "haarcascade_frontalface_alt2.xml"

#carregar classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

#iniciar camera
cap = cv2.VideoCapture(0)

#definimos tamanho da imagem
#capture.set(cv2.CAP_DROP_FRAME_WIDTH, 640)
#capture.set(cv2.CAP_DROP_FRAME_HEIGHT, 480)


while not cv2.waitKey(20) & 0xFF == ord("q"):

    ret, frame_color = cap.read()

    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    face = faceClassifier.detectMultiScale(gray)

    for x, y, w, h in face:
        cv2.rectangle(frame_color, (x, y),  (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Reconhecimento Facial - ITF AUTOMACAO AMBEV", frame_color)


