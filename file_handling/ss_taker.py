# this isnt an AI file, it's just for fetching images of fake people from thispersondoesnotexist.com so we can test it's accuracy 
# i know that i should use urlretrieve, but i get http error 403 so im using this workaround 

from selenium import webdriver 
from pyautogui import * 
from cv2 import waitKey


browser = webdriver.Chrome()
browser.get('https://thispersondoesnotexist.com')

c = 0

while True:

    n = str(c)
    name = n + '.png'
    
    waitKey(2000)

    ss = screenshot()
    ss.save(rf'D:\images\{name}')

    browser.refresh()

    c += 1 
