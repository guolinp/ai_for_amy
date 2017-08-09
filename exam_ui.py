#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from component import Label
from panel import Panel

class ExamUI():
    def __init__(self, title=None):
        self._panel = Panel(32, 16)

        self._panel.add_component(Label(0, 1, '--------------------------------'))
       #self._panel.add_component(Label(0, 2, ' _label_ title                  '))
        self._panel.add_component(Label(0, 3, '--------------------------------'))
       #self._panel.add_component(Label(0, 4, ' _label_stat                    '))
        self._panel.add_component(Label(0, 5, '--------------------------------'))
       #self._panel.add_component(Label(0, 6, '                                '))
       #self._panel.add_component(Label(0, 7, '                                '))
       #self._panel.add_component(Label(0, 8, '                                '))
       #self._panel.add_component(Label(0, 9, '                                '))
       #self._panel.add_component(Label(0,10, '                                '))
       #self._panel.add_component(Label(0,11, '                                '))
       #self._panel.add_component(Label(0,12, '                                '))
       #self._panel.add_component(Label(0,13, '                                '))
       #self._panel.add_component(Label(0,14, '                                '))
        self._panel.add_component(Label(0,15, '--------------------------------'))

        self._label_title = Label(0, 2)
        self._label_stat = Label(0, 4)

        self._panel.add_component(self._label_title)
        self._panel.add_component(self._label_stat)

        self._label_messages = list()
        for i in range(0, 9):
            label = Label(0, 6 + i)
            self._label_messages.append(label)
            self._panel.add_component(label)

        self.set_title(title)
        self.set_statistic(0, 0)

    def set_title(self, title):
        self._label_title.set_text('        %s' % title)

    def set_statistic(self, num_pass, num_fail):
        self._label_stat.set_text('正确: %02d        错误: %02d' % (num_pass, num_fail))

    def set_message(self, msg_index, msg_string):
        if msg_index < 0 or msg_index > 8:
            return
        self._label_messages[msg_index].set_text(msg_string)

    def clear_message(self, msg_index):
        if msg_index < 0 or msg_index > 8:
            return
        self._label_messages[msg_index].clear_text()

    def clear_all_messages(self):
        for i in range(0, 9):
            self._label_messages[i].clear_text()

    def set_result(self, is_correct):
        if is_correct:
            self.set_message(0, '    [V] 回答正确')
        else:
            self.set_message(0, '    [X] 回答错误')

    def set_question(self, question):
        self.set_message(2, question)

    def set_choice(self, index, choice):
        if index < 1 or index > 4:
            return
        self.set_message(2 + index, '  %d. %s' % (index, choice))
        
    def draw(self):
        self._panel.draw()
