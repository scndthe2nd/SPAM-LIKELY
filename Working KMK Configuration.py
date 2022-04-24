print("Starting")
 
import board
 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import ShiftRegisterKeys
import time
import neopixel
from kmk.handlers.sequences import send_string
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation
 
class _KMKKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = ShiftRegisterKeys(
            # require arguments:
            clock=board.D3,
            data=board.D4,
            latch=board.D2,
            key_count=24,
            # optional arguments with defaults:
            value_to_latch=True, # 74HC165: True, CD4021: False
            value_when_pressed=False,
            interval=0.02,
            max_events=64
        )
keyboard = _KMKKeyboard()
tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)
 
MACRO1 = KC.TD(
    KC.N1,  # Tap once for "a"
    KC.N2,  # Tap twice for "b"
    # Tap three times to send a raw string via macro
    send_string('macros in a tap dance? I think yes'),
)

MACRO2 = KC.TD(
    KC.N1,  # Tap once for "a"
    KC.N2,  # Tap twice for "b"
    # Tap three times to send a raw string via macro
    send_string('macros in a tap dance? I think yes'),
)
MACRO3 = KC.TD(
    KC.N1,  # Tap once for "a"
    KC.N2,  # Tap twice for "b"
    # Tap three times to send a raw string via macro
    send_string('macros in a tap dance? I think yes'),
)
MACRO4 = KC.TD(
    KC.N1,  # Tap once for "a"
    KC.N2,  # Tap twice for "b"
    # Tap three times to send a raw string via macro
    send_string('macros in a tap dance? I think yes'),
)
MACRO5 = KC.TD(
    KC.N1,  # Tap once for "a"
    KC.N2,  # Tap twice for "b"
    # Tap three times to send a raw string via macro
    send_string('macros in a tap dance? I think yes'),
)
MACRO6 = KC.TD(
    KC.N1,  # Tap once for "a"
    KC.N2,  # Tap twice for "b"
    # Tap three times to send a raw string via macro
    send_string('macros in a tap dance? I think yes'),
)

keyboard.keymap = [
    [KC.BACKSPACE,KC.SPACE,KC.ENTER,KC.B,KC.V,KC.Z,KC.LSHIFT,KC.TAB,
    KC.F,KC.C,KC.X,KC.A,KC.S,KC.Q,KC.TAB,KC.G,
    KC.R,KC.D,KC.E,KC.W,KC.N1,KC.N5,KC.N6,KC.T,
        ],
]


'''
##Keymap L0
[
MACRO1, MACRO2, MACRO3,                                     KC.PS, MACRO6, KC.ESC,
KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T,           KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BackSlash,
MACRO4, KC.A, KC.S, KC.D,KC.F,KC.G,             KC.H, KC.J, KC.K, KC.L, KC.Colon, KC.Enter,
KC.SHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,              KC.N, KC.M, KC.Comma, KC.Period, KC.Slash, KC.SHIFT
                KC.BACKSPACE, KC.SPACE, MACRO5  KC.Meta, KC.LCtl, KC.Alt
]

## Keymap L1
[
MACRO1, MACRO2, MACRO3,                                                 KC.PS, MACRO6, KC.ESC,
KC.TAB, -----, KC.N7, KC.N8, KC.N9, KC.PLUS,    KC.PGUP, KC.HOME, KC.INS, KC.OP, KC.CP, -----,
MACRO4, -----, KC.N4, KC.N5,KC.N6,KC.MINUS,     KC.PGDN, KC.END, KC.DEL, -----, -----, KC.Enter,
KC.SHIFT, -----,KC.N1,KC.N2,KC.N3,KC.DOT,       -----, -----, -----, -----, -----, KC.SHIFT,
            KC.BACKSPACE, KC.SPACE, MACRO5      KC.META, KC.LCTL, KC.ALT
]

]


### Register Keymap
[
21  22  23                              46  45  44
15  14  20  19  17  16      39  40  42  43  37  38
0   12  13  18  9   8       31  32  41  36  35  23
7   6   11  10  5   4       27  28  33  34  29  30
            1   2   3       26  25  24          
]
'''





keyboard.debug_enabled = True
 
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
 
pixel.brightness = 0.01
 
 
if __name__ == '__main__':
    keyboard.go()

while True:
    pixel.fill((1,1,1))
