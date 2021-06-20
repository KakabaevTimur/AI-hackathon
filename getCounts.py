import os.path
from pprint import pprint
from typing import List

from fuzzywuzzy import fuzz

import hhPars
import parse_refl_comments
import words


def getCounts(tax_path, common_perc):
    text=""
    skills=""
    if os.path.isfile('text.txt'):
        print("Reading from files")
        file = open('text.txt', 'r', encoding="utf-8")
        text = file.read()
        file.close()
        file = open('skills.txt', 'r', encoding="utf-8")
        skills = file.read().split("\n")
        file.close()
    else:
        text, skills = hhPars.getTextfromHH(tax_path)
        print("Get HH")
        # text += parse_refl_comments.getComments(".\Reflexia_PTsS-2020.xls")
        # print("Get Comments")
        file = open('text.txt', 'w+', encoding="utf-8")
        file.write(text)
        file.close()
        with open("skills.txt", "w+", encoding="utf-8") as file:
            file_lines = "\n".join(skills)
            file.write(file_lines)

    
    top = words.top_words(text, 0)
    skills_tmp = []
    for skill in skills:
        skills_tmp.extend(skill.split())
    skill_top = {}
    for skill in skills_tmp:
        skill_top.update({t[0]: t[1] for t in top if t[0].lower() == skill.lower()})
    
    # Adding up commons
    common = {}
    for skill in skill_top.keys():
        if any(skill in i for i in common.values()):
            continue
        for skill2 in skill_top.keys():
            if any(skill2 in i for i in common.values()):
                continue
            if fuzz.ratio(skill, skill2) > common_perc and not skill == skill2:
                if skill not in common.keys():
                    common[skill] = list()
                common[skill].append(skill2)
    for skill in common.keys():
        skill_top[skill] += sum([skill_top[sk] for sk in common[skill]])
        for s in common[skill]:
            skill_top.pop(s)

    # pprint(skill_top)
    return skill_top

if __name__ == "__main__":
    getCounts('./Taxonomii_na_osnove_analiza_rynka_truda.xlsx', 70)
