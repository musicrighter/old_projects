def gcd(a, b):
	if b % a == 0:
		return a
	r = b % a
	if a % r == 0:
		return r
	r1 = a % r
	if r % r1 == 0:
		return r1
	else:
		while r1 != 0:
			r = r % r1
			if r == 0:
				return r1
			r1 = r1 % r
		return r

a = int(input('a: '))
b = int(input('b: '))
n = a
m = b
if a > b:
	a = m
	b = n

ans = gcd(a,b)
print('\nThe G.C.D. of', a, 'and', b, 'is:', ans)