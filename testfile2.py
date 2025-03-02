import pygame

import os
import sys
pygame.init()
def initialiseJoysticks():
    """Initialise all joysticks, returning a list of pygame.joystick.Joystick"""
    joysticks = []              # for returning

    # Initialise the Joystick sub-module
    pygame.joystick.init()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range( joystick_count ):
        joystick = pygame.joystick.Joystick( i )
        joystick.init()
        # NOTE: Some examples discard joysticks where the button-count
        #       is zero.  Maybe this is a common problem. 
        joysticks.append( joystick )

    # TODO: Print all the statistics about the joysticks
    if ( len( joysticks ) == 0 ):
        print( "No joysticks found" )
    else:
        for i,joystk in enumerate( joysticks ):
            print("Joystick %d is named [%s]" % ( i, joystk.get_name() ) )
            joystk.rumble(1, 1, 100)
            # etc.

    return joysticks

all_joysticks = initialiseJoysticks()
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if all_joysticks[0].get_button(0):
                print('HELLO!')
                print(all_joysticks[0].rumble(0.5, 0.5, 1000))
