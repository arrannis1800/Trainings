nums = [3,2,4]
target = 6


def find_solution(nums,target):
	quantity = len(nums)
	num = 0
	num2 = 0
	while num < quantity:
		while num2 < quantity:
			if num == num2:
				pass
			elif(nums[num] + nums[num2] == target):
				print(f"[{num},{num2}]")
				return
			num2 +=1
		num +=1
	


find_solution(nums,target)