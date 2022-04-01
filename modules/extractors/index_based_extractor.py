# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import pickle
import requests


def extract_resources(text_question, answer_list):
    dictionary = {}
    dictionary["input-text"] = text_question
    dictionary["indexname"] = "tripleindextyped"
    dictionary["size"] = 10
    text = json.dumps(dictionary)
    resp = requests.get('http://ea-test.cs.upb.de:5000/get-triples-by-text', json=dictionary).json()
    entityset = set()
    relationset = set()
    answerset = set()
    answerset.add(answer_list)
    for triple in resp['triples']:
        if not triple['subject'] in answerset:
            entityset.add(triple['subject'])
        relationset.add(triple['predicate'])
        if not triple['object'] in answerset and 'http' in triple['object']:
            entityset.add(triple['object'])
    return list(entityset), list(relationset), list(answerset)
