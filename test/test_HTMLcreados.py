import pytest
import os
from src import appJsonToHTML

@pytest.mark.crear_HTML
def paginasBase():
    assert os.path.exists("docs/PaginaCategorias.html") == True
    assert os.path.exists("docs/PaginaMTB.html") == True
    assert os.path.exists("docs/PaginaE-Bike.html") == True
    assert os.path.exists("docs/PaginaCarretera.html") == True
