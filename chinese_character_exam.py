#!/usr/bin/python
#-*-coding:utf-8-*-

import ascii_ui
import random

class ChineseCharacterExam():
    def __init__(self, question_num):
        self._question_num = question_num
        self._pass = 0
        self._fail = 0
        self._ui = ascii_ui.AsciiUI(32, 13)

    def start(self):
        for i in range(0, self._question_num):
            question, choice1, choice2, answer = self.make_question()
            user_answer = self.__get_user_answer(question, choice1, choice2)
            if answer == user_answer:
                self._pass += 1
                result = '[V] 正确'
            else:
                self._fail += 1
                result = '[X] 错误'
            self.__show_result(result, question, choice1 if answer == 1 else  choice2)

            raw_input('按回车继续: ')

        self.__show_message('测试结束', '', '', '')
            
    def make_question(self):
         return '天是什么颜色的？', '1. 蓝色', '2. 水果', 1

    def __get_user_answer(self, question, choice1, choice2):
        while True:
            self.__show_question(question, choice1, choice2)
            user_answer = raw_input('你的答案: ')
            try:
                user_answer = int(user_answer)
                break
            except:
                pass
        return user_answer

    def __base_ui(self):
        self._ui.clear()
        self._ui.fill_string(0,  1, '--------------------------------')
        self._ui.fill_string(0,  2, '            汉字测试            ')
        self._ui.fill_string(0,  3, '--------------------------------')
        self._ui.fill_string(0,  5, '--------------------------------')
        self._ui.fill_string(0, 12, '--------------------------------')

    def __show_message(self, msg1, msg2, msg3, msg4):
        self.__base_ui()
        self._ui.fill_string(0,  4, '正确:[%02d]  错误:[%02d]' % (self._pass, self._fail))
        self._ui.fill_string(0,  6, '%s                      ' % msg1)
        self._ui.fill_string(0,  8, '%s                      ' % msg2)
        self._ui.fill_string(0,  9, '    %s                  ' % msg3)
        self._ui.fill_string(0, 10, '    %s                  ' % msg4)
        self._ui.draw()

    def __show_result(self, result, question, answer):
        self.__show_message(result, question, answer, '')

    def __show_question(self, question, choice1, choice2):
        self.__show_message('', question, choice1, choice2)


class ChineseCharacterEasy(ChineseCharacterExam):
    def make_question(self):
        #TODO: Add new class to load DB and generate questions
        #      this function just choose question by random
        with open('questions.db') as f:
            lines = f.readlines()
            i = random.choice(range(0, len(lines)))
            q = lines[i].split('|')
        return q[0], '1. ' + q[1], '2. ' + q[2], int(q[3])

if __name__ == "__main__":
    t = ChineseCharacterEasy(10)
    t.start()
