# -*- coding: utf-8 -*-
from Types import DataType

GoodStudentType = int


class CalcGoodStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: GoodStudentType = 0

    def calc(self) -> GoodStudentType:
        count_good_students = 0
        for student in self.data:
            good_student = True
            for subject in self.data[student]:
                if subject[1] < 76:
                    good_student = False
            if good_student:
                count_good_students += 1
        return count_good_students
