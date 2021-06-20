import sys
import words
from fuzzywuzzy import fuzz
from getCounts import getCounts
from parse_input_file import getTextFrom

FUZZING_THRESHOLD = 70

def measure(text, keywords_counts):
    words_tmp = words.clear_text(text)

    uniq = []
    for x in words_tmp.split(' '):
        if x not in uniq:
            uniq.append(x)
    
    score = 0
    max = sum(keywords_counts.values())
    print(max)
    for key in keywords_counts.keys():
        for wd in uniq:
            # if fuzz.ratio(key, wd) > FUZZING_THRESHOLD:
            if key.lower() == wd.lower():
                score += keywords_counts[key]
    return score / max
    
        

if __name__ == "__main__":
    # if len(sys.argv()) != 4:
    #     exit(1)
    text = getTextFrom(sys.argv[1])
    print("Preparing data")
    abilities_path = sys.argv[2] # ./Taxonomii_na_osnove_analiza_rynka_truda.xlsx
    keywords_counts = getCounts(abilities_path, FUZZING_THRESHOLD)
    val = measure(text, keywords_counts)
    print("Score is:", val)
