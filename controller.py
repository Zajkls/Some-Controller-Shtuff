import pygame

clock = pygame.time.Clock()
import time
import pygame
import os
import asyncio
import math
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
sounds=['shock.mp3', 
        'laughing.mp3', 
        'failure.mp3', 
        'alert1.mp3', 
        'clapping.mp3', 
        'minnesota.mp3']
songs=['FNAF.mp3', 
       'cynthia.mp3', 
       'merry_go_round_of_life.mp3', 
       'twinleaftown.mp3', 
       'bltrack1.mp3', 
       'skyrimsound.mp3'
       'Imyours.mp3', 
       'let_her_go.mp3']

#inits
cur_channel = 0
cur_sound = 0
cur_song = 0
joystic = 0
all_sounds = len(sounds)
all_songs = len(songs)

joy = pygame.joystick.Joystick(joystic)
print(joy.get_name())
print(joy.get_button(0))
print(joy.get_instance_id())
#startup

joy.rumble(1, 1, 1000)
print("Booted")

joystick_movement = 0
pygame.mixer.music.set_volume(1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.__repr__())
            if not FORCE_SWITCH_OVERRIDE:
                if joy.get_button(1):
                    my_sound = Sound(sounds[cur_sound])
                    mixer.Channel(cur_channel).set_volume(pygame.mixer.music.get_volume())
                    mixer.Channel(cur_channel).play(my_sound)
                    cur_channel += 1
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
            if joy.get_button(7):
                joy.rumble(0.75, 0.75, 1250)
                if FORCE_SWITCH_OVERRIDE:
                    mixer.unpause()
                else:
                    mixer.stop()
                    mixer.music.stop()
                FORCE_SWITCH_OVERRIDE = not FORCE_SWITCH_OVERRIDE
        elif event.type == pygame.JOYAXISMOTION:
            if abs(event.value) >= 0.95:
                print(event)
                if event.axis == 0:
                    if event.value <= 0:
                        a = int((pygame.mixer.music.get_volume() - 0.01) * 1000)/1000
                        print(a)
                        pygame.mixer.music.set_volume(max(0, a))
                        print('DOWN ',end='')
                        print(pygame.mixer.music.get_volume())
                    elif event.value >= 0:
                        a = int((pygame.mixer.music.get_volume() + 0.01) * 1000)/1000
                        print(a)
                        pygame.mixer.music.set_volume(a)
                        print('UP ',end='')
                        print(pygame.mixer.music.get_volume())
                    for i in range(0, 100):
                        mixer.Channel(i).set_volume(pygame.mixer.music.get_volume())
            elif joy.get_button(9) and joy.get_button(10) and joy.get_button(6):
                quit()
    clock.tick(30)
