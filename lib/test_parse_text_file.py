import pytest
from parse_text_file import parse_text_file

def test_parse_text_file(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as file:
        file.write("Line 1\nLine 2\nLine 3")

    parse_text_file(file_path)

    with open(file_path, "r") as file:
        assert file.read() == "Line 1\nLine 2\nLine 3"