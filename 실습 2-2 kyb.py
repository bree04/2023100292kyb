import re

class KyEditor:
    def __init__(self):
        self.lines = []

    def insert(self, pos, text):
        self.lines.insert(pos, text)

    def delete(self, pos):
        if 0 <= pos < len(self.lines):
            self.lines.pop(pos)

    def replace(self, pos, text):
        if 0 <= pos < len(self.lines):
            self.lines[pos] = text

    def print_lines(self):
        for i, line in enumerate(self.lines):
            print(f"[{i}] {line}")

    def make_dictionary(self):
        word_count = {}
        for line in self.lines:
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        print("단어 빈도수:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

def run_editor():
    editor = KyEditor()

    while True:
        command = input("i-입력, d-삭제, r-변경, p-출력, m-사전생성, q-종료 => ")

        if command == 'i':
            pos = int(input("입력행 번호: "))
            text = input("입력행 내용: ")
            editor.insert(pos, text)

        elif command == 'd':
            pos = int(input("삭제행 번호: "))
            editor.delete(pos)

        elif command == 'r':
            pos = int(input("변경행 번호: "))
            text = input("변경행 내용: ")
            editor.replace(pos, text)

        elif command == 'p':
            editor.print_lines()

        elif command == 'm':
            editor.make_dictionary()

        elif command == 'q':
            break

run_editor()
