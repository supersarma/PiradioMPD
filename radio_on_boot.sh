#!/bin/bash
mpc clear
mpc load /home/pi/.mpd/playlists/radio.m3u
mpc volume 30
sleep 30
mpc play 1
