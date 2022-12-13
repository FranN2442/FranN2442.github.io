import pytest
import os 
from src import appJsonToHTML

@pytest.mark.paginasMarcas
def test_Canyon():
    assert os.path.exists("docs/PaginaCanyon.html") == True
def test_Specialized():
    assert os.path.exists("docs/PaginaSpecialized.html") == True
def test_Mondraker():
    assert os.path.exists("docs/PaginaMondraker.html") == True
def test_BH():
    assert os.path.exists("docs/PaginaBH.html") == True
    