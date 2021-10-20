def main(s):
	s_new = []

	if s[0] in [")", "}", "]"] or s[-1] in ["(", "{", "["] or len(s)%2!=0:
		return "false"
		
	for i in s:
		if i in["(", "{", "["]:
			s_new.append(i)
		elif (i == ")" and s_new[-1] == "(") or (i == "}" and s_new[-1] == "{") or (i == "]" and s_new[-1] == "["):
			s_new.pop()
		else:
			return "false"

	return "true"


if __name__ == '__main__':
	s = input("input string: ")
	print(main(s))