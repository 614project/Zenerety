import os;
from pythonnet import load;
load("coreclr");
import clr;
absolute_path = os.path.dirname(os.path.abspath(__file__));
clr.AddReference(os.path.join(absolute_path,r"ZeneretyEngine.dll"));
clr.AddReference(os.path.join(absolute_path,r"Jyunrcaea! Framework.dll"));

from .BaseObject import BaseObject;
from .Box import Box;
from .Color import Color;
from .Display import Display;
from .DrawableObject import DrawableObject;
from .Texture import Texture;
from .Framework import Framework;
from .Input import Input;
from .Keycode import Keycode;
from .ObjectList import ObjectList;
from .Scale2D import Scale2D;
from .Scene import Scene;
from .Sprite import Sprite;
from .TextBox import TextBox;
from .Texture import Texture;
from .Window import Window;

if __name__ == "__main__":
    print("It is not executable script! only import able.");