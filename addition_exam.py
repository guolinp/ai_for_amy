#!/usr/bin/python
#-*-coding:utf-8-*-

import math_exam
import random

class MathAdditionExam(math_exam.MathExam):
    def make_question(self):
        a = random.choice(range(1,9))
        b = random.choice(range(1,10-a))
        question = "%d+%d=" % (a,b)
        answer = a + b
        return question, answer

if __name__ == "__main__":
    t = MathAdditionExam(2)
    t.start()
