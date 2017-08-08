#!/usr/bin/python
#-*-coding:utf-8-*-

import os 
import graphic

class Component():
    def __init__(self, x_pos, y_pos):
        self._x_pos = x_pos
        self._y_pos = y_pos

    def draw(self, g):
        pass

class Label(Component):
    def __init__(self, x_pos, y_pos, text=None):
        Component.__init__(self, x_pos, y_pos)
        self._text = text

    def set_text(self, text):
        if text and len(text) > 0:
            self._text = text

    def clear_text(self):
        self._text = None

    def draw(self, g):
        if self._text:
            g.set_string(self._x_pos, self._y_pos, self._text)
