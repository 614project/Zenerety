class Display:
    """렌더링과 관련된 기능이 모여있습니다."""

    MonitorWidth:int
    """모니터의 픽셀 너비를 구합니다."""
    MonitorHeight:int
    """모니터의 픽셀 높이를 구합니다."""
    MonitorRefreshRate:int
    """모니터의 주사율을 구합니다."""
    FrameLateLimit:int
    """초당 프레임 제한입니다. (0을 넣을경우 모니터 주사율을 따릅니다.)"""

from JyunrcaeaFramework import Display;