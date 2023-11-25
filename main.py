import nltk  
print("\n==============> Loading...\n")
from nltk.corpus import wordnet as wn 

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


def get_links(item):
    duckDuckUrl = 'https://html.duckduckgo.com/html/'
    payload = {'q': ''}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'}
    link_results = set()
    payload['q'] = item
    link_elements = []
    with open('processed_data/synonym_filter.txt', "r", encoding="utf8") as f:
        synonym_filter = [line.rstrip() for line in f]
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
        if link and not re.match(r".*duckduckgo.*", link, re.IGNORECASE) and link != '/html/':
            flag = 1
            for filter_word in synonym_filter:
                if re.match(rf'.*{filter_word}.*',link,re.IGNORECASE):
                    flag = 0
                    break
            if flag == 1:
                link_results.add(link)
    link_list = list(link_results)
    print("Links fetched, ", link_list)
    return link_list

def getSynonyms(word):
    with open('processed_data/synonym_filter.txt', "r", encoding="utf8") as f:
        synonym_filter = [line.rstrip() for line in f]
    synonyms = []
    for syn in wn.synsets(word):
        for i in syn.lemmas():
            name = i.name()
            flag = 1
            for filter_word in synonym_filter:
                if re.match(rf'.*{filter_word}.*',name,re.IGNORECASE):
                    flag = 0
                    break
            if flag == 1:
                synonyms.append(name)
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

def fetch_veda(choice):
    fetched_data = []
    veda="processed_data/"
    if(choice == 1):
        veda = veda + "rigveda_exp_final.txt"
    elif(choice == 2):
        veda = veda + "samveda_exp_final.txt"
    elif(choice == 3):
        veda = veda + "atharvaveda_exp_final.txt"
    else :
        veda = veda + "yajurveda_exp_final.txt"
    with open(veda, "r", encoding="utf8") as f:
        fetched_data = [line.rstrip() for line in f]
    return fetched_data

def print_lines(data_array):
    for i in data_array:
        print(i)

def linear_search(fetched_data):
    while True:
        candidate_shlokas = []
        prompt_word = input("Enter the search term: ");
        print("\nSearching..")
        for i in fetched_data:
            if re.search(rf'.*{prompt_word}.*',i,re.IGNORECASE):
                candidate_shlokas.append(i);
        print(f"Search results for {prompt_word} -\n")
        print_lines(candidate_shlokas)
        print("\n\n")
        selection = int(input("\n1)Select a shloka from the search results\n2)Search again\n3)Exit\nEnter your choice: "))
        if selection == 1:
            index_selection = int(input("\nEnter the index of the shloka: "))
            return index_selection
        elif selection == 2:
            continue
        else: 
            return -1
    return -1


def linear_search_prompted(fetched_data):
    while True:
        prompt_word = input("Enter the search term: ");
        print("\nSearching..")
        index = 0
        for i in fetched_data:
            if re.search(rf'.*{prompt_word}.*',i,re.IGNORECASE):
                print(i)
                print("\n")
                selection = int(input("\n1)Select this shloka\n2)Next Shloka\n3)Exit\nEnter your choice: "))
                print("\n")
                if selection == 1:
                    index = int(i.split(":")[0])
                    return index
                elif selection == 2:
                    continue
                else: 
                    return -1;
                print("\n\n")
        selection_outer = int(input("\nNo more results to show\n1)Search again\n2)Exit\nEnter your choice: "))
        if selection_outer == 1:
            continue
        else: 
            return -1;


def main():
    print("===================================================================================")
    print("                                     VEDA-INTERPRETER                              ")
    print("===================================================================================\n")
    choice = int(input("MENU :\n1. Rig Veda\n2. Sama Veda\n3. Atharva Veda\n4. Yajur Veda\nEnter your choice : "))
    entry_choice = int(input("How would you like to proceed with the search?\n1)Search by keyword\n2)Search by Shloka id\nEnter your choice: "))
    if entry_choice == 1:
        print("Fetching data..")
        all_data = fetch_veda(choice)
        print("Data fetched.")
        # shloka_index = linear_search(all_data)
        shloka_index = linear_search_prompted(all_data)
        if shloka_index > 0:
            shloka = all_data[shloka_index - 1]
        else:
            print("Exiting!")
            return
    else:
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
    i = 1
    SEARCH_LIMIT = 20 
    for term in terms:
        if i == SEARCH_LIMIT:
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


if __name__ == "__main__":
    main()