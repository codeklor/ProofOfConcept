'''
Created on Nov 14, 2022

@author: Matthew Billingsley

Source Code Watcher_app2.py
Working towards integration with Kivy GUI

The below code can be executed to see the Kivy GUI Demo;
    Restriction, verify you are in the Kivy Virtual Environment before execution.
# python kivy_venv\share\kivy-examples\demo\showcase\main.py

'''

import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class BoxLayout(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class WatcherApp(App):
    pass

if __name__ == '__main__':
    WatcherApp().run()