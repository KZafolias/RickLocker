import ctypes

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:20:03 2021
@author: Kostas Zafolias
"""
import time
from pygame import mixer


mixer.init()
mixer.music.load("C:\Users\user\Desktop\sricklock\srickroll.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

# lock desktop
ctypes.windll.user32.LockWorkStation()
# max volume and play mp3
