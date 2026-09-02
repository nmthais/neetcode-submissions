class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            # Anagrams have the exact same sorted string key
            key = "".join(sorted(string))
            groups[key].append(string)

        return list(groups.values())