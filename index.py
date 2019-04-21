#! /usr/bin/env python
# coding: utf-8
"""Main file for the website."""


from flask import Flask,request
from config import *
import requests
import json
import random
import os

api_key = os.getenv("API_KEY")
app = Flask(__name__)

def parse(research):
        """Parse the research"""
        research_parsed = ""
        for word in research.split():            #Parsing the research
                if word not in base_word:
                        research_parsed = research_parsed + word + " "             
        research_parsed = research_parsed[:-1]          #Parsed researched
        return research_parsed

def google_maps_api_search(search):
    """Searches a location through Google Maps API """
    search_params = {'key' : api_key, 'input' : search, 'inputtype' : 'textquery', 'fields' : 'geometry'}
    search_req = requests.get(search_url, params=search_params)
    search_json = search_req.json()
    return search_json

def get_latitude(result):
        """ Retrieves location latitude"""
        return result["candidates"][0]["geometry"]["location"]["lat"]

def get_longitutde(result):
        """ Retrieves location longitude """
        return result["candidates"][0]["geometry"]["location"]["lng"]


def wikipedia_api_search(search,params):
    """ Searches the location's Wikipedia info through the API"""
    params.update(search)   
    wiki_req = requests.Session().get(wiki_url, params=params)
    wiki_json = wiki_req.json()
    return wiki_json


""" Main route for the html webpage """  
@app.route('/')
def helloIndex():
        with open('templates/index.html', 'r') as f:
                return f.read()
        
""" Route for the search answer webpage """ 
@app.route('/result')
def result():
        user_research = request.args.get('name') 
        user_research_parsed = parse(user_research)
        search_json = google_maps_api_search(user_research_parsed)
        if search_json["status"] == 'ZERO_RESULTS':
                return json.dumps("No results")
        else:
                latitude = get_latitude(search_json)
                longitude = get_longitutde(search_json)
                wiki_json_pageid = wikipedia_api_search({'srsearch' : user_research_parsed}, wiki_params_pageid)
                pageid = wiki_json_pageid['query']['search'][0]['pageid']
                wiki_json_infos = wikipedia_api_search({'pageids' : pageid}, wiki_params_infos)
                quote = abe_quotes[random.randint(0,len(abe_quotes)-1)]
                response = {'latitude' : latitude, 'longitude' : longitude, 'page' : wiki_json_infos, 'quote' :quote}
                return json.dumps(response)

if __name__ == "__main__":
    app.run(port= 80)