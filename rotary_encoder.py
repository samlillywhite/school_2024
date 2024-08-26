import time

import board
import digitalio
counter = 0


# Create digital input with pull-up resistor on pin D10
# for break beam sensor.
break_beam = digitalio.DigitalInOut(board.D10)
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
            print(counter)

    if break_beam.value:
        state = 'open'
            
    time.sleep(0.01)  # Delay for 1 second and repeat again.

