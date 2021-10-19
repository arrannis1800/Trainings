
def main(head, n):
	head.pop(len(head) - n)
	return head

if __name__ == '__main__':
	head = list(map(int,input("input list: ").split(",")))
	n = int(input("input n: "))
	print(main(head, n))