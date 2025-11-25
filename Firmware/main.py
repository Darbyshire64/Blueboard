print("KMK Starting")

# Get KMK Modules
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Get Exstentions for Other Components
from kmk.extensions.display import Display, SSD1306
from kmk.extensions.display.displays import OledDisplay
from kmk.extensions.modules.encoder import EncoderHandler

encoders = EncoderHandler()

encoders.pins = (
    (board.D2, board.D3),   # Encoder 1: pinA, pinB
)

encoders.map = (
    ((KC.VOLD, KC.VOLU),),  # CCW turns, CW turns
)

keyboard.extensions.append(encoders)


keyboard = KMKKeyboard()

#Use OLED
oled = SSD1306(
    i2c=board.I2C(),     # Use your board’s I2C object
    width=128,
    height=32,
)


display = Display(oled)
keyboard.extensions.append(display)


## KMK Config
keyboard.col_pins = (board.GP0,)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Key Map
#keyboard.keymap = [
#    [KC.A,]
#]

## Init
if __name__ == '__main__':
    keyboard.go()