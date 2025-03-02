import pygame
import psutil
import os
import subprocess
import time

pygame.init()
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
processes = [p.cmdline() for p in psutil.process_iter() if p.name().lower() in ['python.exe'] and 'controller.py' in p.cmdline()[1]]
clock = pygame.time.Clock()
running = bool(processes)
while True:
    processes = [p.cmdline() for p in psutil.process_iter() if p.name().lower() in ['python.exe'] and 'controller.py' in p.cmdline()[1]]
    if not processes and not running:
        print('not_running')
        for event in pygame.event.get():
            if joy.get_button(6):
                time.sleep(2)
                if joy.get_button(6):
                    running = True
                    subprocess.call([f"python.exe", f"controller.py"])
                    print('SUCCESS!')
    else:
        running = False
    print(processes)
    clock.tick(1)


