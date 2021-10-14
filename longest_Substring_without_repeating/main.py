
def find_string(string):
	if string == "":
		return 0
	string_length = 1
	string_for_test = []
	for first_num in range(len(string)):
		string_for_test = [string[first_num]]
		for next_num in range(first_num + 1, len(string)):
			if string[next_num] in string_for_test:
				break
			else:
				string_for_test.append(string[next_num])
				if string_length < len(string_for_test):
					string_length = len(string_for_test)

	return string_length

def main(string):
	output = 0

	for char in string:
		if string.count(char) > 1:
			print(find_string(string))
			return
		else:
			output = len(string)


	print(output)


if __name__ == "__main__":
	string = input("input string: ")
	print(find_string(string))