lists = [[1,4,5],[1,3,4],[2,6]]

def main(lists):
	output = []
	for l in lists:
		for el in l:
			output.append(el)

	output.sort()
	return output

if __name__ == '__main__':
	print(main(lists))