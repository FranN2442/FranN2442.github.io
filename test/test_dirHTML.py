import pytest
import os 
from src import appJsonToHTML

@pytest.mark.filesDocs()
def test_2():
    docs = os.listdir("docs")
    countList = len(docs)
    assert countList >=1