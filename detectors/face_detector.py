from cv2 import *  


trained_face_data = CascadeClassifier('haarcascade_frontalface_default.xml')


# to capture vid from a webcam
webcam = VideoCapture(0)

while True:
    succesful_frame_read, frame = webcam.read()

    # must convert to grayscale 
    grayscaled_img = cvtColor(frame, COLOR_BGR2GRAY)

    # detect faces 
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # draw rectangles around the face (dynamically)
    for (x, y, w, h) in face_coordinates:
        rectangle(frame, (x, y), (x+w, y+h), (175,0, 0), 2)

    imshow('face detector', frame)
    key = waitKey(33)

    # stop if q is pressed 
    if key==81 or key==113:
        break 

# release the webcam 
webcam.release()
