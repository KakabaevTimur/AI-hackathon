#!/usr/bin/python3

import sys
import collections
import pandas as pd
import re

def clear_html_tags(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '\n', raw_html)
  return cleantext

def clear_text(text):
    text = text.replace("."," ")
    text = text.replace(","," ")
    text = text.replace(":"," ")
    text = text.replace("\""," ")
    text = text.replace("\'"," ")
    text = text.replace("!"," ")
    text = text.replace("*"," ")
    text = text.replace("{"," ")
    text = text.replace("}"," ")
    text = text.replace("["," ")
    text = text.replace("]"," ")
    text = text.replace("/"," ")
    text = text.replace("\\"," ")
    text = text.replace("-"," ")
    # text = text.replace("+"," ")
    text = text.replace("»"," ")
    text = text.replace("«"," ")
    text = text.replace("↔"," ")
    text = text.replace("?"," ") 
    text = text.replace(")"," ") 
    text = text.replace("("," ") 
    text = text.replace("|"," ") 
    text = text.replace("→"," ") 
    text = text.replace("~"," ") 
    text = text.replace("^"," ") 
    text = text.replace(";"," ") 
    text = text.replace("@"," ") 
    text = text.replace("№"," ") 
    text = text.replace("%"," ") 
    text = text.replace("•"," ") 
    text = text.replace("&"," ") 
    text = text.replace("$"," ") 
    text = text.replace("…"," ") 
    text = text.replace("="," ") 
    text = text.replace("–"," ") 
    text = text.replace("—"," ") 
    text = text.replace("_"," ") 
    text = text.replace("."," ") 
    text = text.replace("“"," ") 
    text = text.replace("”"," ") 
    text = text.replace("©"," ") 
    text = text.replace("&quot;"," ") 
    text = text.replace("</?\w+>", " ")
    text = text.replace(u"\u2022", " ")
    return text

def clear_words(words):
    to_remove = ["и", "в", "с", "на", "для", "как", "hh", "их", "курс", "а", "но", "logo", "по","null","name",'id','false','url','alternate_url','lat',
    'lng','true','line_name','station_id','line_id','premium', 'department','has_test','response_letter_required','area',
    'salary','gross','currency','to','from','работы','original','знание','id','metro_stations','metro',
    'raw','description','building','street','city','день','fullday','полный','station_name','trusted',
    'vacancies_url','logo_urls','открытая','open','accept_temporary','working_time_modes','working_time_intervals',
    'working_days','schedule','contacts','responsibility','requirement','snippet','участие','умение','серпуховско-тимирязевская',
    'улица,','понимание','замоскворецкая','от','original','station_name','rur','employer','relations', 'or', 'and',
    'insider_interview','apply_alternate_url','archived','published_at','sort_point_distance','response_url',
    'address','type', 'переулок', 'или', 'проспект', 'арбатско-покровская', 'калужско-рижская', 'года', 'набережная', 'серпуховскотимирязевская',
    'лет', 'улица', 'created_at', 'httpsapihhruareas1', 'хорошее', 'под', 'сокольническая', 'калужскорижская', 'арбатскопокровская', 'не']
    return list(filter(lambda x: x not in to_remove and not x.isdigit() and len(x) < 35, words))

def top_words(text, n_print):
    text = clear_html_tags(text)
    counts = {}
    text = clear_text(text)
    words = text.lower().split()
    words = clear_words(words)

    for word in words:
        # Get commons
        if not counts.get(word):
            counts[word] = 1
        else:
            counts[word] += 1

    counter = collections.Counter(counts)
    if n_print > 0:
        return counter.most_common(n_print)
    else:
        return counter.most_common()



if __name__ == "__main__":
    # Read input file, note the encoding is specified here 
    # It may be different in your text file
    file = open(sys.argv[1], encoding="utf8")
    content=file.read()
    n_words = int(sys.argv[2])
    top_words(content, n_words)
    # Close the file
    file.close()
