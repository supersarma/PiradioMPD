#!/usr/bin/python
#Control MPD Client volume using a physical rotary encoder
#pip install mopidy-spotify

from RPi import GPIO
from time import sleep
import os

clk = 23
dt = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


clkLastState = GPIO.input(clk)
# Donne le nombre de ligne dans le fichier de la playlist. Ne pas depasser
# Si ajout des liens dans le fichier plus tard, pas besoin de changer le code 
nombre_lignes_playlist = os.popen("wc -l < /home/pi/.mpd/playlists/radio.m3u").read()

#La Station jouée au démarrage est toujours 1 (crontab)
station_actuelle = 1

try:
        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                    if dtState != clkState:
                        if station_actuelle > 0 and station_actuelle < int(nombre_lignes_playlist):
                            station_actuelle += 1
                        else:
                             pass
                    else:
                        if station_actuelle > 1:
                            station_actuelle -=1
                        else:
                             pass
                    # lacer la lecture 
                    os.system("mpc play " + str(station_actuelle))
                    print("La station actuelle est de : " + str(station_actuelle))
                    print("Le nombre de lignes dans la palylist est de : " + nombre_lignes_playlist)
                    clkLastState = clkState
                    sleep(1)
finally:
        GPIO.cleanup
