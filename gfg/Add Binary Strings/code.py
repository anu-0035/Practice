#User function Template for python3
# class Solution:
#     def num(self,s):
#         s = s[::-1]
#         x = 0
#         for i in range(len(s)):
#             if  s[i] == "1":
#                 x += (2 ** i)
#         return x
    
# 	def addBinary(self, s1, s2):
# 		# code here
# 		s1 = self.num(s1)
# 		s2 = self.num(s2)
# 		return bin(s1+s2)[2:]
class Solution:
	def addBinary(self, s1, s2):
		# code here
		return bin(int(s1, 2) + int(s2, 2))[2:]
