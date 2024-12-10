from .Scale2D import Scale2D
from .BaseObject import BaseObject;

class DrawableObject(BaseObject):
    """실제로 그려지는 있는 객체입니다."""

    DisplayedWidth:int
    """실제 렌더링 되는 너비"""
    DisplayedHeight:int
    """실제 렌더링 되는 높이"""

    Opacity:int
    """투명도 (0은 완전 투명, 255는 불투명)"""
    Scale:Scale2D
    """스케일입니다."""
    ScaleX:float
    """너비 배율 """
    ScaleY:float
    """높이 배율 """
    # MouseOver:bool
    # """마우스에 닿았는지에 대한 여부  (객체 전용)"""

    # def Overlap(self,other) -> bool:
    #     """다른 객체와 겹침 여부  (객체 전용)"""
    #     pass

from JyunrcaeaFramework import DrawableObject;