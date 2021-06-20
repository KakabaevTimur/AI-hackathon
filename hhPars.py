import requests
import words
import get_abilities


def getPage(param):
  params = {
  'text': param,
  'page': 0, # Индекс страницы поиска на HH
  'per_page': 30 # Кол-во вакансий на 1 странице
  }

  req = requests.get('https://api.hh.ru/vacancies', params) 
  data = req.content.decode() # декод чтобы Кириллица отображалась корректно
  req.close()
  data = words.clear_text(data)
  return data

def getTextfromHH(path):
  resultHH = ""
  skills = get_abilities.get_list_of_abilities(path)

  for skill in skills:
    print(f"Parsing {skill}")
    resultHH += getPage(skill)

  return resultHH, skills


