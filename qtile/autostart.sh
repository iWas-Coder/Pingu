#!/bin/bash

picom --experimental-backends &

volumeicon &

# Audio
pulseaudio -k &
sleep 1 &
pulseaudio -D &

# Monitor
xset -dpms &
xset s off &

