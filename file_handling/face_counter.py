# here we will be counting the number of faces detected from the images we saved 
# this will give us the accuracy of the algorithm developed by opencv 
# i ran it on a database of pictures of AI-generated faces and it returned as 100 percent accurate
# you can use any dataset you want  

from os import listdir
from cv2 import * 

face_data = CascadeClassifier('haarcascade_frontalface_default.xml')

dir = listdir('C:/images')

count = 0

for file in dir:
    
    img = imread('C:/images/'+file, 0) 
    
    faces = face_data.detectMultiScale(img)
    
    truth = False

    for (x, y, w, h) in faces:
      truth = True

    if truth == True:
        count += 1 
    else:
        count += 0 
    
    print('number of faces = ', count)

accuracy = count/len(dir)
print("The accuracy is ",(accuracy * 100), "percent.")
