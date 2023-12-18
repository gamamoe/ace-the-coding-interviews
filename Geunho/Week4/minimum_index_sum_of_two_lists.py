from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_by_list1 = {word: index for index, word in enumerate(list1)}
        index_by_list2 = {word: index for index, word in enumerate(list2)}

        answer = []
        minimum_index_sum = 2000
        for word in list1:
            if word in index_by_list1 and word in index_by_list2:
                index1 = index_by_list1[word]
                index2 = index_by_list2[word]

                index_sum = index1 + index2
                if index_sum == minimum_index_sum:
                    answer.append(word)
                elif index1 + index2 < minimum_index_sum:
                    minimum_index_sum = index_sum
                    answer = [word]

        return answer


solution = Solution()
assert solution.findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
) == ["Shogun"]
assert solution.findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["KFC", "Shogun", "Burger King"],
) == ["Shogun"]
assert solution.findRestaurant(
    ["happy", "sad", "good"],
    ["sad", "happy", "good"],
) == ["sad", "happy"]
