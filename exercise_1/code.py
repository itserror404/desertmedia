# SPDX-FileCopyrightText: 2023 Maimuna Zaheer
# SPDX-License-Identifier: MIT

import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3 
speed= 10 # 20 for smooth transition

while True:
    # Cherry Blossom (Bright Pink to Dark Green)
    for i in range(speed):
        r = int(255 - (i * 10))
        g = int(0 + (i * 5))  # these numbers are trial for ex 7 was too much 
        b = int(80 - (i * 4)) # and less than 4 (blue) was less so g settled w 5 (6 is ok too)
        led[0] = (r, g, b)   
        time.sleep(speed / 10) 
    
    # Summer (Dark Green to Warm Orange)
    # (0,128,0) is bright green what i tried to achieve in prev loop- works well with speed =20
    for i in range(speed):
        r = int(0 + (i * 12))  # trial, 10 was less 12 felt nice 15 was too quick
        g = int(128 + (i * 2))
        b = int(0)
        led[0] = (r, g, b)
        time.sleep(speed / 10)

    # Autumn (Warm Orange) (255, 69,0)
    for i in range(speed):
        r = int(255)
        g = int(69 + (i * 3))
        b = int(0)
        led[0] = (r, g, b)    
        time.sleep(speed / 10)
    
    # Winter (Warm Orange to Snow White) 
    # after moving from 255,69,0 i tried to stop at 255, 138,0 in prev loop and then go to 255,255,255
    for i in range(speed):
        r = int(255)
        g = int(138 + (i * 3))
        b = int(0)
        led[0] = (r, g, b)
        time.sleep(speed / 10)
        
    # snow white 255 255 255
    for i in range(speed):
        r = int(255 - (i * 6))
        g = int(138 - (i * 3))
        b = int(0 + (i * 12))
        led[0] = (r, g, b)
        time.sleep(speed / 10)
        
    break

