'''
Here we will be detecting genders instead of races in the previous 'race_counter.py'. For some context, read that if you haven't.
Again, all of the images are in the same directory as here as well as in D:\images. 

'''
from deepface import DeepFace 
from os import listdir 

dir = listdir('D:\images')

males = 0 
females = 0 
not_detected = 0 

for img in dir:
    try:
       x = DeepFace.analyze(img, actions=['gender'])

       print('On:', img)

       gender = x['gender']

       if gender == 'Man':
           males += 1
       elif gender == 'Woman':
           females += 1   
       else:
           print('no idea what gender is here')
        

    except ValueError:
        print('No face detected in ', img)
        not_detected += 1 
    
print('There are this many males: ', males)

print('There are this many females: ', females)

print('There were', not_detected, 'faces not detected')
        
'''        
Of 1647 images, there were 1638 which contained faces detected by the algorithm (accuracy is 99.45 percent).
Of the remaining faces, there were 936 males and 702 females. 
Thus, 57.14 percent of faces were male and 42.86 were female.
This is another example of this AI being biased, this time in terms of gender.

'''
