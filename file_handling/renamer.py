# some of the screenshots were of the loading page, so they had to be removed 
# that disrupted the order of the names; this script re-does that order

from os import rename, listdir 

dir = 'D:\images'

count = 1 

for file in listdir(dir):
    rename(rf'D:\images\{file}',rf'D:\images\{count}.png')
    count += 1 

