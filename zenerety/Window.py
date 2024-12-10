class Window:
    """창과 관련된 기능들이 모여있습니다."""

    Width:int
    """너비"""
    Height:int
    """높이"""
    Opacity:float
    """투명도"""
    X:int
    """창의 수평 위치"""
    Y:int
    """창의 수직 위치"""
    Fullscreen:bool
    """전체화면 여부"""
    Title:str
    """제목"""
    BackgroundColor:tuple[int,int,int]
    """배경색"""
    Borderless:bool
    """무테 여부"""
    AlwaysOnTop:bool
    """항상 맨 위에 고정시킬지에 대한 여부"""
    FrameworkStopWhenClose:bool
    """창을 닫을때 프레임워크를 중단할지에 대한 여부입니다."""
    BlockAltF4:bool
    """Alt + F4 단축키로 창을 종료하는것을 막을지에 대한 여부입니다"""
    Resizable:bool
    """창 크기를 조절할수 있게 할지에 대한 여부입니다."""

    def Raise():
        """창을 맨 앞으로 올리고 이 창에 초첨을 맞춥니다."""
        pass

    def Restore():
        """최소/최대화된 창의 크기/위치를 원래대로 돌려놓습니다."""
        pass

    def Resize(width:int,height:int):
        """크기를 조절합니다."""
        pass

    def Move(x:int,y:int):
        """창을 이동합니다. (None은 중심)"""
        pass

    def SetMaximizeSize(width:int, height:int):
        """최대 창 크기를 지정합니다."""
        pass

    def SetMinimizeSize(width:int, height:int):
        """최소 창 크기를 지정합니다."""
        pass

    def Maximize():
        """창을 최대화 합니다."""
        pass

    def Minimize():
        """창을 최소화 합니다."""
        pass

from JyunrcaeaFramework import Window;