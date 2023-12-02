import pytest

from visit_49994 import solution



def test_case_1():
    assert solution('ULURRDLLU') == 7

def test_case_2():
    assert solution('LULLLLLLU') == 7


if __name__ == "__main__":
    target = solution
    pytest.main()
