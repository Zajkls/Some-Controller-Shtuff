from pynput import mouse
import pynput
import time
import pygame
import os
import playsound
from playsound import playsound
import keyboard
import asyncio 

#mouse_listener = pynput.mouse.Listener(suppress=True)
#mouse_listener.start()


pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(101)
mousea = mouse.Controller()
mixer = pygame.mixer
Sound = pygame.mixer.Sound
pygame.joystick.init()
# The event listener will be running in this block
cur_channel = 0
FORCE_SWITCH_OVERRIDE = False
MASTER_OVERRIDE = False
options = False
count = 0
print(pygame.joystick.get_count())
def while_looper(joystic, sounds=[], songs=[]):
    cur_channel = 0
    cur_sound = 0
    cur_song = 0
    all_sounds = len(sounds)
    all_songs = len(songs)
    joy = pygame.joystick.Joystick(joystic)
    print(joy.get_name())
    print(joy.get_button(0))
    print(joy.get_instance_id())
    joy.rumble(1, 1, 1000)
    while True:
        with event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(event.__repr__())
                if joy.get_button(1):
                    mixer.Channel(cur_channel).play(Sound(sounds[cur_sound]))
                elif joy.get_button(0):
                    cur_song += 1
                    if cur_song >= all_songs:
                        cur_song = 0
                        joy.rumble(0.5, 0.5, 500)
                elif joy.get_button(3):
                    cur_song -= 1
                    if cur_song < 0:
                        cur_song = all_songs - 1
                        joy.rumble(0.5, 0.5, 1000)
                elif joy.get_button(18):
                    cur_sound -= 1
                    if cur_sound <= 0:
                        cur_sound = all_sounds - 1
                        joy.rumble(0.5, 0.5, 1000)
                elif joy.get_button(16):
                    cur_sound += 1
                    if cur_sound >= all_sounds:
                        cur_sound = 0
                        joy.rumble(0.5, 0.5, 500)
                elif joy.get_button(2):
                    mixer.stop()
                    mixer.unpause()
                    mixer.music.load(songs[cur_song])
                    mixer.music.play()
        clock.tick(30)
"""joystick= pygame.joystick.Joystick(0)
joystick.init()
joystick.rumble(1, 1, 1000)"""
while_looper(0, sounds=['shock.mp3', 'laughing.mp3', 'failure.mp3', 'sigma.ogg', 'minnesota.ogg'], songs=['FNAF.mp3', 'cynthia.mp3'])
with mouse.Events() as events:
    for event in events:
        if keyboard.is_pressed('v'):
            #mouse_listener.stgvop()
            quit()
        if type(event) == pynput.mouse.Events.Click:
            if not FORCE_SWITCH_OVERRIDE and not MASTER_OVERRIDE:
                if event.pressed:
                    if event.button == mouse.Button.x2:
                        print('FORWARD')
                        cur_channel += 1
                        options = not options
                    elif event.button == mouse.Button.middle:
                        print('MIDDLE')
                        if options:
                            MASTER_OVERRIDE = True
                        else:
                            mixer.Channel(cur_channel).play(Sound('laughing.mp3'))
                        cur_channel += 1
                    elif event.button == mouse.Button.left:
                        print('LEFT')
                        if options:
                            mixer.stop()
                            mixer.unpause()
                            mixer.music.load(f'cynthia.mp3')
                            mixer.music.play()
                        else:
                            mixer.Channel(cur_channel).play(Sound('shock.mp3'))
                        cur_channel += 1
                    elif event.button == mouse.Button.right:
                        print('RIGHT')
                        if options:
                            mixer.stop()
                            mixer.unpause()
                            mixer.music.load(f'FNAF.mp3')
                            mixer.music.play()
                        else:
                            mixer.Channel(cur_channel).play(Sound('failure.mp3'))
                        cur_channel += 1

            if event.button == mouse.Button.x1 and event.pressed:
                print('BACK')
                cur_channel += 1
                if FORCE_SWITCH_OVERRIDE:
                    mixer.unpause()
                    FORCE_SWITCH_OVERRIDE = not FORCE_SWITCH_OVERRIDE
                elif MASTER_OVERRIDE:
                    if count == 2:
                        mixer.unpause()
                        count = 0
                        MASTER_OVERRIDE = not MASTER_OVERRIDE
                    count += 1
                else:
                    mixer.music.stop()
                    mixer.stop()
                    mixer.music.pause()
                    FORCE_SWITCH_OVERRIDE = not FORCE_SWITCH_OVERRIDE

time.sleep(1)
