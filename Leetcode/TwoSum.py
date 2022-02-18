'''' 
TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order '''

#input: nums=[2,7,5] target=9
#output: [0,1]

#Brute force approach
class Solution: 
	def(self, nums: List[int], target: int):
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] == target - nums[j]:
					return [i,j]
