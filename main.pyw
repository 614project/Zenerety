from zenerety import *;
from scenes import *;
    
Framework.Init("화살표 키로 이동, zxc키로 색변경, 123으로 배경변경, f11로 전체화면, esc로 나가기", 614, 480);
Window.BackgroundColor = Color.White;
Scene.Set(myScene.scene);
Framework.Run();