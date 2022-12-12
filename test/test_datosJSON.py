
import pytest
import os

diccionario = {"documents" : [{"_id":"i","model":"i","marca":"i","material":"i","group_set":" i","type":"i","weight":"i","price_day":"i","price_hour":"i","availible":"i","location":"i","serial":"i","fork":"i","imagen":"i"}]}


@pytest.mark.contieneInfo
def test_contieneInfo():

    ejecutar(diccionario)

    assert os.stat("./DataBase/bicisCarretera.json").st_size != 0