
def main(array):
	output = []
	if len(array) <= 2:
		return output

	array = list(map(int, array))
	for first_num in range(len(array)):
		for sec_num in range(first_num + 1, len(array)):
			for thrird_num in range(sec_num + 1, len(array)):
				if array[first_num] + array[sec_num] + array[thrird_num] == 0:
					print("ok")
					output.append([array[first_num], array[sec_num], array[thrird_num]])

	return output

if __name__ == '__main__':
	array = input("integer array = ").split(",")
	print(main(array))