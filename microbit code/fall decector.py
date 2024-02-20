from microbit import *
radio.set_transmit_power(7)
radio.set_transmit_serial_number(False)
radio.set_group(34)

def on_forever():
    serial.write_line("")
    serial.write_number(input.acceleration(Dimension.STRENGTH))
    if input.acceleration(Dimension.STRENGTH) >= 7000:
        radio.send_number(2)
    elif input.acceleration(Dimension.STRENGTH) >= 4000:
        radio.send_number(1)
basic.forever(on_forever)