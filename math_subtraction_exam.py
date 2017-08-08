#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from exam_base import ExamBase

class MathSubtractionExam(ExamBase):
    def make_question(self):
        a = random.choice(range(2,10))
        b = random.choice(range(1,a))
        question = "%d-%d=" % (a,b)
        answer = a - b
        return (question,), answer

if __name__ == "__main__":
    t = MathSubtractionExam('    十以内减法测试')
    t.start(3)
