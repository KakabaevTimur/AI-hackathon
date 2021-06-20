import sys
import mammoth
from os import path
import words


def getTextWord(filename):
    result = ""
    with open(filename, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
    return words.clear_html_tags(result.value)


if __name__ == "__main__":
    path = sys.argv[1]
    print(list(filter(lambda x: len(x), getTextWord(path).split('\n'))))
