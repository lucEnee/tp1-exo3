x = 0
x2 = 0
y = 0
intensite = 0

def on_forever():
    global x, y, intensite
    x = randint(0, 4)
    x = randint(0, 4)
    y = 0
    intensite = 255
    for index in range(8):
        led.plot(x, y)
        basic.pause(200)
        y += 1
        intensite += -40
        led.set_brightness(intensite)
        led.unplot(x, y - 3)
    for index2 in range(8):
        led.plot(x, y)
        basic.pause(200)
        y += 1
        intensite += -40
        led.set_brightness(intensite)
        led.unplot(x, y - 3)
basic.forever(on_forever)
