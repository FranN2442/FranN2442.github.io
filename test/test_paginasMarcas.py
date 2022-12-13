import pytest
import os 
from src import appJsonToHTML

@pytest.mark.paginasMarcas
def paginasMarcas():

    assert os.path.exists("docs/Canyon.html") == True
    assert os.path.exists("docs/specialized.html") == True
    assert os.path.exists("docs/Mondraker.html") == True
    assert os.path.exists("docs/BH.html") == True
    