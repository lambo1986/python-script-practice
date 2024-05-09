def parse_text_file(file_path):
  with open(file_path, 'r') as file:
    for line in file:
      print(line)

file_path = "./resources/sample1.txt"
parse_text_file(file_path)