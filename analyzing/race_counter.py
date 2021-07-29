# this is where we will understand any racial bias in the AI on thispersondoesnotexist.com
# the numbers of faces with different races will be printed as output 
# there will be some images with poorly made faces, and we will thus know how good the AI is at making real-looking 
# faces from the number of files with no faces detected
# unfortunately this only worked when all of the images were in the same directory as this file 

from deepface import DeepFace
from os import listdir 

dir = listdir('D:\images')

asian = 0
indian = 0
black = 0 
white = 0 
middle_eastern = 0 
latino_hispanic = 0 
not_detected = 0 



for img in dir:

    try:

        x = DeepFace.analyze(img, actions=['race'])

        race = x['dominant_race']


        if race == 'asian':
            asian += 1 

        elif race == 'indian':
            indian += 1 

        elif race == 'black':
            black += 1

        elif race == 'white':
            white += 1 

        elif race == 'middle eastern':
            middle_eastern += 1 

        elif race == 'latino hispanic':
            latino_hispanic += 1 

        else:
            print(race)
    
    except ValueError:
        
        print('no face was detected in', img)
        not_detected += 1 


print('there are this many asians:', asian)

print('there are this many indians:', indian)

print('there are this many blacks:', black)

print('there are this many whites:', white)

print('there are this many middle easterns:', middle_eastern)

print('there are this many latino hispanics:', latino_hispanic)

print('there were ', not_detected, 'images with no faces detected.')
