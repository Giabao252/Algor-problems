class Solution: 
	def isPalindrome(self, x: int) -> bool: 
		if x < 0: 
			return False

		divider = 10

		while x >= 10*divider:
			divider *= 10

		while x:
			left = x // divider
			right = x % 10

			if right != left: 
				return False
			x = (x % divider) // 10

			return True 

