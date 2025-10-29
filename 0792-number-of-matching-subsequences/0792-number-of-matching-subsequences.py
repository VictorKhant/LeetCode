from bisect import bisect_right
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexMap = defaultdict(list)
        count = 0
        for i, c in enumerate(s):
            indexMap[c].append(i)
        for word in words:
            if self.isValid(word, indexMap):
                count += 1
        return count
    
    def isValid(self, word, indexMap):
        prevIndex = -1
        for c in word:
            if c in indexMap:
                currIndexList = indexMap[c]
                index = bisect_right(currIndexList, prevIndex)
                if index == len(currIndexList):
                    return False
                prevIndex = currIndexList[index]
            else:
                return False
        return True

