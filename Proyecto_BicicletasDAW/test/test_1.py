import pytest
import src.appJsonToHTML 

items = src.appJsonToHTML.cargarDatos()

def test_1():
    assert src.appJsonToHTML.PaginaCategorias(items)== PaginaCategorias.html

    