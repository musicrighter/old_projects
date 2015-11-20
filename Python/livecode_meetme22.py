def merge(a,b):
	'''Merge two sorted lists.
	Args:
		a: A sorted list (0 <= i < j < len(a) -> a[i] <= a[j])
		b: A sorted list (elements comparable of elements in a and b)
	Returns:
		a sorted list containing the union of elements in a and b
	'''
	posA, posB = 0, 0
	merged_list = []

	while posB < len(b) and posA < len(a):
		if a[posA] <= b[posB]:
			merged_list.append(a[posA])
			posA += 1
		else:
			merged_list.append(b[posB])
			posB += 1
	if posA == len(a):
		merged_list = merged_list + b[posB:]
	else:
		merged_list = merged_list + a[posA:]


	# while len(merged_list) < len(a) + len(b):
	# 	if posA == len(a):
	# 		merged_list.append(b[posB])
	# 		posB += 1
	# 	elif posB == len(a):
	# 		merged_list.append(a[posA])
	# 		posA += 1
	# 	elif a[posA] <= b[posB]:
	# 		merged_list.append(a[posA])
	# 		posA += 1
	# 	else:
	# 		merged_list.append(b[posB])
	# 		posB += 1

	return merged_list

class Mergeable():

	def __init__(self, a):
		self.mylist = sorted(a)

	def class_merge(self, other):
		return Mergeable(self.mylist, other.mylist)

def main():
	'''test it'''
	print(merge([1,3,5], [0,2,5,7]))

main()