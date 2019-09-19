#!/usr/bin/python2

import os
import pygame
import random
import time
import sys, signal
import subprocess

def get_win_size(window_id):
    data = subprocess.check_output("xwininfo -id " + window_id + " | grep -e Width -e Height | tr -s ' ' | cut -d ' ' -f 3 | tail -n 2", shell=True).splitlines()
    width = int(data[0])
    height = int(data[1])
    return (width, height)


def run_screensaver():
    def handle_term(signal, frame):
        pygame.quit()
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_term)

    windowid = os.environ['XSCREENSAVER_WINDOW']
    os.environ['SDL_WINDOWID'] = windowid

    pygame.init()

    window = pygame.display.set_mode((0,0)) # auto-resize
    window.fill((0,0,0))
    pygame.display.flip()

    #width, height = pygame.display.get_surface().get_size()
    width, height = get_win_size(windowid)

    logolocation = os.path.dirname(os.path.realpath(__file__)) + "/logon.png"
    xplogo = pygame.image.load(logolocation)
    imagew = 275
    imageh = 174

    pygame.display.flip()

    while True:
        window.fill((0,0,0))

        randw = random.randrange(10, width - imagew - 10) # 10 pixel gap
        randh = random.randrange(10, height - imageh - 10) # 10 pixel gap

        window.blit(xplogo, (randw, randh))
        pygame.display.flip()

        time.sleep(10)
