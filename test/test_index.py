import index as script 
import urllib.request
from io import BytesIO
import json
import pytest

def test_parse():
    assert script.parse("Dis moi où se trouve la Tour Eiffel") == "Tour Eiffel"

def test_http_return(tmpdir, monkeypatch):
    results = {
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

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    p = tmpdir.mkdir("program").join("search.json")

    # run script
    script.search(["--dest", str(p)])

    local_res = json.load(open(p))
    assert local_res == script.google_maps_api_search("Tour Eiffel")
