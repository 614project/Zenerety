from .BaseObject import BaseObject
from .Color import Color;

class Box(BaseObject):
    """직사각형 객체입니다."""

    Color:Color;
    """채워질 색입니다."""
    Opacity:int
    """투명도입니다. (0은 투명 255는 불투명)."""

    def __init__(self,width:int = 0, height:int = 0, color:Color = None):
        """직사각형 객체를 생성합니다."""

from ZeneretyEngine import Box;