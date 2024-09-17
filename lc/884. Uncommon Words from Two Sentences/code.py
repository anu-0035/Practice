class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # counts = Counter(chain(s1.split(),s2.split()))
        # return [k for k,v in counts.most_common() if v == 1]
        count1 = Counter(s1.split(" "))
        count2 = Counter(s2.split(" "))
        set1 = [w1 for w1 in count1.keys() if count1[w1] <= 1 and count2[w1] <= 1]
        set2 = [w2 for w2 in count2.keys() if count1[w2] <= 1 and count2[w2] <= 1]

        return list(set(set1) - set(set2)) + list(set(set2) - set(set1))
        
