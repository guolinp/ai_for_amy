#!/usr/bin/python
#-*-coding:utf-8-*-

import os 
from graphic import Graphic
from component import *

class Panel():
    def __init__(self, width, height):
        self._g = Graphic(width, height)
        self._components = list()

    def add_component(self, component):
        self._components.append(component)

    def draw(self):
        self._g.clear()
        for component in self._components:
            component.draw(self._g)
        self._g.draw()
