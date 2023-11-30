import pytest

from exam_42840 import solution

def test_case_1():
    assert solution([1,2,3,4,5]) == [1]

def test_case_2():
    assert solution([1,3,2,4,2]) == [1,2,3]


if __name__ == "__main__":
    target = solution
    pytest.main()
