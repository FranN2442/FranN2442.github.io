import pytest
import os
from src import appJsonToHTML

items =appJsonToHTML.CheckWrite()

@pytest.mark.crear_HTML
def paginasBase():
    assert os.path.exists("html/PaginaCategorias.html") == True
    assert os.path.exists("html/PaginaMTB.html") == True
    assert os.path.exists("html/PaginaE-Bike.html") == True
    assert os.path.exists("html/PaginaCarretera.html") == True
