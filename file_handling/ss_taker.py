# this isnt an AI file, it's just for fetching images of fake people from thispersondoesnotexist.com so we can test it's accuracy 
# i know that i should use urlretrieve, but i get http error 403 so im using this workaround 

from selenium import webdriver 
import pyautogui 
from cv2 import waitKey


browser = webdriver.Chrome()
browser.get('https://thispersondoesnotexist.com')

c = 1

while True:

    n = str(c)
    name = n + '.png'
    
    waitKey(2000)

    ss = pyautogui.screenshot()
    ss.save(rf'D:\images\{name}')

    browser.refresh()

    c += 1 
