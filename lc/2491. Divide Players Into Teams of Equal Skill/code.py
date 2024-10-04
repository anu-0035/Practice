class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill = skill[0] + skill[-(1)]
        ans = 0
        for i in range(len(skill)//2):
            if skill[i] + skill[-(i+1)] != total_skill:
                return -1 
            ans += (skill[i] * skill[-(i+1)])
        return ans
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().dividePlayers(nums),file=f)
exit(0)        
