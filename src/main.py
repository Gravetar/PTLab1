# -*- coding: utf-8 -*-
import argparse
import sys

from CalcGoodStudent import CalcGoodStudent
from CalcRating import CalcRating
from XMLDataReader import XMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = XMLDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcGoodStudent(students).calc()
    print("CountGoodStudents: ", rating)


if __name__ == "__main__":
    main()
