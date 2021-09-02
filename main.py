import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from pygame import mixer
from mutagen.mp3 import MP3



Window.size = (320, 600)


class MusicScreen(Screen):
    pass

class SongCover(MDBoxLayout):

    mixer.init()
    song_path = "Specturm Layers.mp3"
    song_name = song_path.split("/")
    song_name = song_name[len(song_name)-1].replace(".mp3","")
    
    mixer.music.load(song_path)
    mixer.music.set_volume(0.5)

    length = MP3(song_path).info.length

    angle = NumericProperty()
    anim = Animation(angle=-360, d=3, t='linear')
    anim += Animation(angle=0, d=3, t='linear')

    progress = Animation(value=100, d= int(length), t='linear')
    anim.repeat = True
    
    is_play = False
    
    def rotate(self):
        if self.anim.have_properties_to_animate(self):
            self.anim.stop(self)
            self.progress.stop(self.widget)
            mixer.music.pause()
            self.is_play = True
        else:
            if self.is_play:
                mixer.music.unpause()
                self.is_play = True
            else:
                mixer.music.play()

            self.anim.start(self)
            self.progress.start(self.widget)


    def play(self, widget):
        self.widget = widget
        self.progress.start(widget)
        self.rotate()

class MainApp(MDApp):
    def build(self):
        return MusicScreen()

MainApp().run()