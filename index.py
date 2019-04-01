from flask import Flask,request
from constants import *
import requests
import json



app = Flask(__name__)



#def parse(research):
#        """Parse the research"""
#        research_parsed = ""
#        for word in research.split():            #Parsing the research
#                if word not in base_word:
#                        research_parsed = research_parsed + word + " "             
#        research_parsed = research_parsed[:-1]          #Parsed researched
#        return research_parsed
#
#def google_maps_api_search(search):
#    search_params = {'key' : api_key, 'input' : search, 'inputtype' : 'textquery', 'fields' : 'geometry'}
#    search_req = requests.get(search_url, params=search_params)
#    search_json = search_req.json()
#    return search_json
#
#def get_latitude(result):
#        return result["candidates"][0]["geometry"]["location"]["lat"]
#
#def get_longitutde(result):
#        return result["candidates"][0]["geometry"]["location"]["lng"]
#
#
#def wikipedia_api_search(search,params):
#    wiki_req = requests.Session().get(wiki_url, params=params)
#    wiki_json = wiki_req.json()
#    return wiki_json
#

@app.route('/')  #Main route for the html webpage
def helloIndex():
    with open('templates/index.html', 'r') as f:
        return f.read()
        

@app.route('/test')  #Route for another webpage
def testIndex():
    var = request.args.get('name') #Fetches the user research
    var_parsed = ""
    for word in var.split():            #Parsing the research
        if word not in base_word:
                var_parsed = var_parsed + word + " "             #Parsed researched
    var_parsed = var_parsed[:-1]
    search_params = {'key' : api_key, 'input' : var_parsed, 'inputtype' : 'textquery', 'fields' : 'geometry'}
    search_req = requests.get(search_url, params=search_params)
    search_json = search_req.json()
    if search_json["status"] == 'ZERO_RESULTS':
            print("Je ne vois pas de quel endroit tu parles, mon poussin")
            return json.dumps("No results")
    else:
        latitude = search_json["candidates"][0]["geometry"]["location"]["lat"]
        longitude = search_json["candidates"][0]["geometry"]["location"]["lng"]

        wiki_params = {'action': "query",'list':"search",'srsearch': var_parsed, 'format': "json" }    
        wiki_req = requests.Session().get(wiki_url, params=wiki_params)
        wiki_json = wiki_req.json()
        pageid = wiki_json['query']['search'][0]['pageid']
        
        wiki_params =  {
                'pageids': pageid,
                'action':'query',
                'utf8':True,
                'format':'json',
                'prop':'extracts|info',
                'inprop':'url',
                'exlimit':1,
                'explaintext':True,
                'exsentences':3,
                'exsectionformat':'plain',
                'exintro':True,}
        wiki_req = requests.Session().get(wiki_url, params=wiki_params)
        wiki_json = wiki_req.json()
        print(wiki_json)

        dico = {'latitude' : latitude, 'longitude' : longitude, 'page' : wiki_json}
        
        return json.dumps(dico)

app.run(port= 80)