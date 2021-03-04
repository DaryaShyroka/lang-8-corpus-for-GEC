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
    """Get dictionary of a user's metadata

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing link to a user's friend-list

    Returns:
        ditionary: dictionary of key = user_id, value = metadata/profile_info
    """
    metadata = {}
    for profile in soup.find_all("div", {"class": "user_profile_row"}):
        subtitle = profile.find("div", {"class": "subtitle"})
        metadata[subtitle.text.strip()] = subtitle.next_sibling.strip()
    return metadata


def get_friends(soup, n = 20):
    """Get list of friend ids (only English learners)

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing link to a user's friend-list
        n (int, optional): Number of friends needed to get. Defaults to 20.

    Returns:
        list: list of integers/friend_ids
    """
    friends = []
    for friend in soup.find_all("div", {"class": "language_box f_left"}):
        if len(friends) == n:
            return friends
        if "english" in friend.find("li", {"class": "studying"}).text.strip().lower():
            friends.append(friend.contents[1]["href"][1:])
    next_page = soup.find('li',{'class':'pager_next'})
    if next_page:
        time.sleep(1)
        href = next_page.contents[0]["href"]
        try:
            new_soup = BeautifulSoup(urlopen('https://lang-8.com' + href), 'html.parser')
            friends.extend(get_friends(new_soup, n - len(friends)))
        except:
            pass
    return friends


def get_documents(soup, n = 20):
    
    """Get list of document/journal ids (only English journals)

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing link to a user's journals list
        n (int, optional): Number of documents needed to get. Defaults to 20.

    Returns:
        list: list of integers/document_ids
    """
    documents = []
    for container in soup.find_all("div", {"class": "journals_flex"}):
        if len(documents) == n:
            return documents
        doc_lang = container.find("li", {"class": "studying"}).text.strip().lower()
        if("english" == doc_lang.lower()):
            doc_id = container.find_all("a")[1]["href"].rsplit("/", 1)[-1]            
            documents.append(doc_id)
    next_page = soup.find('li',{'class':'pager_next'})
    if next_page:
        time.sleep(1)
        href = next_page.contents[0]["href"]
        try:
            new_soup = BeautifulSoup(urlopen('https://lang-8.com' + href), 'html.parser')
            documents.extend(get_documents(new_soup, n - len(documents)))
        except:
            pass
    return documents

def get_corrections(soup):
    """Get list of tagged original-corrected sentences from a document

    Args:
        soup (BeautifulSoup): BeautifulSoap object containing a link with user_id and the user's journal_id

    Returns:
        list: list of Tag elements
    """
    comments_field = soup.find("div", {"id": "comments_and_corrections_field"})
    return comments_field.find_all("div", {"class": "correction_box"})

def get_pair_sents(corrections):
    """Get defaultdict of original-corrected sentences. Corrected sentences are in list. Corrections are made by Lang8 users

    Args:
        corrections (list of Tags): list containing Tag elements

    Returns:
        defaultdict: dictionary of original-corrected sentences
    """
    pair_sents = defaultdict(list)
    for cor in corrections:
        ref = cor.find("li", {"class": "corrected correct"})
        if ref:
            org = cor.find("li", {"class": "incorrect"}).get_text()
            ref = get_corrected_sentence(ref.find("p"))
            pair_sents[org].append(ref)
    return pair_sents

def get_corrected_sentence(p):
    """Get nth corrected sentence made for original sentence

    Args:
        p (Tag): Tag containing a corrected sentence

    Returns:
        String: corrected sentence
    """
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