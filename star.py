import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[5] = (10,0,0)
