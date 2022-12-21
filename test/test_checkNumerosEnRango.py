# import module from another directory
from src.checkNumerosEnRango import checkNumerosEnRango
import test.casosTestSudoku
import pytest


@pytest.mark.checkNumerosEnRango
def test_checkNumerosEnRango():

    assert checkNumerosEnRango(test.casosTestSudoku.correct) == True
    assert checkNumerosEnRango(test.casosTestSudoku.incorrect) == True
    assert checkNumerosEnRango(test.casosTestSudoku.incorrect2) == True
    assert checkNumerosEnRango(test.casosTestSudoku.incorrect3) == False
    assert checkNumerosEnRango(test.casosTestSudoku.incorrect4) == False
    assert checkNumerosEnRango(test.casosTestSudoku.incorrect5) == False
    assert checkNumerosEnRango(test.casosTestSudoku.irregular) == False
    assert checkNumerosEnRango(test.casosTestSudoku.irregular2) == True