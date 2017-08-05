#!/usr/bin/python
#-*-coding:utf-8-*-

import math_exam
import random

class MathSubtractionExam(math_exam.MathExam):
    def make_question(self):
        a = random.choice(range(2,10))
        b = random.choice(range(1,a))
        question = "%d-%d=" % (a,b)
        answer = a - b
        return question, answer

if __name__ == "__main__":
    t = MathSubtractionExam(10)
    t.start()
