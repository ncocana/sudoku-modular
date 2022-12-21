# import module from another directory
from src.checkColumnas import checkColumnas
import test.casosTestSudoku
import pytest


@pytest.mark.checkColumnas
def test_checkColumnas():

    assert checkColumnas(test.casosTestSudoku.correct) == True
    assert checkColumnas(test.casosTestSudoku.incorrect) == False
    assert checkColumnas(test.casosTestSudoku.incorrect2) == False
    assert checkColumnas(test.casosTestSudoku.incorrect3) == False
    assert checkColumnas(test.casosTestSudoku.incorrect4) == True
    assert checkColumnas(test.casosTestSudoku.incorrect5) == True
    assert checkColumnas(test.casosTestSudoku.irregular) == True
    assert checkColumnas(test.casosTestSudoku.irregular2) == False