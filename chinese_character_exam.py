#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from exam_base import ExamBase


class ChineseCharacterQuestion():

    def __init__(self, db):
        self._db = db
        self._questions = list()

    def load_db(self):
        with open(self._db) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                if line.startswith('#'):
                    continue
                q = line.split('|')
                if len(q) == 0:
                    continue
                self._questions.append((q[:-1], int(q[-1])))
        return len(self._questions) > 0

    def get_next(self):
        which_one = random.choice(range(0, len(self._questions)))
        return self._questions[which_one]


class ChineseCharacterExam(ExamBase):

    def __init__(self, title, db):
        ExamBase.__init__(self, title)
        self._question = ChineseCharacterQuestion(db)
        if not self._question.load_db():
            print 'no questions'

    def make_question(self):
        return self._question.get_next()

if __name__ == "__main__":
    t = ChineseCharacterExam('汉字认字测试', 'questions.db')
    t.start(10)
