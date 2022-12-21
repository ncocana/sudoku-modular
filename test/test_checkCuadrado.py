# import module from another directory
from src.checkCuadrado import checkCuadrado
import test.casosTestSudoku
import pytest


@pytest.mark.checkCuadrado
def test_checkCuadrado():

    assert checkCuadrado(test.casosTestSudoku.correct) == True
    assert checkCuadrado(test.casosTestSudoku.incorrect) == True
    assert checkCuadrado(test.casosTestSudoku.incorrect2) == True
    assert checkCuadrado(test.casosTestSudoku.incorrect3) == True
    assert checkCuadrado(test.casosTestSudoku.incorrect4) == True
    assert checkCuadrado(test.casosTestSudoku.incorrect5) == True
    assert checkCuadrado(test.casosTestSudoku.irregular) == False
    assert checkCuadrado(test.casosTestSudoku.irregular2) == False