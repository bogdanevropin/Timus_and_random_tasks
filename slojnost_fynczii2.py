def get_input():
	x1, x2 = map(int, input().split())
	n = x2 - x1 + 1
	i = 0
	while i < n:
		for v in map(int, input().split()):
			yield v
			i += 1

def solve():
	data = iter(get_input())
	prev = next(data)
	answer = 1
	dir_ = 0
	for v in data:
		cur_dir = 1 if v > prev else (-1 if v < prev else 0)
		if cur_dir:
			if dir_ and cur_dir != dir_:
				answer += 1
				dir_ = 0
			else:
				dir_ = cur_dir
		prev = v
	return answer

if __name__ == '__main__':
	print(solve())