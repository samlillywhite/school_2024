import time
import board
from adafruit_neotrellis.neotrellis import NeoTrellis
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.program_change import ProgramChange

# create the i2c object for the trellis
i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# create the trellis
trellis = NeoTrellis(i2c_bus)
# Initialize MIDI output on the USB port
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# Set the brightness value (0 to 1.0)
trellis.brightness = 0.5

# some color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# Define the notes for a C Major chord (MIDI note numbers)
c4 = 60  # C4
db4 = 61
d4 = 62
eb4 = 63
e4 = 64  # E4
f4 = 65
gb4 = 66
g4 = 67  # G4
ab4 = 68
a4 = 69
Bb4 = 70
B4 = 71
c5 = 72
db5 = 73
d5 = 74
eb5 = 75



# this will be called when button events are received
def blink(event):
    global c4
    global db4
    global d4
    global eb4
    global e4
    global f4
    global gb4
    global g4
    global ab4
    global a4
    global Bb4
    global B4
    global c5
    global db5
    global d5
    global eb5
    # turn the LED on when a rising edge is detected
    if event.edge == NeoTrellis.EDGE_RISING:
        trellis.pixels[event.number] = CYAN
        # Send NoteOn messages for each note in the chord
        # midi.send(NoteOn(c4, 120,))  # NoteOn for C4 with velocity 120
        # midi.send(NoteOn(e4, 120))  # NoteOn for E4 with velocity 120
        # midi.send(NoteOn(g4, 120))  # NoteOn for G4 with velocity 120
        if event.number == 0:
            midi.send(ProgramChange(127))
            midi.send(NoteOn(c4, 120))
        elif event.number == 1:    
            midi.send(NoteOn(db4, 120))
        elif event.number == 2:    
            midi.send(NoteOn(d4, 120))
        elif event.number == 3:
            midi.send(NoteOn(eb4, 120))
        elif event.number == 4:    
            midi.send(NoteOn(e4, 120))
        elif event.number == 5:    
            midi.send(NoteOn(f4, 120))
        elif event.number == 6:
            midi.send(NoteOn(gb4, 120))
        elif event.number == 7:    
            midi.send(NoteOn(g4, 120))
        elif event.number == 8:    
            midi.send(NoteOn(ab4, 120))
        elif event.number == 9:
            midi.send(NoteOn(a4, 120))
        elif event.number == 10:    
            midi.send(NoteOn(Bb4, 120))
        elif event.number == 11:    
            midi.send(NoteOn(B4, 120))
        elif event.number == 12:    
            midi.send(NoteOn(c5, 120))
        elif event.number == 13:
            midi.send(NoteOn(db5, 120))
        elif event.number == 14:    
            midi.send(NoteOn(d5, 120))
        elif event.number == 15:    
            midi.send(NoteOn(eb5, 120))
        
        # Hold the chord for 2 seconds
        # time.sleep(2)

    # turn the LED off when a falling edge is detected
    elif event.edge == NeoTrellis.EDGE_FALLING:
        trellis.pixels[event.number] = OFF
        # Send NoteOff messages for each note in the chord
        # midi.send(NoteOff(c4, 0,))  # NoteOff for C4
        # midi.send(NoteOff(e4, 0))  # NoteOff for E4
        # midi.send(NoteOff(g4, 0))  # NoteOff for G4
        if event.number == 0:
            midi.send(NoteOff(c4, 120))
        elif event.number == 1:    
            midi.send(NoteOff(db4, 120))
        elif event.number == 2:    
            midi.send(NoteOff(d4, 120))
        elif event.number == 3:
            midi.send(NoteOff(eb4, 120))
        elif event.number == 4:    
            midi.send(NoteOff(e4, 120))
        elif event.number == 5:    
            midi.send(NoteOff(f4, 120))
        elif event.number == 6:
            midi.send(NoteOff(gb4, 120))
        elif event.number == 7:    
            midi.send(NoteOff(g4, 120))
        elif event.number == 8:    
            midi.send(NoteOff(ab4, 120))
        elif event.number == 9:
            midi.send(NoteOff(a4, 120))
        elif event.number == 10:    
            midi.send(NoteOff(Bb4, 120))
        elif event.number == 11:    
            midi.send(NoteOff(B4, 120))
        elif event.number == 12:    
            midi.send(NoteOff(c5, 120))
        elif event.number == 13:
            midi.send(NoteOff(db5, 120))
        elif event.number == 14:    
            midi.send(NoteOff(d5, 120))
        elif event.number == 15:    
            midi.send(NoteOff(eb5, 120))

for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # cycle the LEDs on startup
    trellis.pixels[i] = PURPLE
    time.sleep(0.05)

for i in range(16):
    trellis.pixels[i] = OFF
    time.sleep(0.05)

while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 millisecons or so
    time.sleep(0.02)











