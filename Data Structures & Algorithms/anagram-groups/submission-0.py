class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        aList = []
        for i, n in enumerate(strs):
            if tuple(sorted(n)) in hashMap:
                hashMap[tuple(sorted(n))].append(i)
            else:
                hashMap[tuple(sorted(n))] = [i]

        for values in hashMap.values():
            aList.append([strs[i] for i in values])

        return aList