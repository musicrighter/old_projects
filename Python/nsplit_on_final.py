def nsplit(lis, border):
	empty = []
	cur = []
	if lis == []:
		return lis
	for num in lis:
		if num != border:
			cur.append(num)
		elif cur != []:
			empty.append(cur) 
			cur = []
	if cur != []:
		empty.append(cur)
	return empty

print(nsplit([0,2,5,0,3,4,9,0,1,0,31,0,3,0,0,4,1,0,0], 0))

