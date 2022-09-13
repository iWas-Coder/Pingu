#!/bin/bash

PKGS=$(curl -s -X GET "https://raw.githubusercontent.com/iWas-Coder/Pingu/main/assets/pkg-lists/live" | tr '\n' ' ')

pacstrap /mnt $PKGS
