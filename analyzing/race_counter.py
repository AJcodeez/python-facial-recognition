'''
This is where we will understand any racial bias in the AI on thispersondoesnotexist.com.
The numbers of faces with different races will be printed as output.
There will be some images with poorly made faces, and we will thus know how good the AI is at making real-looking.
Faces from the number of files with no faces detected.
Unfortunately this only worked when all of the images were in the same directory as this file, as well as the directory which I have provided to the code.

'''

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


'''
Using the 'ss_taker.py' file in the file_handling folder, I collected a total of 1647 pictures, saved as png files in the directory 'D:\images'.
Of these, 9 were not detected as faces, so the accuracy of the AI making the faces on thispersondoesnotexist.com is 99.45 percent rounded off to two decimal places.
From the remaining 1638 face images, there were:
209 Asian faces (12.76 %);
16 South Asian faces (0.98 %);
1119 white faces (68.32 %);
45 black faces (2.75 %)
104 Middle-Eastern faces (6.35 %);
and 145 Latinx faces (8.85 %)

This clearly highlights a racial bias in the AI's algorithm, which is heavily tilting towards white/caucasian individuals.
Such an innovative and interesting display of the capabilities of artifical intelligence should not become yet another example of racial discrimination, and should be 
more diverse in terms of the ethnicities and races of the people it displays. 

'''
