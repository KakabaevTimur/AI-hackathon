import parse_taxonomy
import get_text_from_word
import words
import sys
from pprint import pprint

def get_list_of_abilities(path):
    fileFormat = path.split('.')[-1]
    abils = None
    if fileFormat == 'docx':
        abils = get_text_from_word.getTextWord(path)
    elif fileFormat == 'xls':
        abils = parse_taxonomy.GetTextExcel(path)
    elif fileFormat == 'xlsx':
        abils = parse_taxonomy.GetTextExcel(path)[2::]
    else:
        print("Invalid file extension")
        exit(1)
    return list(abils)

if __name__ == "__main__":
    path = sys.argv[1]
    pprint(get_list_of_abilities(path))
    