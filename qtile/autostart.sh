#!/bin/bash

# --- Setting my wallpaper
nitrogen --restore &

# --- Autostarting my compositor 
picom --config /home/sudozelda/.picom.conf &

# --- Autostarting my policykit
/usr/bin/lxpolkit &
