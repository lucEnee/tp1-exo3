let x = 0
let y = 0
let intensite = 0
basic.forever(function () {
    x = randint(0, 4)
    y = -1
    intensite = 255
    for (let index = 0; index < 8; index++) {
        led.plot(x, y)
        basic.pause(200)
        y += 1
        intensite += -40
        led.setBrightness(intensite)
        led.unplot(x, y - 3)
    }
})
