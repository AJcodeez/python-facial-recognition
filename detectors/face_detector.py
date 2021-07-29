'''
we will be using haarcascades, a lightweight solution for detecting faces
when a face is detected, we will draw a rectangle around the face 
webcam feed will be used 
the .xml file with the haarcascade must be in the same directory as this file for it to work
keep in mind that haarcascades and the opencv function is optimised for speed instead of accuracy 
the following link will provide an explanation and demonstration of haarcascades:
https://towardsdatascience.com/computer-vision-detecting-objects-using-haar-cascade-classifier-4585472829a9

'''

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
