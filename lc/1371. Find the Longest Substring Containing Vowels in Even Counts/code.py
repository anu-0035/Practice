class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a':1,'e':2,'i':4,'o':8,'u':16}
        res,mask = 0,0
        mask_idx = [-1] * 32
        for i,c in enumerate(s):
            mask = mask ^ vowels.get(c,0)
            if mask_idx[mask] != -1 or mask == 0 :
                length = i - mask_idx[mask]
                res = max(res,length)
            else:
                mask_idx[mask] = i
            
        return res
        
