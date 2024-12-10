# Zenerety
[Jyunrcaea! Framework](https://github.com/jyunrcaea/JyunrcaeaFramework/tree/0.7.x)을 기반으로 한, Python용 2D 게임 개발 프레임워크

## Example
```py
from zenerety import *;
    
Framework.Init("Title", 1280, 720);
Framework.Run();
```

## Requirements
Python 3 및 .NET Runtime 최신버전

## Architecture 
자동완성 지원을 위해, 더미 클래스/매서드를 만들고 덮어쓰는 방식을 사용하였습니다.  
[Python.NET](https://github.com/pythonnet/pythonnet)으로 C# 클래스/매서드를 불러와서 덮어쓰는 방식으로, 사실상 C#에 있던 대부분의 매서드/클래스와 일대일로 대응합니다.

### Known Issues
(Python.NET를 사용하여 C#과 Python 서로 상호작용할때의 문제점입니다.)
- C# 에서는 파이썬 내에서 override된 매서드를 감지하지 못합니다. 이로 인해 JF와 사용법이 약간 다른편입니다.  
- C# Enum의 일부 원소들이 Python에서는 문자열로 바뀝니다(예: 65 -> 'A'). 이로 인해 keydown, keyup 이벤트로 들어온 키를 판별할때 ``key == int(Keycode.A)`` 같은 방식으로 비교해야합니다.

여담으로, 예외 발생시 Python의 예외일 경우 대게 Python.NET의 문제일 가능성이 큽니다.
