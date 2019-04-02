import index as script 
import pytest

def test_parse():
    assert script.parse("Dis moi où se trouve la Tour Eiffel") == "Tour Eiffel"

    