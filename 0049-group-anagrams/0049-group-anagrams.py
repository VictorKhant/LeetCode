class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp in dic.keys():
                dic[temp] += [s]
            else:
                dic[temp] =[s]
        return list(dic.values())
