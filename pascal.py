#Pascal.py (Lab 3) [Shane Roeseberg]

def pascal_tri(n):

    if n == 1:
        return [1]

    else:
        line = [1]
        existing_line = pascal_tri(n - 1)

        for x in range(len(existing_line) - 1):
            line.append(existing_line[x] + existing_line[x + 1])
        line += [1]

    return line
for i in range(1,11):
	print(pascal_tri(i))

def pascal(n, k):

	if k > n:
		print("K cannot be greater than N")
		exit(1)

	if n == 0:
		return 1

	elif n == k or k == 0:
		return 1

	else:
		return pascal (n - 1, k - 1) + pascal (n - 1, k)

print(pascal(4,2),6)