#!/bin/sh

# === Compositor === #
picom &

# === Wallpaper === #
feh --bg-center /usr/share/wallpaper/wallpaper_1.jpg --bg-center /usr/share/wallpaper/wallpaper_2.jpg &

# === Volumeicon System Tray Icon === #
volumeicon &
