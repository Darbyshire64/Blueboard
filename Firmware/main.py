print("KMK Starting")

#Base Modules
import time

# Get KMK Modules
import board, busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Get Exstentions for Other Components
from kmk.extensions.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, SSD1306
from adafruit_mcp230xx.mcp23017 import MCP23017

print("[STAUTS] Import Done")

## Start Main Code
print("[STAUTS] Expander Init")

i2c = busio.I2C(board.SCL, board.SDA)


mcp1 = MCP23017(i2c, address=0x20)
mcp2 = MCP23017(i2c, address=0x21)

# EXPANDER 1 - COL
col1 = mcp1.get_pin(0)
col2 = mcp1.get_pin(1)
col3 = mcp1.get_pin(2)
col4 = mcp1.get_pin(3)
col5 = mcp1.get_pin(4)
col6 = mcp1.get_pin(5)
col7 = mcp1.get_pin(6)
col8 = mcp1.get_pin(7)
col9 = mcp1.get_pin(8)
col10 = mcp1.get_pin(9)
col11 = mcp1.get_pin(10)
col12 = mcp1.get_pin(11)
col13 = mcp1.get_pin(12)
col14 = mcp1.get_pin(13)
col15 = mcp1.get_pin(14)
col16 = mcp1.get_pin(15)
col17 = mcp1.get_pin(16)

# EXPANDER 2 - COL
col18 = mcp2.get_pin(0)
col19 = mcp2.get_pin(1)
col20 = mcp2.get_pin(2)
col21 = mcp2.get_pin(3)
col22 = mcp2.get_pin(4)
col23 = mcp2.get_pin(5)


# EXPANDER 2 - ROW
row1 = mcp2.get_pin(8)
row2 = mcp2.get_pin(9)
row3 = mcp2.get_pin(10)
row4 = mcp2.get_pin(11)
row5 = mcp2.get_pin(12)
row6 = mcp2.get_pin(13)

print("[STAUTS] Expander Done")
print("[STAUTS] Keyboard Init")

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,) #NOT Done until Expander Init
keyboard.row_pins = (board.GP1,) # Not Done until Expander Init
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,]
]

print("[STAUTS] Keyboard Done")
print("[STAUTS] Encoder Init")


encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]


# Regular GPIO Encoder
encoder_handler.pins = (
    (board.D8, board.D7, board.D1), # encoder #1 
    (board.D11, board.D10, board.D0) # encoder #2
)


encoder_handler.map = [ 
    ( KC.VOLD, KC.VOLU, KC.MUTE),
    (Zoom_out, Zoom_in, KC.NO),
]

print("[STAUTS] Encoder Done")
print("[STAUTS] OLED Init")


oled = SSD1306(
    i2c=board.I2C(),
    width=128,
    height=32
)

display = Display(oled)
keyboard.extensions.append(display)

def log(text):
    display.show_text(text)
    print(text)

log("Hello World!!!")
time.sleep(.5)


log("[STAUTS] OLED Done")
log("[STAUTS] Initialzing")
    

if __name__ == "__main__":
    keyboard.go()