from flask import Flask,request
from key import *
import requests
import json


app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
wiki_url = "https://fr.wikipedia.org/w/api.php"

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
    print(var_parsed)
    #print (search_json)
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
        'prop':'extracts',
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