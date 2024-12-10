class Texture:
    """텍스쳐"""

    def __init__(self, path:str):
        """파일로부터 텍스쳐를 로드합니다."""

        self.Width:int;
        """텍스쳐의 너비"""
        self.Height:int;
        """텍스쳐의 높이"""
        self.Opacity:int;
        """텍스쳐의 투명도"""

    def SetRenderRange(self,x:int,y:int,width:int,height:int):
        """텍스쳐의 특정 범위만을 그리도록 설정"""

from ZeneretyEngine import Texture;