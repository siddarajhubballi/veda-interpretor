import nltk  
print("Loading...")
from nltk.corpus import wordnet as wn 
from nltk.corpus import wordnet

import os
import re
import json
import random
import itertools
import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}

print("     ===================================================================================")
print("                                          VEDA-INTERPRETOR                                      ")
print("     ===================================================================================\n")


def get_links(item):
    duckDuckUrl = 'https://html.duckduckgo.com/html/'
    payload = {'q': ''}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'}
    link_results = set()
    payload['q'] = item
    link_elements = []
    while link_elements == []:
        try:
            res = requests.post(duckDuckUrl, data=payload, headers=headers)
        except Exception as e:
            print(f"For: {item} - {e}")
            print(f"Too many requests! need to cool down")
            time.sleep(random.randrange(5, 10))
            break
        soup = BeautifulSoup(res.text, 'html.parser')
        link_elements = soup.findAll('a')
        time.sleep(random.randrange(2, 4))
    time.sleep(random.randrange(2, 4))
    for i in link_elements:
        link = i.get("href")
        link_results.add(link)
    link_list = list(link_results)
    # print("Links fetched, ", link_list)
    return link_list

def getSynonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    synonyms_new = [i.replace("_"," ").lower() for i in synonyms] 
    synonyms_new.append(word)
    return set(synonyms_new)

def giveShloka(choice,id):
    veda="processed_data/"
    if(choice == 1):
        veda = veda + "rigveda_exp_final.txt"
    elif(choice == 2):
        veda = veda + "samveda_exp_final.txt"
    elif(choice == 3):
        veda = veda + "atharvaveda_exp_final.txt"
    else :
        veda = veda + "yajurveda_exp_final.txt"
    
    f = open(veda, "r", encoding="utf8")
    for i in range(1,id):
        sentence = f.readline()
    sentence = f.readline()
    return sentence

def searchTerms(sentence):
    searchTerms = []
    words = sentence.split()
    for i in range(len(words)):
        if(words[i] in nouns):
            synonyms = getSynonyms(words[i])
            temp = words
            for k in synonyms:
                temp[i] = k
                term = " ".join(temp)
                searchTerms.append(term)
    return searchTerms

                    
choice = int(input("MENU :\n1. Rig Veda\n2. Sama Veda\n3. Atharva Veda\n4. Yajur Veda\nEnter your choice : "))
id = int(input("Enter Sholka id : "))

shloka = giveShloka(choice,id)

print("\n=================")
print(shloka)
print("=================\n")

subsentences = shloka.split(",")
terms = []

for subsentence in subsentences:
    terms = terms + searchTerms(subsentence)
print("Search terms generated")

print("Fetching links...\n")

links = []
i=1
for term in terms:
    if i==10:
        break
    print("Fetching links for " + term)
    links = links + get_links(term)
    i=i+1

freq = {}
for item in links:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

print("Results : ")
freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
for x in freq:
    print(x)

# high-priest of yajna and the divine voice