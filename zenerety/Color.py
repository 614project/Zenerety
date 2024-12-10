class Color:
    """색을 저장하는 클래스입니다."""
    def __init__(self,red:int = 255,green:int = 255, blue:int = 255, alpha:int = 255) -> None:
        """RGBA 순으로 0~255 사이의 값을 지정하세요"""
        pass

    Red:int
    """빨간색"""
    Green:int
    """초록색"""
    Blue:int
    """파란색"""
    Alpha:int
    """투명도"""

from JyunrcaeaFramework import Color;