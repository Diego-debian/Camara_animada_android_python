import kivy
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window 
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config 
from kivy.core.window import WindowBase
import os
import time
from commands import getoutput
#from kivy.graphics.opengl import glReadPixels, GL_RGBA, GL_UNSIGNED_BYTE
#from kivy.core.image import ImageLoader
import random

Config.set("graphics", "width", "650")
Config.set("graphics", "height", "400")
Config.set('graphics', 'orientation', 'horizontal')

class Camara_Animada(App):        

    def ac_btn1(self, *args):
        if (self.a == 0):
            self.Animacion1()
            self.a = 1  
    
    def ac_btn2(self, *args):
        if (self.a == 1):
            self.CAM_WIDGET.remove_widget(self.Anim)
            self.a = 0 

    def ac_btn3(self, *args):
        self.Cam_avatar = self.avatares[random.randrange(len(self.avatares))]
        if (self.a == 0):
            self.ac_btn1()
            self.ac_btn2()
        if (self.a == 1):
            self.ac_btn2()
            self.ac_btn1()

    def ac_btn4(self, *args):
        self.Capturar_display()
           

    def Animacion1(self, *args):
        self.Anim = Image()
        self.Anim.source = self.Cam_avatar
        self.Anim.anim_delay=(0.15)
        self.Anim.pos_hint= {"x": -0.1, "center_y": -1}
        self.Anim.pos = random.randrange(100,680), random.randrange(100,460)
        self.CAM_WIDGET.add_widget(self.Anim)
#        self.CAM_WIDGET.remove_widget(self.Anim)
 

    def Mostrar_cam(self):
        global Cam
        Cam = Camera()
        Cam.resolution=(640,480)
        Cam.size=(680,460)
        Cam.pos=(100,100)
#       Cam.texture
        self.CAM_WIDGET.add_widget(Cam)


    def Capturar_display(self):	
#        self.CAM_WIDGET.clear_widgets()

        try:
          #  Window.screenshot(name='captura.png')
  
            Window.screenshot(name='../../../../../storage/sdcard1/Picture/captura.png')

        
        except:
            Window.screenshot(name='../../../../../storage/sdcard0/Picture/captura.png')    




    def Boton1(self):       
        global btn1
        btn1 = Button()
        btn1.text= 'mostrar' 
        btn1.size_hint = 0.7, 0.4
        btn1.pos = 60,30
        btn1.height = '48dp'
        btn1.bind(on_press = self.ac_btn1)
        self.CAM_WIDGET.add_widget(btn1)

    def Boton2(self):       
        global btn2
        btn2 = Button()
        btn2.text= 'remover' 
        btn2.size_hint = 0.7, 0.4
        btn2.pos = 180,30
        btn2.height = '48dp'
        btn2.bind(on_press = self.ac_btn2)
        self.CAM_WIDGET.add_widget(btn2)

    def Label1(self):       
        global lbl1
        lbl1 = Label()
        adress = getoutput('pwd')
        Adress = str(adress)
        print Adress
        lbl1.text = str(Adress)  
        lbl1.pos = 180,300
        self.CAM_WIDGET.add_widget(lbl1)

    def Boton3(self):       
        global btn3
        btn3 = Button()
        btn3.text= 'cambiar' 
        btn3.size_hint = 0.7, 0.4
        btn3.pos = 300,30
        btn3.height = '48dp'
        btn3.bind(on_press = self.ac_btn3)
        self.CAM_WIDGET.add_widget(btn3)

    def Boton4(self):       
        global btn4
        btn4 = Button()
        btn4.text= 'Capturar' 
        btn4.size_hint = 0.7, 0.4
        btn4.pos = 420,30
        btn4.height = '48dp'
        btn4.bind(on_press = self.ac_btn4)
        self.CAM_WIDGET.add_widget(btn4)


    def build(self):  
        self.a = 0
        self.avatares = ['img/caballo.zip', 'img/deansface.zip', 'img/hypno.zip', 'img/narices.zip', 'img/light.zip', 'img/Skull.zip']
        self.Cam_avatar = self.avatares[1]
        self.CAM_WIDGET = Widget()
        self.Mostrar_cam()
        self.Boton1()
        self.Boton2()
        self.Boton3()
#        self.Label1()
        self.Boton4()
        return self.CAM_WIDGET


if __name__ == '__main__':
    Camara_Animada().run()
