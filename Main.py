### START
print("Starting")
## Import Board 
import board

## Import CircuitPython Junk
import time
import neopixel
import displayio

## Import KMK
from kmk.kmk_keyboard import KMKKeyboard

## Import Keys
from kmk.keys import KC, make_key

## Import Scanners
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic
from kmk.scanners.keypad import ShiftRegisterKeys

## Import Modules
from kmk.modules.tapdance import TapDance
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.oneshot import OneShot
from kmk.modules.layers import Layers

## Import Handlers
from kmk.handlers.sequences import send_string
from kmk.handlers.sequences import simple_key_sequence

## Import Extensions
#from kmk.extensions.statusled import statusLED
#from kmk.extensions.led import LED
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.lock_status import LockStatus

## Define Variables for RGB
rgb_pixel_pin = board.NEOPIXEL
num_pixels = 1
rgb_order=(1, 0, 2)


## Redefine Keyboard Class via Shift Registers
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
            value_to_latch=True, 
            value_when_pressed=False,
            interval=0.02,
            max_events=64
        )
    coord_mapping = [
    20, 21, 22,                              46, 45, 44,
    14, 13, 19, 18, 16, 23,      47, 40, 42, 43, 37, 38,
     7, 11, 12, 17,  8, 15,      39, 32, 41, 36, 35, 31,
     6,  5, 10,  9,  4,  3,      27, 28, 33, 34, 29, 30,
                 0,  1,  2,      26, 25, 24,
    ]
    rgb_ext = RGB(
        num_pixels=num_pixels, 
        pixel_pin=rgb_pixel_pin,
        rgb_order=rgb_order,
        hue_default=85,
        sat_default=255,
        val_default=0,
    )
#    print(coord_mapping) ## Show me Coordinate Mapping


### DEF BARE KEYBOARD
keyboard = _KMKKeyboard()

### Module Configuration
## TAPDANCE Init
tapdance = TapDance()
tapdance.tap_time = 500
keyboard.modules.append(tapdance)

## ONESHOT Init
oneshot = OneShot()
keyboard.modules.append(oneshot)

## COMBO Init
combos = Combos()
keyboard.modules.append(combos)

## LAYERS Init
keyboard.modules.append(Layers())

## LOCKSTATUS Init
# Work in progress #
# locks = LockStatus()
# keyboard.extensions.append(locks)

# locks.get_num_lock()
# locks.get_caps_lock()
# locks.get_scroll_lock()
# locks.get_compose()
# locks.get_kana()


## RGB Init
# Don't need this anymore? #

## NEOPIXEL STATUSES
RED = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(0,255,5)
YELLOW = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(42,255,5)
GREEN = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(85,255,5)
AQUA = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(128,255,5)
BLUE = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(171,255,5)
PURPLE = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(213,255,5)
BLANK = lambda *args, **kwargs: keyboard.rgb_ext.set_hsv_fill(0,255,0)


### KEYMAPPING
_____ = KC.TRNS ## This seems to be common


## TAPDANCE MACROS
MACRO1 = KC.TD(
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
    KC.DOUBLE_QUOTE,  # Tap once for """
    KC.GRAVE,  # Tap twice for "`"
    KC.TILDE,  # Tap three times for "~"
)
CTRL_MACRO = KC.TD(
    KC.OS(KC.LCTL,tap_time=None),  # Tap once for "LCTL"
    KC.OS(KC.LALT,tap_time=None),  # Tap twice for "LALT"
    KC.OS(KC.LWIN,tap_time=None),  # Tap three times for "LWIN"
)


### SEQUENCES


#ComboA = simple_key_sequence(
#    (KC.DEBUG, 
#    KC.RGB_TOG)
#)

##ChangeL1= simple_key_sequence(
#keyboard#    
##  keyboard.pixels.set_hsv_fill(42, 255, 5),
## Change RGB Status
##)    



LAYER_1 = KC.TG(1)
LAYER_1.after_press_handler(BLUE)
LAYER_1.after_release_handler(BLANK)




### HANDLERS
# Honestly, I don't have another place for this at the moment.
# needed as reference for adding effects to macros
'''

before_press_handler
after_press_handler
on_press
on_release
before_release_handler
after_release_handler

'''


'''
## Define Keys
make_key(
    names=('TDEBUG',)
)


##Define Combos

Sequence((KC.DEBUG, KC.RGB_TOG) KC.TDEBUG, timeout=500, per_key_timeout=False),
'''

# Define Keymap
'''
    20, 21, 22,                              46, 45, 44,
    14, 13, 19, 18, 16, 23,      47, 40, 42, 43, 37, 38,
     7, 11, 12, 17,  8, 15,      39, 32, 41, 36, 35, 31,
     6,  5, 10,  9,  4,  3,      27, 28, 33, 34, 29, 30,
                 0,  1,  2,      26, 25, 24,
'''
keyboard.keymap = [
## NORMAL KEYMAP
    [
    KC.ESC,     KC.DEBUG, KC.LALT(KC.TAB),                                    LAYER_1,  KC.PRINT_SCREEN,    CBRACKET_M, 
    KC.TAB,     KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,       KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,       OBRACKET_M, 
    CTRL_MACRO, KC.A,   KC.S,   KC.D,   KC.F,   KC.G,       KC.H,   KC.J,   KC.K,   KC.L,   QUOTE_M,    KC.ENTER,
    KC.LSHIFT,  KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,       KC.N,   KC.M,   COMMA_M,KC.DOT, KC.SLASH,   KC.RSHIFT,
                        KC.BACKSPACE,    KC.SPACE,   KC.ENTER,   KC.LALT,    KC.LCTL,    KC.LWIN,
    ],

### Numbers
    [
    KC.TRNS,  KC.TRNS,  KC.TRNS,                                                            KC.TRNS,  KC.TRNS,  KC.NO,
    KC.TRNS,  KC.NO,  KC.N7,  KC.N8,  KC.N9,  KC.SLASH,             KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
    KC.NO,  KC.NO,  KC.N4,  KC.N5,  KC.N6,  KC.DOT,                 KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
    KC.NO,  KC.NO,  KC.N1,  KC.N2,  KC.N3,  KC.N0,                  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
                            KC.TRNS,    KC.SPACE,   KC.ENTER,   KC.LALT,    KC.LCTL,    KC.LWIN,
    ],

### Null Set Keymap
    [
    KC.TRNS,  KC.TRNS,  KC.TRNS,                                                             KC.TRNS,  KC.TRNS,  KC.NO,
    KC.NO,  KC.NO,  KC.HOME, KC.UP,  KC.END,     KC.PGUP,            KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
    KC.NO,  KC.NO,  KC.LEFT, KC.DOWN,KC.RIGHT,   KC.PGDOWN,           KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
    KC.NO,  KC.NO,  KC.NO,   KC.NO,  KC.NO,      KC.NO,              KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
                             KC.TRNS,  KC.TRNS,  KC.TRNS,            KC.NO,  KC.NO,  KC.NO,
    ],

'''
### Null Set Keymap
    [
    KC.TRNS,  KC.TRNS,  KC.TRNS                                                         KC.NO,  KC.TRNS,  KC.NO,
    KC.TRNS,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,            KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
    KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,              KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
    KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,              KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.NO,
                            KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.NO,  KC.NO,  KC.NO,
    ],
'''
]

print("Started")

# Debug
keyboard.debug_enabled = True


## Main Loop
if __name__ == '__main__':
    keyboard.go()
