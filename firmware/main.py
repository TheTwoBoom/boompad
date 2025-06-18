# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306

# Replace SCL and SDA according to your hardware configuration.
i2c_bus = busio.I2C(board.GP7, board.GP6)

rgb = RGB(pixel_pin=board.GP0, num_pixels=4)

driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(EncoderHandler())
keyboard.extensions.append(rgb)

keyboard.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP28, board.GP29)
rollover_cols_every_rows = 4
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.T, KC.B, KC.O, KC.RETURN],
    [KC.W, KC.M, KC.SPACE, KC.ENTER],
]

# For all display types
display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=30, # time in seconds to reduce screen brightness
    dim_target=0.3, # set level for brightness decrease
    off_time=120, # time in seconds to turn off screen
    powersave_dim_time=20, # time in seconds to reduce screen brightness
    powersave_dim_target=0.3, # set level for brightness decrease
    powersave_off_time=60, # time in seconds to turn off screen
)

display.entries = [
    TextEntry(text="This actually works", x=0, y=0),
    TextEntry(text="BoomPad v0.1", x=0, y=12),
]
keyboard.extensions.append(display)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()