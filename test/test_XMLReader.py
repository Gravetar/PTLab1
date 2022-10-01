# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n" + \
               "<root>\n" + \
               "    <Иванов_Иван_Иванович>\n" + \
               "        <математика>67</математика>\n" + \
               "        <литература>100</литература>\n" + \
               "        <программирование>91</программирование>\n" + \
               "    </Иванов_Иван_Иванович>\n" + \
               "    <Петров_Петр_Петрович>\n" + \
               "        <математика>78</математика>\n" + \
               "        <химия>87</химия>\n" + \
               "        <социология>61</социология>\n" + \
               "    </Петров_Петр_Петрович>\n" + \
               "</root>\n"
        data = {
            "Иванов_Иван_Иванович": [
                ("математика", 67), ("литература", 100),
                ("программирование", 91)
            ],
            "Петров_Петр_Петрович": [
                ("математика", 78), ("химия", 87), ("социология", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.XML")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
