#!/usr/bin/python
#-*-coding:utf-8-*-

import ascii_ui
import random


class MathExam():
    def __init__(self, question_num):
        self._question_num = question_num
        self._pass = 0
        self._fail = 0
        self._ui = ascii_ui.AsciiUI(24,12)

    def start(self):
        for i in range(0, self._question_num):
            question, answer = self.make_question()
            user_answer = self.__get_user_answer(question)
            if answer == user_answer:
                self._pass += 1
                result = '[V] 正确'
            else:
                self._fail += 1
                result = '[X] 错误'
            tip = '        %s%d(%d)' %(question, answer, user_answer)
            self.__show_result(result, tip)

            raw_input('按回车继续: ')

        self.__show_message('测试结束', '')
            
    def make_question(self):
         return '1 + 1 =', 2

    def __get_user_answer(self, question):
        while True:
            self.__show_question(question)
            user_answer = raw_input('你的答案: ')
            try:
                user_answer = int(user_answer)
                break
            except:
                pass
        return user_answer

    def __base_ui(self):
        self._ui.clear()
        self._ui.fill_string(0,  1, '------------------------')
        self._ui.fill_string(0,  2, '        数学测试        ')
        self._ui.fill_string(0,  3, '------------------------')
        self._ui.fill_string(0,  5, '------------------------')
        self._ui.fill_string(0, 11, '------------------------')

    def __show_message(self, msg1, msg2):
        self.__base_ui()
        self._ui.fill_string(0,  4, '正确:[%02d]  错误:[%02d]' % (self._pass, self._fail))
        self._ui.fill_string(0,  8, '    %s                  ' % msg1)
        self._ui.fill_string(0, 10, '    %s                  ' % msg2)
        self._ui.draw()

    def __show_result(self, result, tip):
        self.__show_message(result, tip)

    def __show_question(self, question):
        self.__show_message(question, '')

