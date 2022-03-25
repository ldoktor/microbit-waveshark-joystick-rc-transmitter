let vpred_vzad = 0
let levo_pravo = 0
radio.setGroup(1)
WSJoyStick.JoyStickInit()
basic.forever(function () {
    levo_pravo = Math.map(pins.analogReadPin(AnalogPin.P1), 0, 1023, -100, 100)
    vpred_vzad = Math.map(pins.analogReadPin(AnalogPin.P2), 0, 1023, -100, 100)
    radio.sendValue("right", vpred_vzad - levo_pravo)
    radio.sendValue("left", vpred_vzad + levo_pravo)
})
