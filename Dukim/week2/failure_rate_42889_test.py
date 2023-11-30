import pytest

from failure_rate_42889 import solution



def test_case_1():
    assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]


def test_case_2():
    assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]


def test_case_3():
    assert solution(4, [2, 2, 2, 2]) == [2, 1, 3, 4]


def test_case_4():
    assert solution(4, [5, 5, 5, 5]) == [1, 2, 3, 4]


def test_case_5():
    assert solution(4, [1, 2, 3, 4, 5]) == [4, 3, 2, 1]

def test_case_6():
    assert solution(4, [1, 2, 3, 4]) == [4, 3, 2, 1]


def test_case_7():
    assert solution(4, [1, 2, 3]) == [3, 2, 1, 4]

def test_case_8():
    assert solution(2, [1, 1, 1, 1]) == [1, 2]


if __name__ == "__main__":
    target = solution
    pytest.main()
