import time
import json
import os
from bs4 import BeautifulSoup
import bs4
from urllib.request import urlopen
from collections import defaultdict
import re
import pandas as pd

CORPUS = pd.read_csv("data/final_corpus.csv", encoding="utf-8").set_index("id")
METADATA = pd.read_csv(
    "data/lang-8-users.csv", encoding="utf-8", dtype={"user_id": str}
)

LOCATION_MAPS = {
    0: "Japan",
    1: "China",
    2: "Taiwan",
    3: "Vietnam",
    4: "Russia",
    5: "Korea",
    6: "Brazil",
    7: "U.S.A",
    8: "France",
    9: "Spain",
}

OCCUPATION_MAPS = {
    0: "Artist",
    1: "Designer",
    2: "Engineer",
    3: "Housewife/ Househusband",
    4: "Office worker",
    5: "Programmer",
    6: "Student",
    7: "Teacher",
    8: "Other",
}

GENDER_MAPS = {0: "Female", 1: "Male"}

SENT_TYPE_MAPS = {0: "original", 1: "corrected"}

METADATA_KEYS = {"sex", "occupation", "location", "Lpoints"}


def construct_metadata_dict(param_dict):
    """Construct the metadata dictionary based on param_dict provided"""
    new_dict = {}

    for k, v in param_dict.items():
        if k in METADATA_KEYS:
            if v == -1:
                continue
            if k == "sex":
                if v in GENDER_MAPS:
                    v = GENDER_MAPS[v]
            elif k == "occupation":
                if v in OCCUPATION_MAPS:
                    v = OCCUPATION_MAPS[v]
            elif k == "location":
                if v in LOCATION_MAPS:
                    v = LOCATION_MAPS[v]
            new_dict[k] = v
    return new_dict


def get_by_range(corpus, sent_type, num_range=(10, 15)):
    """Returns sentence pairs with only sentence length within num_range, sent_type
    is used to specify whether the restrictions are put on original or corrected sentences
    """
    lower, upper = num_range
    if sent_type in SENT_TYPE_MAPS:
        mask = (corpus[SENT_TYPE_MAPS[sent_type]].str.len() >= lower) & (
            corpus[SENT_TYPE_MAPS[sent_type]].str.len() <= upper
        )
        return corpus.loc[mask]
    else:
        org_mask = (corpus["original"].str.len() >= lower) & (
            corpus["original"].str.len() <= upper
        )
        cor_mask = (corpus["corrected"].str.len() >= lower) & (
            corpus["corrected"].str.len() <= upper
        )
        mask = org_mask & cor_mask
        return corpus.loc[mask]


def get_by_multiple_corrections(corpus, n_corrections):
    """Return the sentences which only contains n number of corrections"""
    columns = CORPUS.columns.to_list()
    grouped = corpus.groupby("original").agg("count").reset_index()
    filtered = grouped[grouped["corrected"] >= n_corrections]
    return pd.merge(filtered, CORPUS, on="original", suffixes=("_y", ""))[columns]


def get_by_metadata(corpus, **args):
    """Filter the corpus based on the args provided"""
    if not len(args):
        return corpus
    query_str = " & ".join([f"{k} == '{v}'" for k, v in args.items() if k != "Lpoints"])
    print(query_str)
    filtered = METADATA
    if query_str:
        filtered = METADATA.query(query_str)
    if "Lpoints" in args and args["Lpoints"] != "all":
        query_str = f"lpoints >= {args['Lpoints'][0]} & lpoints <= {args['Lpoints'][1]}"
        print(query_str)
        filtered = filtered.query(query_str)
    user_lst = filtered["user_id"].to_list()
    return corpus.query("user_id in @user_lst")


def get_dict_corpus(corpus, size=10):
    """Return a part of the corpus based on the size"""
    return corpus[:size].T.to_dict("list")


def extract_list(df, str_sentence):
    return df[str_sentence].tolist()


def extract_pair_set(df):
    original_list = extract_list(df, "original")
    corrected_list = extract_list(df, "corrected")
    sentence_pair_set = {
        (original_list[i], corrected_list[i]) for i in range(len(original_list))
    }
    return sentence_pair_set


def annotation_search(
    final_corpus, agreementType, wordRange, nCorrections, sentenceType
):
    """
    This function takes as user input and returns the set of pairs (original sentence, corrected sentence).
    --------------------------
    Argument: final_corpus (final corpus in pandas data frame form)
              agreementType (Number of annotators who agreed with the correction - integer between 0 and 3)
              wordRange (Number of words in a sentence)
              nCorrections (number of corrections offered in the website)
              sentenceType (original / correct / both)
    Returns: a set of pairs (original sentence, corrected sentence) which meet the requirements specified
    """
    take_intersection = []  # contains the set of sentence pairs to be intersected
    if (
        agreementType > 3
        or agreementType < -1
        or nCorrections < 1
        or sentenceType > 1
        or sentenceType < -1
        or type(sentenceType) != int
    ):
        return set()  # return an empty set for invalid requirements
    elif agreementType >= 0 and agreementType <= 3:
        df = final_corpus[final_corpus["total_agree"] == agreementType][
            ["original", "corrected"]
        ]
        take_intersection.append(extract_pair_set(df))
    word_min = 0
    word_max = 100000
    str_list = []
    if wordRange != -1:
        word_min, word_max = wordRange
    if sentenceType == 0 or sentenceType == -1:
        str_list.append("original")
    elif sentenceType == 1:
        str_list.append("corrected")
    if sentenceType == -1:
        str_list.append("corrected")
    for str_sentenceType in str_list:
        df_min = pd.DataFrame(
            final_corpus[
                final_corpus[str_sentenceType].apply(lambda x: len(x.split()))
                >= word_min
            ][["original", "corrected"]]
        )
        df_max = pd.DataFrame(
            final_corpus[
                final_corpus[str_sentenceType].apply(lambda x: len(x.split()))
                <= word_max
            ][["original", "corrected"]]
        )
        take_intersection.append(extract_pair_set(df_min))
        take_intersection.append(extract_pair_set(df_max))
    if nCorrections > 0:
        df = final_corpus.groupby("original").nunique()
        original = set(df[df["corrected"] == nCorrections].index.tolist())
        original_df = pd.DataFrame(original, columns=["original"])
        original_count = pd.merge(
            original_df, final_corpus, how="left", on=["original"]
        )
        take_intersection.append(extract_pair_set(original_count))
    ss = take_intersection[0]
    for i in range(1, len(take_intersection)):
        ss = ss & take_intersection[i]
    return ss  # a set of pairs (original, corrected)


def get_target_sents(args):

    # Targeted corpus
    metadata_params = construct_metadata_dict(args)
    corpus = get_by_metadata(CORPUS, **metadata_params)
    res = corpus

    if args["corpusType"] == 1:
        res = res[~res["agree"].isna()]
        # filtered by agreementType
        res = annotation_search(
            res,
            args["agreementType"],
            args["wordRange"],
            args["nCorrections"],
            args["sentenceType"],
        )
        return res
    elif args["corpusType"] == 0:
        res = res[res["agree"].isna()]
    else:
        res = res
    res = get_by_range(res, args["sentenceType"], args["wordRange"])
    res = get_by_multiple_corrections(res, args["nCorrections"])[
        ["original", "corrected"]
    ]
    return extract_pair_set(res)


# def get_by_range(sent_type, range = (10, 15)):
#     mask =  (CORPUS[sent_type].str.len() >= range[0]) & (CORPUS[sent_type].str.len() <= range[1])
#     return CORPUS.loc[mask].T.to_dict('list')


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


def get_friends(soup, n=20):
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
    next_page = soup.find("li", {"class": "pager_next"})
    if next_page:
        time.sleep(1)
        href = next_page.contents[0]["href"]
        try:
            new_soup = BeautifulSoup(
                urlopen("https://lang-8.com" + href), "html.parser"
            )
            friends.extend(get_friends(new_soup, n - len(friends)))
        except:
            pass
    return friends


def get_documents(soup, n=20):

    """Get list of document/journal ids (only English journals)
    Args:
        soup (BeautifulSoup): BeautifulSoup object containing link to a user's journals list
        n (int, optional): Number of documents needed to get. Defaults to 20.
    Returns:
        list: list of integers/document_ids
    """
    documents = []
    for container in soup.find_all("div", {"class": "journals_flex"}):
        if container:
            if len(documents) == n:
                return documents
            doc_lang = container.find("li", {"class": "studying"}).text.strip().lower()
            if "english" == doc_lang.lower():
                doc_id = container.find_all("a")[1]["href"].rsplit("/", 1)[-1]
                documents.append(doc_id)
    next_page = soup.find("li", {"class": "pager_next"})
    if next_page:
        time.sleep(1)
        href = next_page.contents[0]["href"]
        try:
            new_soup = BeautifulSoup(
                urlopen("https://lang-8.com" + href), "html.parser"
            )
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
    if comments_field:
        return comments_field.find_all("div", {"class": "correction_box"})
    return None


def get_pair_sents(corrections):
    """Get defaultdict of original-corrected sentences. Corrected sentences are in list. Corrections are made by Lang8 users
    Args:
        corrections (list of Tags): list containing Tag elements
    Returns:
        defaultdict: dictionary of original-corrected sentences
    """
    pair_sents = defaultdict(list)
    if corrections:
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


def remove_duplicates(df, subset, inplace=False):
    """Removes all duplicates from the Dataframe, but the first one
    Args:
        df (Dataframe): pandas Dataframe
        subset (list): A list of columns to search for duplicates
        inplace (boolean): if True -> alters the given df, if False (default) -> creates a new df
    Returns:
        Dataframe: if inplace=False (default)
        None: if inplace=True
    """
    return df.drop_duplicates(keep="first", subset=subset, inplace=inplace)


def remove_n_less_sents(df, inplace=False, n=4):
    """Removes rows from the Dataframe where number of characters in 'original' is less than n
    Args:
        df (Dataframe): pandas Dataframe
        inplace: if True -> alters the given df, if False (default) -> creates a new df
        n: numbers of characters to query in original sentences
    Returns:
        Dataframe: if inplace=False (default)
        None: if inplace=True
    """
    return df.drop(df[df.original.str.len() < n].index, inplace=inplace)
