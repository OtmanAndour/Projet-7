from flask import Flask,request
from key import *
import requests
import json


app = Flask(__name__)
base_word = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô",'Dis']
PARAM_EXTRAC = {
        'action':'query',
        'utf8':True,
        'format':'json',
        'prop':'extracts',
        'exlimit':1,
        'explaintext':True,
        # 'exsentences':3,
        'exsectionformat':'plain',
        'exintro':True,}
#PARAM_SEARCH = {'action': "query",'list':"search",
#    'srsearch': var_parsed, 'format': "json" }

search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"
wiki_url = "https://fr.wikipedia.org/w/api.php"

@app.route('/')  #Main route for the html webpage
def helloIndex():
    with open('index.html', 'r') as f:
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
    

    
    
    #place_id = search_json["candidates"][0]['place_id']
    #details_params = {'key' : api_key, 'placeid' : place_id}
    #details_resp = requests.get(details_url, params=details_params)
    #details_json = details_resp.json()

    return json.dumps(dico)

app.run(port= 80)