def main(s):
	length = 0
	output = ''
	palindrom = []
	string = []


	if len(s) <= 1:
		return(s)
	else:
		for first_char in range(len(s)):
			string = list(s[first_char])
			for next_char in range(first_char + 1, len(s)):
				string.append(s[next_char])
				if string == string[::-1] and length < len(string):
					length = len(string)
					palindrom = string.copy()
				elif string != string[::-1] and length < len(string):
					palindrom = string.copy()


		return output.join(palindrom)


if __name__ == '__main__':
	s = input("input string: ")
	print(main(s))