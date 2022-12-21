# import module from another directory
from src.checkFilas import checkFilas
import test.casosTestSudoku
import pytest


@pytest.mark.checkFilas
def test_checkFilas():

    assert checkFilas(test.casosTestSudoku.correct) == True
    assert checkFilas(test.casosTestSudoku.incorrect) == False
    assert checkFilas(test.casosTestSudoku.incorrect2) == False
    assert checkFilas(test.casosTestSudoku.incorrect3) == True
    assert checkFilas(test.casosTestSudoku.incorrect4) == True
    assert checkFilas(test.casosTestSudoku.incorrect5) == True
    assert checkFilas(test.casosTestSudoku.irregular) == True
    assert checkFilas(test.casosTestSudoku.irregular2) == True