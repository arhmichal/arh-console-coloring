import enum

def encode(code): return f"\033[{code}m"

def decode(code): return code[3:-1]

def enum2str(e): return e.value

class Format(enum.Enum):
    Reset=encode(0)
    Normal=encode(0)
    Default=encode(0)
    Bold=encode(1)
    Light=encode(1)
    Dark=encode(2)
    Italic=encode(3)
    Underline=encode(4)
    Blink=encode(5)
    # Dunno=encode(6)
    Inverted=encode(7)
    Invisible=encode(8)
    Strike_Through=encode(9)
    Double_Underline=encode(21) # 0x15
    Overline=encode(53) # 0x35

class Color(enum.Enum):
    Black=encode(30)
    Red=encode(31)
    Green=encode(32)
    Yellow=encode(33)
    Blue=encode(34)
    Purple=encode(35)
    Cyan=encode(36)
    Grey=encode(37)
    # Dunno=encode(38) # 0x26
    White=encode(39)

class BgColor(enum.Enum):
    Black=encode(40)
    Red=encode(41)
    Green=encode(42)
    Yellow=encode(43)
    Blue=encode(44)
    Purple=encode(45)
    Cyan=encode(46)
    Grey=encode(47)

def color_this(text, *args) -> str:
    stringified = list(map(enum2str, args))
    return "".join(stringified) + text + encode(0)

print(color_this("ala"))
print(color_this("ala", BgColor.Red, Format.Bold))
