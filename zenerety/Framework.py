from zenerety import Display
from .Scene import Scene


class Framework:
    SavingPerformance:bool
    """saving performance by reducing event polling."""
    Running:bool
    """whether framework is running"""
    RunningTime:float
    """framework running time so far in milisecond"""

    def Init(title:str, width:int, height:int):
        """init to framework"""

    def Run():
        """run framework"""

    def Stop():
        """stop framework."""

    def SetScene(scene:Scene):
        Display.Target = scene;

    def GetScene() -> Scene:
        return Display.Target;

    Scene = property(GetScene, SetScene);
    """표시할 장면입니다."""

from JyunrcaeaFramework import Framework;