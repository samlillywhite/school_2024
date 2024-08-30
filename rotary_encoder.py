import time
import board
import busio
import digitalio
from adafruit_ht16k33 import segments

# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create the display object
display = segments.Seg7x4(i2c)

# Play with displaying specific parts of the display
display.fill(0)
display.blink_rate = 0
display.brightness = .5
#display.marquee("sal is cool ", delay = .5, loop=True)
#display.set_digit_raw(0, 0x06)
#display.set_digit_raw(1, 0x3f)
#display.set_digit_raw(2, 0x3f)
#display.set_digit_raw(3, 0x3f)
counter = 0

# Create digital input with pull-up resistor on pin D10
# for break beam sensor.
break_beam = digitalio.DigitalInOut(board.D11)
break_beam.direction = digitalio.Direction.INPUT
break_beam.pull = digitalio.Pull.UP

if break_beam.value:
    state = 'open'
else:
    state = 'closed'

# Main loop runs forever and prints a message once a second
# while the sensor is blocked/broken.
while True:
    if not break_beam.value:
        
        if state == 'open':
            counter += 1
            state = 'closed'
        # Break beam input is at a low logic level, i.e. broken!
            display.fill(0)
            display.print(counter)

    if break_beam.value:
        state = 'open'
            

