# import module from another directory
from src.checkSudoku import checkSudoku
import test.casosTestSudoku
import pytest


@pytest.mark.checkSudoku
def test_checkSudoku():

    assert checkSudoku(test.casosTestSudoku.correct) == True
    assert checkSudoku(test.casosTestSudoku.incorrect) == False
    assert checkSudoku(test.casosTestSudoku.incorrect2) == False
    assert checkSudoku(test.casosTestSudoku.incorrect3) == False
    assert checkSudoku(test.casosTestSudoku.incorrect4) == False
    assert checkSudoku(test.casosTestSudoku.incorrect5) == False
    assert checkSudoku(test.casosTestSudoku.irregular) == False
    assert checkSudoku(test.casosTestSudoku.irregular2) == False