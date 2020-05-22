def sq(x):
	return x*x
n=int(input("Enter a number"))
print(f"square of {n} is {sq(n)}")

for i in range(n):
	print(f'square of {i} is {sq(i)}')
