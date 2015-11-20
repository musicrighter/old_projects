def switch(a,b):
	for i in range(len(a)):
		if a[i] < len(b):
			a[i] = b[i]

a = [1,2,3]
b = [4,5,6]
c = a

done = switch(a,b)
print(c)
