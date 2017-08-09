#!/usr/bin/python
#-*-coding:utf-8-*-

from exam_ui import ExamUI
import random

class ExamBase():
    def __init__(self, title):
        self._pass = 0
        self._fail = 0
        self._ui = ExamUI(title)

    def __get_user_answer(self):
        while True:
            self._ui.draw()
            user_answer = raw_input('输入你的答案: ')
            try:
                user_answer = int(user_answer)
                break
            except:
                pass
        return user_answer

    def __set_question(self, question):
        self._ui.clear_all_messages()
        self._ui.set_question(question[0])
        for i in range(1, len(question)):
            self._ui.set_choice(i, question[i])

    def __exit_exam(self):
        self._ui.clear_all_messages()
        self._ui.set_message(0, '    本次测试结束啦')
        self._ui.draw()

    def make_question(self):
         return ('1 + 1 =',), 2

    def show_result(self, answers):
        #self._ui.clear_all_messages()
        self._ui.set_result(answers)
        self._ui.set_statistic(self._pass, self._fail)
        self._ui.draw()

    def start(self, question_num):
        for i in range(0, question_num):
            question, answer = self.make_question()
            self.__set_question(question)
            user_answer = self.__get_user_answer()
            if answer == user_answer:
                self._pass += 1
            else:
                self._fail += 1
            answers = (answer, user_answer)
            self.show_result(answers)
            
            raw_input('请按回车继续: ')

        self.__exit_exam()
