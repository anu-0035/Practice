class Solution:
    def rearrange(self, arr):
        pos = []
        neg = []
        
        # Separate positive and negative numbers
        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        
        i, j = 0, 0
        ans = []
        
        # Start with a positive number and then alternate
        while i < len(pos) and j < len(neg):
            ans.append(pos[i])
            ans.append(neg[j])
            i += 1
            j += 1
        
        ans += pos[i:] if i < len(pos) else neg[j:]
        
        return ans
