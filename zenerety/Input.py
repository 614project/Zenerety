from .Keycode import Keycode;

class Input:
    """입력과 관련된 기능이 모여있습니다."""

    def IsKeyPressed(key:Keycode):
        """특정 키가 현재 눌려져 있는 상태인지 가져옵니다."""

    class Mouse:
        """마우스/포인터와 관련된 기능이 모여있습니다."""

        BlockEventAtToFocus:bool
        """초첨을 되찾기 위해 창을 클릭한 이벤트는 무시할지에 대한 여부입니다."""

        Grab:bool
        """마우스를 창 밖으로 못나가게 붙잡을지에 대한 여부입니다."""

        HideCursor:bool
        """커서를 숨길지에 대한 여부입니다."""

        BlockWindowFrame:bool
        """커서가 숨겨져 있을때 창 테두리를 조작할수 있게 할지에 대한 여부입니다. (창 조절, 이동 등)"""

        class Key:
            Left = 1
            """왼쪽"""
            Middle = 2
            """중간"""
            Right = 3
            """오른쪽"""

from JyunrcaeaFramework import Input;