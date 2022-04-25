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
from kmk.modules.combos import Chord, Combos
from kmk.modules.oneshot import OneShot

class _KMKKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = ShiftRegisterKeys(
            # require arguments:
            clock=board.D3,
            data=board.D4,
            latch=board.D2,
            key_count=48,
            # optional arguments with defaults:
            value_to_latch=True, # 74HC165: True, CD4021: False
            value_when_pressed=False,
            interval=0.02,
            max_events=64
        )

## DEF BARE KEYBOARD
keyboard = _KMKKeyboard()

## MODULES
### TAPDANCE
tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)

### ONESHOT
oneshot = OneShot()
keyboard.modules.append(oneshot)

### COMBOS
combos = Combos()
keyboard.modules.append(combos)

### NEOPIXEL INIT
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
color = (0,0,0)
pixel.brightness = 1
pixel.fill(color)
 
## TAPDANCE MACROS
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
COMMA_M = KC.TD(
    KC.COMMA,  # Tap once for ","
    KC.SEMICOLON,  # Tap twice for ";"
    KC.COLON, # Tap three times for ":"
)
OBRACKET_M = KC.TD(
    KC.LEFT_PAREN,  # Tap once for "("
    KC.LBRACKET,  # Tap twice for "["
    KC.LEFT_CURLY_BRACE,
    KC.LEFT_ANGLE_BRACKET,
)
CBRACKET_M = KC.TD(
    KC.RIGHT_PAREN,  # Tap once for "("
    KC.RBRACKET,  # Tap twice for "["
    KC.RIGHT_CURLY_BRACE,
    KC.RIGHT_ANGLE_BRACKET,
)
QUOTE_M = KC.TD(
    KC.QUOTE,  # Tap once for "'"
    KC.GRAVE,  # Tap twice for "`"
    KC.TILDE,  # Tap three times for "~"
)
CTRL_MACRO = KC.TD(
    KC.OS(KC.LCTL,tap_time=None),  # Tap once for "LCTL"
    KC.OS(KC.LALT,tap_time=None),  # Tap twice for "LALT"
    KC.OS(KC.LWIN,tap_time=None),  # Tap three times for "LWIN"
)

keyboard.keymap = [
## NORMAL KEYMAP
    [KC.BACKSPACE,KC.SPACE,KC.ENTER,KC.B,KC.V,KC.Z,KC.LSHIFT,CTRL_MACRO,
    KC.F,KC.C,KC.X,KC.A,KC.S,KC.Q,KC.TAB,KC.G,
    KC.R,KC.D,KC.E,KC.W,KC.N1,KC.N5,KC.N6,KC.T,

    KC.LALT,KC.LCTL,KC.LWIN,KC.N,KC.M,KC.SLASH,KC.RSHIFT,KC.ENTER,
    KC.J,COMMA_M, KC.DOT, QUOTE_M, KC.L, OBRACKET_M, CBRACKET_M, KC.H,
    KC.U, KC.K, KC.O, KC.P, KC.SCROLL_LOCK, KC.PRINT_SCREEN, KC.PAUSE, KC.Y,
            ],
]
print("Started")
keyboard.debug_enabled = False

if __name__ == '__main__':
    keyboard.go()
    pixel.fill(color)
