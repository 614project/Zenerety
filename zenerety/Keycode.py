from enum import Enum
import re
from winreg import EnumValue

class Keycode(Enum):
    """키코드. 키 입력 관련 이벤트는 이 자료형으로 주어집니다."""
    UNKNOWN:int
    RETURN:int
    ESCAPE:int
    BACKSPACE:int
    TAB:int
    SPACE:int
    EXCLAIM:int
    QUOTEDBL:int
    HASH:int
    PERCENT:int
    DOLLAR:int
    AMPERSAND:int
    QUOTE:int
    LEFTPAREN:int
    RIGHTPAREN:int
    ASTERISK:int
    PLUS:int
    COMMA:int
    MINUS:int
    PERIOD:int
    SLASH:int
    _0:int
    _1:int
    _2:int
    _3:int
    _4:int
    _5:int
    _6:int
    _7:int
    _8:int
    _9:int
    COLON:int
    SEMICOLON:int
    LESS:int
    EQUALS:int
    GREATER:int
    QUESTION:int
    AT:int
    LEFTBRACKET:int
    BACKSLASH:int
    RIGHTBRACKET:int
    CARET:int
    UNDERSCORE:int
    BACKQUOTE:int
    A:int
    B:int
    C:int
    D:int
    E:int
    F:int
    G:int
    H:int
    I:int
    J:int
    K:int
    L:int
    M:int
    N:int
    O:int
    P:int
    Q:int
    R:int
    S:int
    T:int
    U:int
    V:int
    W:int
    X:int
    Y:int
    Z:int
    CAPSLOCK:int
    F1:int
    F2:int
    F3:int
    F4:int
    F5:int
    F6:int
    F7:int
    F8:int
    F9:int
    F10:int
    F11:int
    F12:int
    PRINTSCREEN:int
    SCROLLLOCK:int
    PAUSE:int
    INSERT:int
    HOME:int
    PAGEUP:int
    DELETE:int
    END:int
    PAGEDOWN:int
    RIGHT:int
    LEFT:int
    DOWN:int
    UP:int
    NUMLOCKCLEAR:int
    KP_PLUS:int
    NUM_ENTER:int
    NUM_1:int
    NUM_2:int
    NUM_3:int
    NUM_4:int
    NUM_5:int
    NUM_6:int
    NUM_7:int
    NUM_8:int
    NUM_9:int
    NUM_0:int
    POWER:int
    LCTRL:int
    LSHIFT:int
    LALT:int
    LGUI:int
    RCTRL:int
    RSHIFT:int
    RALT:int
    RGUI:int
    BrightnessDown:int
    BrightnessUp:int

from JyunrcaeaFramework import Keycode;

# FUCK YOU PYTHONNET
# WHY CONVERT INT TO STRING IN ENUM?

# for name in dir(Keycode):
#     if name.startswith("__") or name.endswith("__"):
#         continue
#     enum_value = getattr(Keycode, name);
#     if len(str(enum_value)) == 1:
#         globals()[name] = int(enum_value);
