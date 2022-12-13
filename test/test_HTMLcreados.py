import pytest
import os
from src import appJsonToHTML

@pytest.mark.crear_HTML
def test_paginasBase():
    assert os.path.exists("docs/Index.html") == True
def test_paginasMTB():    
    assert os.path.exists("docs/PaginaMTB.html") == True
def test_paginasEBike():    
    assert os.path.exists("docs/PaginaE-Bike.html") == True
def test_paginasCarretera():
    assert os.path.exists("docs/PaginaCarretera.html") == True
