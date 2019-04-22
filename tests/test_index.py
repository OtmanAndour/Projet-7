import sys
sys.path.append(".")
import index as script
import requests
import json
from config import *
import codecs
import os
api_key = os.getenv("API_KEY")

def test_parse():
    assert script.parse("Dis moi où se trouve la Tour Eiffel") == "Tour Eiffel"

def test_google_maps_api_search(monkeypatch):
    """ Testing for the location Tour Eiffel"""
    search_params = {'key' : api_key, 'input' : "Tour Eiffel", 'inputtype' : 'textquery', 'fields' : 'geometry'}
    search_req = requests.get(search_url, params=search_params)
    with codecs.open("tests/test_google_maps_api.json","w", "utf-8-sig") as f:
        f.write(search_req.text)
        f.close()
    with codecs.open("tests/test_google_maps_api.json","r", "utf-8-sig") as f:
        results = json.loads(f.read())

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return results

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert script.google_maps_api_search('Tour Eiffel') == results

def test_get_latitude():
    data = {
        'candidates': [
            {'geometry': 
                {'location': 
                    {'lat': 48.85837009999999, 'lng': 2.2944813},
                 'viewport': 
                    {'northeast': 
                        {'lat': 48.85974697989273, 'lng': 2.29610765},
                     'southwest': 
                        {'lat': 48.85704732010728, 'lng': 2.29251745}}}}],
        'status': 'OK'}

    assert script.get_latitude(data) == data["candidates"][0]["geometry"]["location"]["lat"]

def test_get_longitude():
    data = {
        'candidates': [
            {'geometry': 
                {'location': 
                    {'lat': 48.85837009999999, 'lng': 2.2944813},
                 'viewport': 
                    {'northeast': 
                        {'lat': 48.85974697989273, 'lng': 2.29610765},
                     'southwest': 
                        {'lat': 48.85704732010728, 'lng': 2.29251745}}}}],
        'status': 'OK'}

    assert script.get_longitutde(data) == data["candidates"][0]["geometry"]["location"]["lng"]


def test_wikipedia_api_search(monkeypatch):
    """ Testing for the location Tour Eiffel"""
    wiki_params_infos.update({'pageids' : 1359783})
    wiki_req = requests.Session().get(wiki_url, params=wiki_params_infos)
    with codecs.open("tests/test_wiki_api.json","w", "utf-8-sig") as f:
        f.write(wiki_req.text)
        f.close()
    with codecs.open("tests/test_wiki_api.json","r", "utf-8-sig") as f:
        results = json.loads(f.read())

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass
        def json(self):
            return results

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert script.wikipedia_api_search({'pageids' : 1359783}, wiki_params_infos) == results