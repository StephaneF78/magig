strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)

def on_forever():
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.pause(500)
basic.forever(on_forever)
