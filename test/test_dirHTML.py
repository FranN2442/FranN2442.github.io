import pytest
import os 
from src import appJsonToHTML

def test_2():
    paginasIndividuales = os.listdir("html/PaginasIndividuales")
    countList = len(paginasIndividuales)
    assert countList >=1