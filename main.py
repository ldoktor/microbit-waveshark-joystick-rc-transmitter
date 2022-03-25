vpred_vzad = 0
levo_pravo = 0
radio.set_group(1)
WSJoyStick.joy_stick_init()

def on_forever():
    global levo_pravo, vpred_vzad
    levo_pravo = Math.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, -100, 100)
    vpred_vzad = Math.map(pins.analog_read_pin(AnalogPin.P2), 0, 1023, -100, 100)
    radio.send_value("right", vpred_vzad - levo_pravo)
    radio.send_value("left", vpred_vzad + levo_pravo)
basic.forever(on_forever)
