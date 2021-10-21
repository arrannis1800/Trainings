def main(l1, l2):
	output = []
	if l1 == "" and l2 == "":
		return output
	elif l1 == "":
		return l2.split()
	elif l2 == "":
		return l1.split()

	for l in l1.split(","):
		output.append(l)
	for l in l2.split(","):
		output.append(l)
	output.sort()
	return output

if __name__ == '__main__':
	l1 = input("input first list: ")
	l2 = input("input second list: ")
	print(main(l1, l2))
	