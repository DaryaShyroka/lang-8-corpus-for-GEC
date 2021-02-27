import time
import json
import os
from bs4 import BeautifulSoup
import bs4
from urllib.request import urlopen
from collections import defaultdict
import re
import pdb


def get_profile(soup):
    metadata = {}
    for profile in soup.find_all("div", {"class": "user_profile_row"}):
        subtitle = profile.find("div", {"class": "subtitle"})
        metadata[subtitle.text.strip()] = subtitle.next_sibling.strip()
    return metadata


def get_friends(soup):
    friends = []
    for friend in soup.find_all("div", {"class": "language_box f_left"}):
        if "english" == friend.find("li", {"class": "studying"}).text.strip().lower():
            friends.append(friend.contents[1]["href"][1:])
    # next_page = soup.find('li',{'class':'pager_next'})
    # if next_page:
    #     time.sleep(1)
    #     print(next_page)
    #     href = next_page.contents[0]["href"]
    #     try:
    #         new_soup = BeautifulSoup(urlopen('https://lang-8.com' + href), 'html.parser')
    #         friends.extend(get_friends(new_soup))
    #     except:
    #         pass
    return friends


def get_documents(soup):
    documents = []
    for doc in soup.find_all("h3", {"class": "journal_title"}):
        doc_id = doc.contents[1]["href"].rsplit("/", 1)[-1]
        documents.append(doc_id)
    # next_page = soup.find('li',{'class':'pager_next'})
    # if next_page:
    #     time.sleep(1)
    #     href = next_page.contents[0]["href"]
    #     try:
    #         new_soup = BeautifulSoup(urlopen('https://lang-8.com' + href), 'html.parser')
    #         documents.extend(get_documents(new_soup))
    #     except:
    #         pass
    return documents


def get_corrections(soup):
    comments_field = soup.find("div", {"id": "comments_and_corrections_field"})
    return comments_field.find_all("div", {"class": "correction_box"})


def get_corrected_sentence(p):
    if not p.find("span", {"class": "sline"}):
        return p.get_text().strip()
    else:
        sent = ""
        for comp in p.children:
            if type(comp) == bs4.element.NavigableString:
                sent += comp
            else:
                if comp.attrs.get("class") and comp["class"][0] == "sline":
                    continue
                if not comp.find("span", {"class": "sline"}):
                    sent += comp.get_text()
        return sent


def get_pair_sents(corrections):
    pair_sents = defaultdict(list)
    for cor in corrections:
        ref = cor.find("li", {"class": "corrected correct"})
        if ref:
            org = cor.find("li", {"class": "incorrect"}).get_text()
            ref = get_corrected_sentence(ref.find("p"))
            pair_sents[org].append(ref)
    return pair_sents