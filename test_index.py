import index as script
import requests

def test_parse():
    assert script.parse("Dis moi où se trouve la Tour Eiffel") == "Tour Eiffel"

#def test_map_return(monkeypatch):
#    """ Testing for the location Tour Eiffel"""
#    results = {
#        'candidates': [
#            {'geometry': 
#                {'location': 
#                    {'lat': 48.85837009999999, 'lng': 2.2944813},
#                 'viewport': 
#                    {'northeast': 
#                        {'lat': 48.85974697989273, 'lng': 2.29610765},
#                     'southwest': 
#                        {'lat': 48.85704732010728, 'lng': 2.29251745}}}}],
#        'status': 'OK'}
#
#    class MockRequestsGet:
#        def __init__(self, url, params=None):
#            pass
#        def json(self):
#            return results
#
#    monkeypatch.setattr('requests.get', MockRequestsGet)
#
#    assert script.google_maps_api_search('Tour Eiffel') == results

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



#def test_map_return(monkeypatch):
#    """ Testing for the location Tour Eiffel"""
#    results = {'batchcomplete': '', 'continue': {'sroffset': 10, 'continue': '-||'}, 'query': {'searchinfo': {'totalhits': 3556}, 'search': [{'ns': 0, 'title': 'Tour Eiffel', 'pageid': 1359783, 'size': 125424, 'wordcount': 14106, 'snippet': 'Pour les articles homonymes, voir <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> (homonymie). <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> Le Champ-de-Mars au premier plan,
#               la <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span> au deuxième, puis les jardins du', 'timestamp': '2019-03-31T21:21:17Z'}, {'ns': 0, 'title': 'Histoire de la tour Eiffel', 'pageid': 688954, 'size': 108893, 'wordcount': 11493, 'snippet': 'comprendront parfaitement Gustave <span class="searchmatch">Eiffel</span> et son équipe d\'ingénieurs, grâce aux expériences passées des ateliers <span class="searchmatch">Eiffel</span>. La <span
#               class="searchmatch">tour</span> de Babel vue par Pieter Brueghel', 'timestamp': '2019-03-26T13:46:06Z'}, {'ns': 0, 'title': 'Gustave Eiffel', 'pageid': 12801, 'size': 43444, 'wordcount': 5154, 'snippet': 'sources\xa0? Gustave <span class="searchmatch">Eiffel</span> Portrait de Gustave <span class="searchmatch">Eiffel</span> en 1893 selon l\'Illustration. Signature Gustave <span class="searchmatch">Eiffel</span>, né Bonickhausen dit <span class="searchmatch">Eiffel</span> le 15 décembre 1832', 'timestamp': '2019-04-04T20:03:26Z'}, {'ns': 0, 'title': 'La Tour Eiffel', 'pageid': 1662824, 'size': 2026, 'wordcount': 268, 'snippet': 'correspondants. La <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> (La torre <span class="searchmatch">Eiffel</span>) est une nouvelle de Dino Buzzati, incluse dans le recueil Le K publié en 1966. L\'ingénieur Gustave <span class="searchmatch">Eiffel</span>, avant', 'timestamp': '2019-03-29T08:20:22Z'}, {'ns': 0, 'title': 'Données techniques de la tour Eiffel', 'pageid': 664163, 'size': 12530, 'wordcount': 31, 'snippet': 'tableaux ci-dessous indiquent les principales spécificités techniques de la <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span>, le premier inventoriant les dimensions de l\'édifice, le deuxième étant', 'timestamp': '2019-03-09T11:35:07Z'}, {'ns': 0, 'title': 'Répliques et imitations de la tour Eiffel', 'pageid': 573472, 'size': 26224, 'wordcount': 2566, 'snippet': 'mars 1889 et immédiatement couronnée d\'un certain succès populaire, la <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span> a fait vite l\'objet de l\'admiration ou de la jalousie d\'autres pays[réf', 'timestamp': '2019-01-29T08:23:02Z'}, {'ns': 0, 'title': "Représentation de la tour Eiffel dans l'art et la culture", 'pageid': 619279, 'size': 46823, 'wordcount': 2851, 'snippet': 'champagne à la <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span> pour chaque scène se déroulant à Paris. En 1949, Burgess Meredith réalise L\'Homme de la <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span> (The man on the <span class="searchmatch">Eiffel</span> Tower),', 'timestamp': '2019-03-26T00:49:52Z'}, {'ns': 0, 'title': 'Radio Tour Eiffel', 'pageid': 341714, 'size': 11283, 'wordcount': 1362, 'snippet': 'doit pas être confondu avec Radio Service <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> ou <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> 95.2. Radio <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> Radio <span class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> est la première station de radio créée en', 'timestamp': '2018-07-22T17:41:27Z'}, {'ns': 0, 'title': "Société d'exploitation de la tour Eiffel", 'pageid': 7186932, 'size': 5096, 'wordcount': 649, 'snippet': 'construction, la <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span> a été exploitée jusqu\'en 1979 par la Société de la <span
#               class="searchmatch">Tour</span> <span class="searchmatch">Eiffel</span> (STE), structure fondée par Gustave <span class="searchmatch">Eiffel</span>. De 1980 à 2005', 'timestamp': '2018-05-06T18:37:20Z'}, {'ns': 0, 'title': 'Chronologie de la tour Eiffel', 'pageid': 606556, 'size': 52229, 'wordcount': 4737, 'snippet': 'future <span class="searchmatch">tour</span> <span class="searchmatch">Eiffel</span>). Mai 1884\xa0: Émile Nouguier et Maurice Koechlin, respectivement chef du bureau des méthodes et chef du bureau d\'études de G.<span class="searchmatch">Eiffel</span> &amp; Cie', 'timestamp': '2019-04-08T14:27:57Z'}]}}
#
#    class MockRequestsGet:
#        def __init__(self, url, params=None):
#            pass
#        def json(self):
#            return results
#
#    monkeypatch.setattr('requests.get', MockRequestsGet)
#
#    assert script.wikipedia_api_search({'srsearch' : "Tour Eiffel"}, wiki_params_pageid) == results