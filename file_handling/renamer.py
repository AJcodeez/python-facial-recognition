# some of the screenshots were of the loading page, so they had to be removed 
# that disrupted the order of the names; this script re-does that order

from os import rename, listdir 

dir = 'C:\images'

count = 1 

for file in listdir(dir):
    rename(rf'C:\images\{file}',rf'C:\images\{count}.png')
    count += 1 

