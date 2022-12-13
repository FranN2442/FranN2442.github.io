import pytest
import os 
from src import appJsonToHTML

@pytest.mark.paginasMarcas
def paginasMarcas():

    assert os.path.exists("html/Canyon.html") == True
    assert os.path.exists("html/specialized.html") == True
    assert os.path.exists("html/Mondraker.html") == True
    assert os.path.exists("html/BH.html") == True
    