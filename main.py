import ctypes
import os

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:20:03 2021

@author: Kostas Zafolias
"""
#lock desktop
ctypes.windll.user32.LockWorkStation()
#max volume and play mp3
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("rickroll.mp3")

# boost volume by 6dB
louder_song = song + 6

# reduce volume by 3dB
quieter_song = song - 3

#Play song
play(louder_song)

#save louder song 
louder_song.export("louder_song.mp3", format='mp3')

