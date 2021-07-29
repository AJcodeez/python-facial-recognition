'''
here we will use the same code in the face detector, along with some more to detect a smile 
if a smile is detected (using haarcascades) then 'smiling' will show beneath the box surrouding the face
again, the .xml file with the smile haarcascades must be in the same directory as this file for it to work 

'''

from cv2 import * 


# face and smile classifiers 
face_detector = CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = CascadeClassifier('haarcascade_smile.xml')

webcam = VideoCapture(0)

while True:
    succesful_frame_read, frame = webcam.read()

    if not succesful_frame_read:
        break

    gray_scaled_frame = cvtColor(frame, COLOR_BGR2GRAY)
    
    faces = face_detector.detectMultiScale(gray_scaled_frame)
    


    for (x, y, w, h) in faces:
        rectangle(frame, (x, y), (x+h, y+h), (0, 255, 0), 2)

        # get the sub frame (using numpy N-dimensional array slicing)
        the_face = frame[y:y+h, x:x+w]
        
        the_face_grayscale = cvtColor(the_face, COLOR_BGR2GRAY)
        
        smiles = smile_detector.detectMultiScale(the_face_grayscale,
                                            scaleFactor=1.7,
                                            minNeighbors=20)


        if len(smiles) > 0:
            putText(frame, 'smiling', (x, y+h+40), fontScale=1, 
            fontFace=FONT_HERSHEY_TRIPLEX, color=(255, 255, 255))


    imshow("smile detector", frame)
    key = waitKey(30)

    if key==81 or key==113:
        break

webcam.release()
destroyAllWindows()


print("Done\a")

