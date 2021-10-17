
def main(height):
	height = list(map(int, height))
	print(height)
	max_container = 0
	container = 0

	for first_num in range(len(height)):
		for sec_num in range(first_num + 1, len(height)):
			if height[first_num] > height[sec_num]:
				container = height[sec_num] * (sec_num - first_num)
			else:
				container = height[first_num] * (sec_num - first_num)


			if container > max_container:
				max_container = container

	return max_container

if __name__ == '__main__':
	height = input("heights = ").split(",")
	print(main(height))