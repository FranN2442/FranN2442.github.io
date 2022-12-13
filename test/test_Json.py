from src.appJsonToHTML import cargarDatos
import pytest
import os

documento = {
    "documents": 
        [
            {
                "_id": "X",
                "brand": "X",
                "material": "X",
                "goup_sproket": "X",
                "model": "X",
                "size": "X",
                "transmission": "X",
                "weigth": "X",
                "price day": "X",
                "price hour": "X",
                "location": "X",
                "availible": "X",
                "serial": "X",
                "type": "X"
            }
        ]
    }

@pytest.mark.test_noVacio
def test_noVacio():
    cargarDatos(documento)
    assert os.stat("../Database/bicisCarretera.json")
