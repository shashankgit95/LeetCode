from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord('a')] += 1
            arr_tuple = tuple(arr)
            get_list = result.setdefault(arr_tuple,[])
            get_list.append(string)
            result[arr_tuple] = get_list
        return result.values()