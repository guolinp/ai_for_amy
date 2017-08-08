#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from exam_base import ExamBase

class ChineseCharacterExam(ExamBase):
    def make_question(self):
        #TODO: Add new class to load DB and generate questions
        #      this function just choose question by random
        with open('questions.db') as f:
            lines = f.readlines()
            i = random.choice(range(0, len(lines)))
            q = lines[i].split('|')
        #return ('Q','A1','A2', 'A3'), int(q[3])
        return (q[0], q[1], q[2]), int(q[3])

if __name__ == "__main__":
    t = ChineseCharacterExam('    汉字认字测试')
    t.start(3)
