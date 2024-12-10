from .Color import Color;
from .DrawableObject import DrawableObject

class TextBox(DrawableObject):
    def __init__(self, content:str, size:int, color:Color, font):
        self.AbsoluteWidth:int;
        """실제 렌더링 너비"""
        self.AbsoluteHeight:int;
        """실제 렌더링 높이"""
        self.Rotation:float;
        """회전값 (가운데 중심, 육십분법)"""

        self.prepare:function|None;
        """장면이 시작될때 가장 먼저 호출되는 함수입니다."""
        self.release:function|None;
        """장면이 종료될때 호출되는 함수입니다."""
        self.update:function|None;
        """매 프레임마다 호출되는 함수입니다. 파라미터에 이전 프레임과의 시간차를 밀리초로 제공합니다."""
        self.resize:function|None;
        """창 크기가 조절될때마다 호출되는 함수입니다."""
        self.resized:function|None;
        """창 조절이 끝났을때 호출되는 함수입니다."""
        self.keydown:function|None;
        """특정 키가 눌렸을때 호출되는 함수입니다."""
        self.keyup:function|None;
        """특정 키를 뗐을때 호출되는 함수입니다."""
        self.mouseKeydown:function|None;
        """마우스 버튼을 눌렀을때 호출되는 함수입니다."""
        self.mouseKeyup:function|None;
        """마우스 버튼을 뗏을때 호출되는 함수입니다."""
        
        self.windowMove:function|None;
        """창을 이동시킬때 호출되는 함수입니다."""
        self.windowQuit:function|None;
        """창의 닫기 버튼을 눌렀을때 호출되는 함수입니다."""
        self.windowMaximized:function|None;
        """창이 최대화 되었을때 호출되는 함수입니다."""
        self.windowMinimized:function|None;
        """창이 최소화 되었을때 호출되는 함수입니다."""
        self.windowRestore:function|None;
        """창이 복구되었을때 호출되는 함수입니다."""
        self.dropFile:function|None;
        """파일을 드래그 앤 드롭 했을대 호출되는 함수입니다."""

        self.Content:str;
        """표시할 텍스트입니다."""
        self.FontSize:int;
        """폰트 크기입니다."""
        self.WrapWidth:int;
        """줄바꿈의 기준이 되는 너비입니다."""
        self.TextColor:Color;
        """글자 색입니다."""
        self.Background:Color|None;
        """배경 색입니다."""

from ZeneretyEngine import TextBox;