from zenerety import *

global scene;
scene = Scene();

pink_box:Box;
#background:Sprite;

red = Color(255,150,150);
green = Color(150,255,150);
blue = Color(150,150,255);

class MyBackground(Sprite):
    def __init__(self):
        self.bg1 = Texture(r"scenes\bg1.png");
        self.bg2 = Texture(r"scenes\bg2.png");
        self.bg3 = Texture(r"scenes\bg3.png");

        self.keydown = self.switch;
        super().__init__(self.bg1);

    def switch(self, key):
        if (key == int(Keycode._1)):
            self.Texture = self.bg1;
        elif (key == int(Keycode._2)):
            self.Texture = self.bg2;
        elif (key == int(Keycode._3)):
            self.Texture = self.bg3;

# 처음 시작될때 호출되는 함수
def prepare():
    global pink_box;

    scene.AddObject(MyBackground());

    pink_box = Box(100, 100, red);
    scene.AddObject(pink_box);

    Window.Raise();

scene.prepare = prepare;

# 매 프레임마다 호출되는 함수
def update(ms):
    if (Input.IsKeyPressed(Keycode.UP)):
        pink_box.y -= ms;
    if (Input.IsKeyPressed(Keycode.DOWN)):
        pink_box.y += ms;
    if (Input.IsKeyPressed(Keycode.LEFT)):
        pink_box.x -= ms;
    if (Input.IsKeyPressed(Keycode.RIGHT)):
        pink_box.x += ms;

scene.update = update;

# 키가 눌렸을때 딱 한번 호출되는 함수
def keydown(key):
    global pink_box;
    if (key == int(Keycode.Z)):
        pink_box.Color = red;
    elif (key == int(Keycode.X)):
        pink_box.Color = green;
    elif (key == int(Keycode.C)):
        pink_box.Color = blue;

    elif (key == int(Keycode.F11)):
        Window.Fullscreen = not Window.Fullscreen;
    elif (key == int(Keycode.ESCAPE)):
        Framework.Stop();

scene.keydown = keydown;