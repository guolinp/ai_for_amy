#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from exam_base import ExamBase


class MathMulitplicationExam(ExamBase):

    def make_question(self):
        a = random.choice(range(1, 10))
        b = random.choice(range(1, 10))
        question = "%d x %d =" % (a, b)
        answer = a * b
        return (question,), answer

if __name__ == "__main__":
    t = MathMulitplicationExam('九九乘法表测试')
    t.start(10)
