#!/usr/bin/python
#-*-coding:utf-8-*-

import os


class Graphic():

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._cache = list()

        for x in range(0, self._height):
            l = list()
            for y in range(0, self._width):
                l.append(' ')
            self._cache.append(l)

    def __in_range(self, x, y):
        return x in range(0, self._width) and y in range(0, self._height)

    def width(self):
        return self._width

    def height(self):
        return self._height

    def set_char(self, x, y, char):
        if self.__in_range(x, y):
            self._cache[y][x] = char
        # else:
        #    print 'out of range'

    def set_string(self, x, y, string):
        str_len = len(string)
        for i in range(0, str_len):
            self.set_char(x + i, y, string[i])

    def clear(self):
        for x in range(0, self._height):
            for y in range(0, self._width):
                self._cache[x][y] = ' '

    def draw(self):
        os.system('clear')
        for x in range(0, self._height):
            print ''.join(self._cache[x])
