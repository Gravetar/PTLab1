# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET

from DataReader import DataReader
from Types import DataType


class XMLDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student in root:
            self.key = student.tag
            self.students[self.key] = []
            for discipline in student:
                self.students[self.key].append((
                    discipline.tag, int(discipline.text)))
        return self.students
