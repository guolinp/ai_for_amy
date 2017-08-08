#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from exam_base import ExamBase

class MathAdditionExam(ExamBase):
    def make_question(self):
        a = random.choice(range(1,9))
        b = random.choice(range(1,10-a))
        question = "%d+%d=" % (a,b)
        answer = a + b
        return (question,), answer

if __name__ == "__main__":
    t = MathAdditionExam('    十以内加法测试')
    t.start(5)
