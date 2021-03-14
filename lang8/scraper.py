import time
import json
import os
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import defaultdict

def get_profile(soup):
    metadata = {}
    for profile in soup.find_all('div', {'class': 'user_profile_row'}):
        subtitle = profile.find('div', {'class': 'subtitle'})
        metadata[subtitle.text.strip()] = subtitle.next_sibling.strip()
    return metadata



def get_friends(soup):
    friends = []
    for friend in soup.find_all('div',{'class':'language_box f_left'}):
        if 'english' == friend.find('li', {'class': 'studying'}).text.strip().lower():
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
    for doc in soup.find_all('h3', {'class': 'journal_title'}):
        doc_id = doc.contents[1]['href'].rsplit('/', 1)[-1]
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

def scrap_metadata():
    result = {}
    output_file = 'lang-8_profiles.json'

    todo_users = set(["213725","673707"])
    done_list = set()

    while todo_users:
        current_user = todo_users.pop()
        success = False
        count = 0
        while not success and count < 10:
            try:
                friends_page_soup = BeautifulSoup(urlopen(f'https://lang-8.com/{current_user}/friends'), 'html.parser')
                documents_page_soup = BeautifulSoup(urlopen(f'https://lang-8.com/{current_user}/journals'), 'html.parser')
                profile = get_profile(friends_page_soup)
                friends = get_friends(friends_page_soup)
                documents = get_documents(documents_page_soup)
                
                entry = {}
                entry['metadata'] = profile
                entry['friends'] = friends
                entry['documents'] = documents
                result[current_user] = entry
                
                success = True
            except:
                print(count, " fail!")
                count += 1
                time.sleep(1)
        if count == 10:
            continue

        for friend in friends:
            if friend not in done_list:
                todo_users.add(friend)
        done_list.add(current_user)
        time.sleep(1)
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile)

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
                if not comp.find("span", {"class": "sline"}):
                    sent += comp.get_text().strip()
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

def download_parallel_sents(user_id, journal_id): 
    url = f"https://lang-8.com/{user_id}/journals/{journal_id}"
    soup = BeautifulSoup(urlopen(url), "html.parser")
    corrections = get_corrections(soup)
    return get_pair_sents(corrections)

def scrap_parralel_sents():
    user_id = 213725

    output_file = 'parallel_sents.json'
    result = defaultdict(dict)

    doc_ids = ["256361636188698521397028321337896574465", "66790772351198343205338104156873537443", "26925720514685372472697671054459123619", "15315532881855258548031902035305937411", "108212644102131691452826825631334775299", "73927908420361877026438805040786028451", "289379293448979329064073272001689926147", "289084686853797097687930179260295526915", "210279654542028363666303976103231207939", "86761333878304985293229014829319829411", "101458756511854233103985034296152268289", "203860010446665114081520125991571928995", "9824360292744538930648547903961544611", "272270008827710797554997709641524682241", "209622523639742916450468077609485580195", "144091741491648197908723994565252200355", "173820573133975343443703218802855229347", "175919122433102828503406040261378946979", "178987358365104073979568696564263925667", "128628740473966544949081283236456866956"]
    for id in doc_ids:
        result[id] = download_parallel_sents(user_id = 213725,journal_id = id)
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile)