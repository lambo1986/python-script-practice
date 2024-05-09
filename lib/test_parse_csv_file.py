import pytest
from parse_csv_file import parse_csv

def test_parse_csv(tmp_path):
    file_path = tmp_path / "test_data.csv"
    with open(file_path, "w") as file:
        file.write("Name,Email,Phone\n")
        file.write("John Doe,john.doe@example.com,555-1234\n")
        file.write("Jane Smith,jane.smith@example.com,555-5678\n")
        file.write("Alice Johnson,alice.johnson@example.com,555-9876\n")
        file.write("Bob Brown,bob.brown@example.com,555-5432\n")
        file.write("Eve Williams,eve.williams@example.com,555-8765\n")

    parse_csv(file_path)

    with open(file_path, "r") as file:
        file_content = file.read()
        assert "John Doe,john.doe@example.com,555-1234" in file_content.split("\n")
        assert "Eve Williams,eve.williams@example.com,555-8765" in file_content.split("\n")
