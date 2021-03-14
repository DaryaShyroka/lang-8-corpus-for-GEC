import json
from pathlib import Path
import os

profiles = None
parallel_sents = None

with open('lang-8_profiles.json') as json_file:
    profiles = json.load(json_file)

with open('parallel_sents.json') as json_file:
    parallel_sents = json.load(json_file)
    
def profile(id):
    return profiles[id]["metadata"]

def friends(id):
    return profiles[id]["friends"]

def documents(id):
    return profiles[id]["documents"]

def par_sents(doc_id):
    return parallel_sents[doc_id]