from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        num_of_elements = len(code)
        if k == 0:
            return [0] * num_of_elements

        answer = []
        padded_code = code + code
        start_index = 0 if k > 0 else num_of_elements
        for index in range(start_index, start_index + num_of_elements):
            if k > 0:
                sum_of_elements = sum(padded_code[index + 1 : index + 1 + k])
            else:
                sum_of_elements = sum(padded_code[index + k : index])
            answer.append(sum_of_elements)

        return answer


s = Solution()
assert s.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert s.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert s.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
