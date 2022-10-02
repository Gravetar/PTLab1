# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcGoodStudent import CalcGoodStudent
import pytest

GoodStudentType = int


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, GoodStudentType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        good_count: GoodStudentType = 1

        return data, good_count

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      GoodStudentType]) \
            -> None:
        calc_goodstudent = CalcGoodStudent(input_data[0])
        assert input_data[0] == calc_goodstudent.data

    def test_calc(self, input_data: tuple[DataType, GoodStudentType]) -> None:
        good_student = CalcGoodStudent(input_data[0]).calc()
        assert pytest.approx(good_student, abs=0.001) == input_data[1]
