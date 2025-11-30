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

keyboard.col_pins = (col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col16,col17,col18,col19,col20,col21,col22,col23) 
keyboard.row_pins = (row1,row2,row3,row4,row5,row6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [XXXXX],[KC.ESCAPE],[XXXXX],[KC.F1],[KC.F2],[KC.F3],[KC.F4],[XXXXX],[KC.F5],[KC.F6],[KC.F7],[KC.F8],[KC.F9],[KC.F10],[KC.F11],[KC.F12],[KC.PSCREEN],[KC.SCROLLLOCK],[KC.PAUSE],[XXXXX],[XXXXX],[XXXXX],[XXXXX]
    [KC.N1],[KC.ZKHK],[KC.N1],[KC.N2],[KC.N3],[KC.N4],[KC.N5],[KC.N6],[KC.N7],[KC.N8],[KC.N9],[KC.N0],[KC.MINUS],[KC.PLUS],[KC.BSPACE],[XXXXX],[KC.INSERT],[KC.HOME],[KC.PGUP],[KC.NLCK],[KC.KP_SLASH],[KC.PAST],[KC.PMNS]
    [KC.N2],[KC.TAB],[KC.Q],[KC.W],[KC.E],[KC.R],[KC.T],[KC.Y],[KC.D],[KC.I],[KC.O],[KC.P],[KC.LBRACKET],[LBRACKET],[KC.SLASH],[XXXXX],[KC.DELETE],[KC.END],[KC.PGDOWN],[KC.KP_7],[KC.P8],[KC.P9],[KC.PPLS]
    [KC.N3],[KC.CAPS],[KC.A],[KC.S],[KC.D],[KC.F],[KC.G],[KC.H],[KC.J],[KC.K],[KC.L],[KC.SCOLON],[KC.AT],[XXXXX],[KC.ENTR][XXXXX],[XXXXX],[XXXXX],[XXXXX],[KC.KP_4],[KC.P5],[KC.P6],[XXXXX]
    [KC.N4],[KC.LSHIFT],[KC.Z],[KC.X],[KC.C],[KC.V],[KC.B],[KC.N],[KC.M],[KC.COMM],[KC.DOT],[XXXXX],[XXXXX],[KC.QUES],[XXXXX],[KC.RSHIFT],[XXXXX],[XXXXX],[KC.UP],[XXXXX],[KC.KP_1],[KC.P2],[KC.P3],[KC.PENT]
    [KC.N5],[KC.LCTRL],[KC.LGUI],[KC.LALT],[XXXXX],[XXXXX],[KC.SPACE],[XXXXX],[XXXXX][KC.RALT],[KC.RGUI],[XXXXX],[XXXXX],[XXXXX],[KC.RCTRL][XXXXX],[KC.LEFT],[KC.DOWN],[KC.RIGHT],[KC.KP_0],[XXXXX],[XXXXX]
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